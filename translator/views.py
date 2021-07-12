from django.shortcuts import render
from rest_framework import generics, status
from .serializers import IPAWordSerializer
from .models import IPA_word
from rest_framework.views import APIView
from rest_framework.response import Response
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import speech_recognition as sr
import librosa
import soundfile as sf

def text_to_speech(text):
        apikey = 'D-9ovhbJSav8hbrn01fs4wKGTgM1DnSlMiNhYKnW6-if'
        url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/2bb74fb6-0f0d-4482-abee-ec1b51dd1e3e'
        authenticator = IAMAuthenticator(apikey)
        tts = TextToSpeechV1(authenticator=authenticator)
        tts.set_service_url(url)
        phoneme = f"<phoneme alphabet='ipa' ph='{text}'></phoneme>"
        #print(type(phoneme))
        with open('./speech.wav', 'wb') as audio_file:
            res = tts.synthesize(phoneme, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
            audio_file.write(res.content)

def speech_to_text():
        x,_ = librosa.load('speech.wav', sr=16000)
        sf.write('speech.wav', x, 16000)
        r = sr.Recognizer()

        with sr.AudioFile("speech.wav") as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                # print("predicting this: ")
                # print(text)
                return text
            except:
                #print("Didn't work...gotta try again")
                return "Didn't work"
class CreateIPATranslator(APIView):
    serializer_class = IPAWordSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            IPA_string = serializer.data.get('IPA_string')
            text_to_speech(IPA_string)
            translated = speech_to_text()
            return Response(translated, status=status.HTTP_200_OK)
    
    


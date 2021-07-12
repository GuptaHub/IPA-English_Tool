from rest_framework import serializers
from .models import IPA_word

class IPAWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPA_word
        field = '_all_'
        exclude = ()
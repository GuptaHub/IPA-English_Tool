import React, { useState, useRef, useEffect } from 'react';
import TodoList from './TodoList'
import uuidv4 from 'uuid/v4'
import './App.css'
const LOCAL_STORAGE_KEY = 'todoApp.todos'

function App(){
  const textRef = useRef();
  const outputRef = useRef();
  const translatedRef = useRef();
  function handleSearch(e){
    const name = textRef.current.value
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        IPA_string: name
      })
    }
    fetch("../../translator/", requestOptions)
    .then((response) => response.json())
    .then((data) => outputRef.current.value = data);
  }
  return (
    <>
      <h1 className="Title">IPA To English Translator</h1>
      <a href="/ToolInfo" className="InfoLink">
        What's this?
      </a>
        
      <textarea className="textBox" ref={textRef} type="text" name="paragraph_text" cols="30" rows="10"></textarea>
        
      
      <div className="arrow_pos">
        
          <img src="../static/images/arrow_webapp.png" className="arrow"/>
        
      </div>

      <textarea className="outputBox" ref={outputRef} type="text" cols="30" rows="10"></textarea>
  
      <button className="TransButton" onClick={handleSearch}>Translate</button>
      <div class="ocean">
        <div class="wave"></div>
        <div class="wave"></div>
      </div>
    </>
  )
}
export default App;
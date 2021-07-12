//django application will render a template (like plain vanilla html) and then react will take control of it and fill it in
import App from "./components/App";
import { render } from "react-dom";
import React from 'react';

const appDiv = document.getElementById("app");
render(<App/>, appDiv);
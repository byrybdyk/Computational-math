import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  let currentURL = window.location.href;
  let pageName = "";
  if (
    currentURL === "http://localhost:3000/lb2" ||
    currentURL === "http://dr-chainsaw.ru/lb2"
  ) {
    pageName = "Lab 2";
  }
  if (
    currentURL === "http://localhost:3000/lb3" ||
    currentURL === "http://dr-chainsaw.ru/lb3"
  ) {
    pageName = "Lab 3";
  }
  if (
    currentURL === "http://localhost:3000/lb4" ||
    currentURL === "http://dr-chainsaw.ru/lb4"
  ) {
    pageName = "Lab 4";
  }
  return (
    <header className="header">
      <div class="header-container">
        <a className="main-header-item" href="/" target="_blank">
          {" "}
          <h2>Computational math</h2>
        </a>
        <a className="header-item" href={currentURL} target="_blank">
          {" "}
          <h2>{pageName}</h2>
        </a>
        <a className="header-item" target="_blank">
          {" "}
          <h2>Zarubov Egor</h2>
        </a>
        <a className="header-item" target="_blank">
          {" "}
          <h2>P3218</h2>
        </a>
      </div>
    </header>
  );
}

import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="header">
        
        <div class="header-container">
            <a className="main-header-item" href="/" target="_blank"> <h2>Computational math</h2></a>
            <a className="header-item" href="/lb2" target="_blank"> <h2>Lab 2</h2></a>
            <a className="header-item"  target="_blank"> <h2>Zarubov Egor</h2></a>
            <a className="header-item" target="_blank"> <h2>P3218</h2></a>
        </div>
            
            
    </header>
  );
}

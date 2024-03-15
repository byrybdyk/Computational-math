import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
    return (
        <div>
            <h1>Добро пожаловать на главную страницу!</h1>
            <Link to="/lb2page">Lab Work 2</Link>
        </div>
    );
}

export default HomePage;

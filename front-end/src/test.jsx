import React, { useState } from 'react';
import { Link } from "react-router-dom";

function TestPage() {
    const [response, setResponse] = useState('');
    const [number1, setNumber1] = useState('');
    const [number2, setNumber2] = useState('');
    const [result, setResult] = useState('');

    const fetchData = async () => {
        try {
            const res = await fetch('http://localhost:8080/hello');
            const data = await res.text();
            setResponse(data);
        } catch (error) {
            console.error('Ошибка при получении данных:', error);
        }
    };

    const handleSubmit = async () => {
        try {
            const response2 = await fetch(`http://localhost:8080/run-python-script?argument1=${number1}&argument2=${number2}`);
            const data = await response2.text();
            setResponse(data);
        } catch (error) {
            console.error('Ошибка при получении данных:', error);
        }
    };

    return (
        <div>
            <h1>Пример REST-запроса на Spring Boot приложение</h1>
            <button onClick={fetchData}>Отправить запрос</button>
            <div>
                <h2>Ответ:</h2>
                <pre>{response}</pre>
            </div>
            <h2>Калькулятор</h2>
            <input
                type="number"
                placeholder="Первое число"
                value={number1}
                onChange={(e) => setNumber1(e.target.value)}
            />
            <input
                type="number"
                placeholder="Второе число"
                value={number2}
                onChange={(e) => setNumber2(e.target.value)}
            />
            <button onClick={handleSubmit}>Отправить</button>
            <div>
                <h3>Результат:</h3>
                <p>{response}</p>
            </div>
        </div>
    );
}

export default TestPage;

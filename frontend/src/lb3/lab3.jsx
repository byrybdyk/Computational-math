import React, { useState } from "react";
import Header from "../components/Header";

function LB3Page() {
  const [selectedMethod, setSelectedMethod] = useState("");
  const handleMethodChange = (option) => {
    setSelectedMethod(option);
  };

  const [selectedQuation, setSelectedQuation] = useState("");
  const handleQuationChange = (option) => {
    setSelectedQuation(option);
  };

  const [leftBorder, setLeftBorder] = useState("");
  const [rightBorder, setRightBorder] = useState("");
  const [inaccuary, setInaccuary] = useState("");
  const [parts, setParts] = useState("");

  const [response, setResponse] = useState("");

  // Обработчики изменения значений в полях ввода
  const handleChangeLeftBorder = (event) => {
    let value = event.target.value; // Получаем значение из поля ввода
    if (value.length > 3) {
      value = value.slice(0, 5); // Если длина больше 3 символов, обрезаем до 3 символов
    }
    setLeftBorder(value); // Обновляем состояние
  };

  const handleChangeRightBorder = (event) => {
    let value = event.target.value; // Получаем значение из поля ввода
    if (value.length > 3) {
      value = value.slice(0, 5); // Если длина больше 3 символов, обрезаем до 3 символов
    }
    setRightBorder(value); // Обновляем состояние
  };

  const handleChangeInaccuary = (event) => {
    let value = event.target.value; // Получаем значение из поля ввода
    if (value.length > 8) {
      value = value.slice(0, 5); // Если длина больше 3 символов, обрезаем до 3 символов
    }
    setInaccuary(value); // Обновляем состояние
  };

  const handleChangeParts = (event) => {
    let value = event.target.value; // Получаем значение из поля ввода
    if (value.length > 8) {
      value = value.slice(0, 5); // Если длина больше 3 символов, обрезаем до 3 символов
    }
    setParts(value); // Обновляем состояние
  };

  const handleBlurParts = () => {
    if (parts === "") {
      setParts(4); // Устанавливаем значение по умолчанию, если поле пустое
    }
  };

  // const url = "dr-chainsaw.ru";
  const url = "localhost:8080";
  const fetchData = async () => {
    const lbname = 3;
    try {
      if (
        !selectedQuation ||
        !selectedMethod ||
        !leftBorder ||
        !rightBorder ||
        !inaccuary ||
        !parts
      ) {
        setResponse("Not all variables are selected");
        throw new Error("Not all variables are selected");
      }
      const response = await fetch(
        `http://${url}/api/run-python-script_lb${lbname}?quation=${selectedQuation}&method=${selectedMethod}&leftBorder=${leftBorder}&rightBorder=${rightBorder}&inaccuary=${inaccuary}&parts=${parts}`
      );
      const data = await response.text();
      setResponse(data);
    } catch (error) {
      console.error("Ошибка при получении данных:", error);
    }
  };
  // const [response, setResponse] = useState("");
  return (
    <div>
      <Header />
      <div className="input">
        <div className="left_block">
          <div className="method-container">
            <button
              onClick={() => handleMethodChange("1")}
              style={{
                backgroundColor:
                  selectedMethod === "1"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              Rectangle method (left)
            </button>

            <button
              onClick={() => handleMethodChange("2")}
              style={{
                backgroundColor:
                  selectedMethod === "2"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              Rectangle method (centre)
            </button>

            <button
              onClick={() => handleMethodChange("3")}
              style={{
                backgroundColor:
                  selectedMethod === "3"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              Rectangle method (right)
            </button>
            <button
              onClick={() => handleMethodChange("4")}
              style={{
                backgroundColor:
                  selectedMethod === "4"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              Trapezoidal method
            </button>
            <button
              onClick={() => handleMethodChange("5")}
              style={{
                backgroundColor:
                  selectedMethod === "5"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              Simpson’s Method
            </button>
          </div>
          <div className="quation-container">
            <button
              onClick={() => handleQuationChange("1")}
              style={{
                backgroundColor:
                  selectedQuation === "1"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              1/x
            </button>

            <button
              onClick={() => handleQuationChange("2")}
              style={{
                backgroundColor:
                  selectedQuation === "2"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              x^2
            </button>

            <button
              onClick={() => handleQuationChange("3")}
              style={{
                backgroundColor:
                  selectedQuation === "3"
                    ? "rgb(100, 113, 205)"
                    : "rgb(0, 113, 205)",
              }}
            >
              x
            </button>
          </div>
          <div className="borders_lb3">
            <label>
              <input
                type="number"
                placeholder="Left"
                value={leftBorder}
                onChange={handleChangeLeftBorder}
                style={{ color: "white" }}
              />
            </label>
            <label>
              <input
                type="number"
                placeholder="Right"
                value={rightBorder}
                onChange={handleChangeRightBorder}
                style={{ color: "white" }}
              />
            </label>
            <label>
              <input
                className="inaccuary"
                type="number"
                placeholder="inaccuary"
                value={inaccuary}
                onChange={handleChangeInaccuary}
                style={{ color: "white" }}
              />
            </label>
            <label>
              <input
                className="parts"
                type="number"
                placeholder="parts"
                value={parts}
                onChange={handleChangeParts}
                onBlur={handleBlurParts}
                defaultValue={"4"}
                style={{ color: "white" }}
              />
            </label>
            <label>
              <button
                type="submit"
                className="calculate-button"
                style={{ color: "white" }}
                onClick={fetchData}
              >
                Calculate
              </button>
            </label>
          </div>
        </div>
        <div className="right_block">
          <div className="answer">
            <div className="answer-zone">
              <h2>
                <pre
                  className="answer-zone"
                  style={{ color: "white", fontSize: "20px" }}
                >
                  {response}
                </pre>
              </h2>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default LB3Page;

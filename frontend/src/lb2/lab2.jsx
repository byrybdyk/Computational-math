import React, { useState } from "react";
import { Link } from "react-router-dom";
import Header from "../components/Header";
import Switch, { switchClasses } from "@mui/joy/Switch";
import Stack from "@mui/joy/Stack";
import Typography from "@mui/joy/Typography";
import GraphLB2 from "../components/GraphLB2";
import SystemGraphLB2 from "../components/SystemGraphLB2";
import SaveToFileButton from '../components/SaveToFileButton';
import Desmos_graph from "../components/Desmos_graph";
import Desmos_system_graph from "../components/Desmos_system_graph";
// import Desmos from '../components/Desmos_graph';

function LB2Page() {
  const url = "dr-chainsaw.ru";
  
    // const url = "localhost:8080";

  const [checked, setChecked] = useState(false);

  const handleChange = () => {
    setChecked(!checked);
  };

  const [selectedQuation, setSelectedQuation] = useState("");
  const [selectedSystem, setSelectedSystem] = useState("");
  const handleQuationChange = (option) => {
    setSelectedQuation(option);
  };

  const [selectedMethod, setSelectedMethod] = useState("");
  const [selectedSystemMethod, setSelectedSystemMethod] = useState("");
  const handleMethodChange = (option) => {
    setSelectedMethod(option);
  };

  const handleSystemChange = (option) => {
    setSelectedSystem(option);
  };

  const handleSystemMethodChange = (option) => {
    setSelectedSystemMethod(option);
  };

  const [leftBorder, setLeftBorder] = useState("");
  const [rightBorder, setRightBorder] = useState("");
  const [inaccuary, setInaccuary] = useState("");

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

  const fetchData = async () => {
    const lbname = 2;
    try {
      if (checked) {
        if (!selectedQuation || !selectedMethod || !leftBorder || !rightBorder || !inaccuary) {
          alert("Not all variables are selected");
          throw new Error('Not all variables are selected');
        }
        const response = await fetch(
          `http://${url}/api/run-python-script?lbname=${lbname}&type=${checked}&quation=${selectedQuation}&method=${selectedMethod}&leftBorder=${leftBorder}&rightBorder=${rightBorder}&inaccuary=${inaccuary}`
        );
        const data = await response.text();
        setResponse(data);
      } else {
        if (!selectedSystem || !selectedSystemMethod || !leftBorder || !rightBorder || !inaccuary) {
          alert("Not all variables are selected");
          throw new Error('Not all variables are selected');
        }
        const response = await fetch(
          `http://${url}/api/run-python-script?lbname=${lbname}&type=${checked}&quation=${selectedSystem}&method=${selectedSystemMethod}&leftBorder=${leftBorder}&rightBorder=${rightBorder}&inaccuary=${inaccuary}`
        );
        const data = await response.text();
        setResponse(data);
      }
    } catch (error) {
      console.error("Ошибка при получении данных:", error);
    }
  };
  
  const [response, setResponse] = useState("");

  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleFileUpload = async () => {
    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch(`http://${url}/api/send-file`, {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const data = await response.text();
                setResponse(data);
                console.log('Файл успешно загружен!');
            } else {
                console.error('Произошла ошибка при загрузке файла:', response.status);
            }
        } catch (error) {
            console.error('Ошибка при отправке запроса:', error);
        }
    } else {
        alert('Пожалуйста, выберите файл перед отправкой.');
    }
};


  return (
    <div>
      <Header />
      <div className="input">
        <div className="left_block">
          <div className="switch">
            <Stack direction="row" spacing={2}>
              <Switch
                checked={checked}
                onChange={(event) => setChecked(event.target.checked)}
                color="success"
                slotProps={{
                  track: {
                    children: (
                      <React.Fragment>
                        <span>System</span>
                        <span>Single</span>
                      </React.Fragment>
                    ),
                    sx: {
                      justifyContent: "space-around",
                    },
                  },
                }}
                sx={{
                  "--Switch-thumbSize": "50px",
                  "--Switch-trackWidth": "400px",
                  "--Switch-trackHeight": "61px",
                  "--Switch-thumbRadius": "50px",
                  "--Switch-thumbSize": "50px",
                }}
                sx={(theme) => ({
                  "--Switch-thumbShadow": "0 3px 7px 0 rgba(0 0 0 / 0.12)",
                  "--Switch-thumbSize": "50px",
                  "--Switch-trackWidth": "400px",
                  "--Switch-trackHeight": "61px",
                  "--Switch-trackBackground": "rgb(0, 113, 205)",
                  "--Switch-thumbColor": "rgb(0, 113, 205)",
                  [`& .${switchClasses.thumb}`]: {
                    transition: "width 0.4s, left 0.4s",
                  },
                  [`&:hover, &.${switchClasses.checked}`]: {
                    "--Switch-trackBackground": "rgb(0, 113, 205)",
                  },
                  "&:active": {
                    "--Switch-thumbWidth": "32px",
                    "--webkit-transition": "background-color 2s",
                  },
                  [`&.${switchClasses.checked}`]: {
                    "--Switch-trackBackground": "rgb(100, 113, 205)",
                    "--webkit-transition": "background-color 2s",
                  },
                  [`&.${switchClasses.checked}:hover`]: {
                    "--Switch-trackBackground": "rgb(100, 113, 205)",
                  },
                })}
              />
            </Stack>
          </div>

          {checked ? (
            <Typography variant="body1">
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
                  x^2 - 3x + 2
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
                  x^3 + 2x^2 - 5
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
                  sin(x) - cos(x)
                </button>
              </div>
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
                  Half division method
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
                  Newton method
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
                  Simple iteration method
                </button>
                <div>
                    <input type="file" onChange={handleFileChange} />
                    <button onClick={handleFileUpload}>Send File</button>
                    <SaveToFileButton response={response} />
                </div>
              </div>
            </Typography>
          ) : (
            <Typography>
              <div className="quation-container">
                <button
                  onClick={() => handleSystemChange("1")}
                  style={{
                    backgroundColor:
                      selectedSystem === "1"
                        ? "rgb(100, 113, 205)"
                        : "rgb(0, 113, 205)",
                  }}
                >
                  0.1x^2 +x + 0.2y^2 - 0.3  <br></br>
                  0.2x^2 + y + 0.1xy -0.7
                </button>

                <button
                  onClick={() => handleSystemChange("2")}
                  style={{
                    backgroundColor:
                      selectedSystem === "2"
                        ? "rgb(100, 113, 205)"
                        : "rgb(0, 113, 205)",
                  }}
                >
                  3y^2+0.5x^2-x<br></br>
                  sin(x)^2-y
                </button>
              </div>
              <div className="method-container">
                

                <button
                  onClick={() => handleSystemMethodChange("1")}
                  style={{
                    backgroundColor:
                      selectedSystemMethod === "1"
                        ? "rgb(100, 113, 205)"
                        : "rgb(0, 113, 205)",
                  }}
                >
                  Simple iteration method
                </button>
                <div>
                    <input type="file" onChange={handleFileChange} />
                    <button onClick={handleFileUpload}>Send File</button>
                    <SaveToFileButton response={response} />
                </div>
              </div>
            </Typography>
          )}
        </div>
        <div className="right_block">
          <div className="graph">
          {checked ? (
            <Typography>
              
                <Desmos_graph 
                leftBorder={leftBorder}
                rightBorder={rightBorder}
                quationNumber={selectedQuation}
                />
              
              
            </Typography>
          ):
          (<Typography>
            <Desmos_system_graph
            leftBorder={leftBorder}
            rightBorder={rightBorder}
            systemNumber={selectedSystem}
            />
            {/* <SystemGraphLB2
                    leftBorder={leftBorder}
                    rightBorder={rightBorder}
                    systemNumber={selectedSystem}
                /> */}
          </Typography>)
          }
            
          </div>
          <div className="borders">
            
            <label>
              <input
                type="number"
                maxLength="3"
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
          <div className="answer">
            <div className="answer-zone">
              <h2></h2>
              <pre className="answer-zone" style={{ color: "white" }}>
                {response}
              </pre>
            </div>
          </div>
        </div>
      </div>

      {/* <h1>LB2</h1>
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
            </div> */}
            
            {/* <script>
                var elt = document.getElementById('calculator');
                var calculator = Desmos.GraphingCalculator(elt);
              </script> */}
    </div>
  );
}

export default LB2Page;

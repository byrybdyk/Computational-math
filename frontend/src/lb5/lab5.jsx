import React, { useState } from "react";
import Header from "../components/Header";
// import DesmosGraph from "./Desmos_graph";
import SaveToFileButton from "./SaveToFileButton";
import Switch, { switchClasses } from "@mui/joy/Switch";
import Stack from "@mui/joy/Stack";
import Typography from "@mui/joy/Typography";
function LB5Page() {
  // const url = "dr-chainsaw.ru";
  const url = "localhost:8080";

  const [checked, setChecked] = useState(false);

  const handleChange = () => {
    setChecked(!checked);
  };

  const [pairs, setPairs] = useState({
    pair1: "",
    pair2: "",
    pair3: "",
    pair4: "",
    pair5: "",
    pair6: "",
    pair7: "",
    pair8: "",
    pair9: "",
    pair10: "",
    pair11: "",
    pair12: "",
  });

  function truncateString(str, maxLength) {
    if (str.length > maxLength) {
      return str.slice(0, maxLength);
    }
    return str;
  }

  const [selectedQuation, setSelectedQuation] = useState("");
  const handleQuationChange = (option) => {
    setSelectedQuation(option);
  };
  const [file, setFile] = useState(null);
  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleFileUpload = async () => {
    if (file) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch(`http://${url}/api/send-file-lb4`, {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          const data = await response.text();
          let [firstPart, rest] = splitFirstLine(data);
          setFirstLine(firstPart);
          setResponse(rest);
          console.log("Файл успешно загружен!");
        } else {
          console.error(
            "Произошла ошибка при загрузке файла:",
            response.status
          );
        }
      } catch (error) {
        console.error("Ошибка при отправке запроса:", error);
      }
    } else {
      alert("Пожалуйста, выберите файл перед отправкой.");
    }
  };

  const handleChangePair1 = (event) => handleChangePairs(event, "pair1");
  const handleChangePair2 = (event) => handleChangePairs(event, "pair2");
  const handleChangePair3 = (event) => handleChangePairs(event, "pair3");
  const handleChangePair4 = (event) => handleChangePairs(event, "pair4");
  const handleChangePair5 = (event) => handleChangePairs(event, "pair5");
  const handleChangePair6 = (event) => handleChangePairs(event, "pair6");
  const handleChangePair7 = (event) => handleChangePairs(event, "pair7");
  const handleChangePair8 = (event) => handleChangePairs(event, "pair8");
  const handleChangePair9 = (event) => handleChangePairs(event, "pair9");
  const handleChangePair10 = (event) => handleChangePairs(event, "pair10");
  const handleChangePair11 = (event) => handleChangePairs(event, "pair11");
  const handleChangePair12 = (event) => handleChangePairs(event, "pair12");

  let handleChangePairs = (event, pairName) => {
    let { value } = event.target;
    value = truncateString(value, 11);
    setPairs((prevPairs) => ({
      ...prevPairs,
      [pairName]: value,
    }));
  };
  const [firstLine, setFirstLine] = useState("");
  function splitFirstLine(str) {
    const [firstPart, rest] = str.split("space", 2);

    return [firstPart, rest];
  }

  function validatePairs() {
    for (let i = 1; i <= 8; i++) {
      const pairName = "pair" + i;
      if (pairs[pairName] === "") {
        setResponse("Please fill in all fields (1-8).");
        return false; // Если хотя бы одно поле пустое, возвращаем false
      }
    }
    setResponse("Vatting response from remote server");
    return true;
  }
  const [response, setResponse] = useState("");

  const [leftBorder, setLeftBorder] = useState("");
  const [rightBorder, setRightBorder] = useState("");
  const [dots, setDots] = useState("");

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

  const handleChangeDots = (event) => {
    let value = event.target.value; // Получаем значение из поля ввода
    if (value.length > 8) {
      value = value.slice(0, 5); // Если длина больше 3 символов, обрезаем до 3 символов
    }
    setDots(value); // Обновляем состояние
  };

  const fetchData = async () => {
    const lbname = 5;
    try {
      if (checked) {
        if (!selectedQuation || !leftBorder || !rightBorder || !dots) {
          // alert("Not all variables are selected");
          setResponse("Not all variables are selected");
          throw new Error("Not all variables are selected");
        }
      } else {
        if (!validatePairs()) {
          throw new Error("Not all variables are selected");
        }
      }
      try {
        const response = await fetch(
          `http://${url}/api/run-python-script_lb${lbname}?type=${checked}&quation=${selectedQuation}&leftBorder=${leftBorder}&rightBorder=${rightBorder}&dots=${dots}&pair1=${pairs.pair1}&pair2=${pairs.pair2}&pair3=${pairs.pair3}&pair4=${pairs.pair4}&pair5=${pairs.pair5}&pair6=${pairs.pair6}&pair7=${pairs.pair7}&pair8=${pairs.pair8}&pair9=${pairs.pair9}&pair10=${pairs.pair10}&pair11=${pairs.pair11}&pair12=${pairs.pair12}`
        );
        const data = await response.text();
        let [firstPart, rest] = splitFirstLine(data);
        setFirstLine(firstPart);
        setResponse(rest);
      } catch (error) {
        console.error("Ошибка при получении данных:", error);
      }
    } catch (error) {
      console.error("Ошибка при получении данных:", error);
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
                        <span>Coordinates</span>
                        <span>Functions</span>
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
              <div className="quation-containerLB5">
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
                  x^3 - 2x^2 - 5
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
                      className="dots"
                      type="number"
                      placeholder="num dots"
                      value={dots}
                      onChange={handleChangeDots}
                      style={{ color: "white" }}
                    />
                  </label>
                </div>
              </div>
            </Typography>
          ) : (
            <Typography variant="body2">
              <div className="input_coordinates">
                <label>
                  <input
                    type="text"
                    placeholder="First coordinates"
                    value={pairs.pair1}
                    onChange={handleChangePair1}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="Second coordinates"
                    value={pairs.pair2}
                    onChange={handleChangePair2}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="Third coordinates"
                    value={pairs.pair3}
                    onChange={handleChangePair3}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="4'th coordinates"
                    value={pairs.pair4}
                    onChange={handleChangePair4}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="5'th coordinates"
                    value={pairs.pair5}
                    onChange={handleChangePair5}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="6'th coordinates"
                    value={pairs.pair6}
                    onChange={handleChangePair6}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="7'th coordinates"
                    value={pairs.pair7}
                    onChange={handleChangePair7}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="8'th coordinates"
                    value={pairs.pair8}
                    onChange={handleChangePair8}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="9'th coordinates"
                    value={pairs.pair9}
                    onChange={handleChangePair9}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="10'th coordinates"
                    value={pairs.pair10}
                    onChange={handleChangePair10}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="11'th coordinates"
                    value={pairs.pair11}
                    onChange={handleChangePair11}
                    style={{ color: "white" }}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="12'th coordinates"
                    value={pairs.pair12}
                    onChange={handleChangePair12}
                    style={{ color: "white" }}
                  />
                </label>
                {/* <label>
                  <button
                    type="submit"
                    className="calculate-button"
                    onClick={fetchData}
                  >
                    Calculate
                  </button>
                </label> */}
              </div>
              <div>
                <input type="file" onChange={handleFileChange} />
                <button onClick={handleFileUpload}>Send File</button>
                <SaveToFileButton response={response} />
              </div>
            </Typography>
          )}
          <div className="input_coordinates">
            <label>
              <button
                type="submit"
                className="calculate-button"
                onClick={fetchData}
              >
                Calculate
              </button>
            </label>
          </div>
        </div>
        <div className="right_blockLB4">
          {/* <div className="centered">
            <DesmosGraph Fx={firstLine} pairs={pairs} />
          </div> */}
          <div className="answerLb4">
            <div className="answer-zoneLB4">
              <h2>
                <pre
                  className="answer-zoneLB4"
                  style={{ color: "white", fontSize: "16px" }}
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

export default LB5Page;

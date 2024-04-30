import React, { useState } from "react";
import Header from "../components/Header";
import DesmosGraph from "./Desmos_graph";
import SaveToFileButton from "./SaveToFileButton";
function LB4Page() {
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
  // const url = "dr-chainsaw.ru";
  const url = "localhost:8080";
  const fetchData = async () => {
    const lbname = 4;
    if (validatePairs()) {
      try {
        const response = await fetch(
          `http://${url}/api/run-python-script_lb${lbname}?pair1=${pairs.pair1}&pair2=${pairs.pair2}&pair3=${pairs.pair3}&pair4=${pairs.pair4}&pair5=${pairs.pair5}&pair6=${pairs.pair6}&pair7=${pairs.pair7}&pair8=${pairs.pair8}&pair9=${pairs.pair9}&pair10=${pairs.pair10}&pair11=${pairs.pair11}&pair12=${pairs.pair12}`
        );
        const data = await response.text();
        let [firstPart, rest] = splitFirstLine(data);
        setFirstLine(firstPart);
        setResponse(rest);
      } catch (error) {
        console.error("Ошибка при получении данных:", error);
      }
    }
  };

  return (
    <div>
      <Header />
      <div className="input">
        <div className="left_blockLB4">
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
          <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleFileUpload}>Send File</button>
            <SaveToFileButton response={response} />
          </div>
        </div>
        <div className="right_blockLB4">
          <div className="centered">
            <DesmosGraph Fx={firstLine} pairs={pairs} />
          </div>
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

export default LB4Page;

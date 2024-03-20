import React from 'react';
import Plot from "react-plotly.js";

export default function SystemGraphLB2({ leftBorder, rightBorder, systemNumber })  {
    // Массив значений x
    leftBorder -= 1;
    rightBorder += 1;
    const xValues = [];
    for (let i = leftBorder; i <= rightBorder; i += 0.01) {
        xValues.push(parseFloat(i.toFixed(1))); // Округляем до одного знака после запятой
    }

    let titleQuation = "";

    // Массив значений y, вычисленных по функции для каждого значения x
    const yValues1 = xValues.map(x => calculateFunction(x, systemNumber, 1));
    const yValues2 = xValues.map(x => calculateFunction(x, systemNumber, 2));
    // alert(xValues+" = "+ yValues1);

    function calculateFunction(x, systemNumber, functionNumber) {
        let result = 0;
        if (systemNumber === '1') {
            if (functionNumber === 1) {
                titleQuation = "Graph of the function f1(x) = x^2 - 3x + 2";
                return Math.sqrt((-0.1 * Math.pow(x, 2) - x + 0.3) / 0.2);
            } else {
                titleQuation = "Graph of the function f2(x) = x^3 - 2x^2 - 5";
                return  (0.7 - 0.2 * Math.pow(x, 2)) / (1 + 0.1 * x);
            }
        }
        if (systemNumber === '2') {
                if (functionNumber === 1) {
                    titleQuation = "Graph of the function f1(x) = x^2 - 3x + 2";
                    result = x * x - 3 * x + 2;
                } else {
                    titleQuation = "Graph of the function f2(x) = x^3 - 2x^2 - 5";
                    result = x * x * x + 2 * x * x - 5;
                }
        } else {
            titleQuation = "Graph";
            result = 0;
        }
        return result;
    }

    return (
        <div
            className="App"
            style={{
                display: "flex",
                justifyContent: "center",
                height: "220px",
            }}
        >
            <Plot
                data={[
                    {
                        x: xValues,
                        y: yValues1,
                        mode: "lines+markers", // Линии и точки на графике
                        type: "scatter",
                        name: "Function 1",
                    
                    },
                    {
                        x: xValues,
                        y: yValues2,
                        mode: "lines+markers", // Линии и точки на графике
                        type: "scatter",
                        name: "Function 2",
                    },
                ]}
                layout={{
                    title: titleQuation,
                    paper_bgcolor: 'white', // цвет заднего фона
                    // plot_bgcolor: 'lightblue', // цвет графика
                    width: 540, // ширина окна графика в пикселях
                    height: 295, // высота окна графика в пикселях
                    xaxis: {
                        title: "x",
                    },
                    yaxis: {
                        title: "f(x)",
                        scaleanchor: "f(x)", // Относительно оси X
                    },
                    aspectratio: { x: 1, y: 1 },
                }}
            />
        </div>
    );
}

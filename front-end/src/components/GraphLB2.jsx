import React from 'react'
import Plot from "react-plotly.js";

export default function GraphLB2() {
    // Массив значений x
const xValues = [];
for (let i = 1.5; i <= 2.5; i += 0.1) {
    xValues.push(parseFloat(i.toFixed(1))); // Округляем до одного знака после запятой
}

// Массив значений y, вычисленных по функции для каждого значения x
const yValues = xValues.map(x => calculateFunction(x));
const strings = Array.from({ length: 10 }, (_, index) => (index + 1).toString());
const yNumbers = Array.from({ length: 10 }, (_, index) => index + 1);
function calculateFunction(x) {
    return x * x - 3 * x + 2;
  }
    return (
        <div
          className="App"
          style={{
            display: "flex",
            justifyContent: "center",
            height: "300px",

          }}
        >
          <Plot
           data={[
            {
              x: xValues,
              y: yValues,
              mode: "lines+markers", // Линии и точки на графике
              type: "scatter",
            },
          ]}
          layout={{
            title: "Graph of the function f(x) = x^2 - 3x + 2",
            paper_bgcolor: 'white', // цвет заднего фона
            // plot_bgcolor: 'lightblue', // цвет графика
            width: 580, // ширина окна графика в пикселях
            height: 384, // высота окна графика в пикселях
            xaxis: {
              title: "x",
            },
            yaxis: {
              title: "f(x)",
                scaleanchor: "x", // Относительно оси X
            },
            aspectratio: { x: 1, y: 1 },
          }}
          />
        </div>
      );
}

import React from 'react'
import Plot from "react-plotly.js";

export default function GraphLB2({ leftBorder, rightBorder,quationNumber })  {
    // Массив значений x
  leftBorder -= 0.3*leftBorder;
  rightBorder *= 1.3;
const xValues = [];
for (let i = leftBorder; i <= rightBorder; i += 0.1) {
    xValues.push(parseFloat(i.toFixed(1))); 
}
let titleQuation = "a";
const yValues = xValues.map(x => calculateFunction(x,quationNumber));
const strings = Array.from({ length: 10 }, (_, index) => (index + 1).toString());
const yNumbers = Array.from({ length: 10 }, (_, index) => index + 1);
function calculateFunction(x, quationNumber) {
    if(quationNumber =='1'){
      titleQuation ="Graph of the function f(x) = x^2 - 3x + 2";
      return x * x - 3 * x + 2;
    }
    if(quationNumber =='2'){
      titleQuation ="Graph of the function f(x) = x^3 - 2x^2 - 5";
      return x*x*x + 2*x*x - 5;
    }
    else{
      titleQuation ="Graph of the function f(x) = sin(x)-cos(x)";
      return Math.sin(x) - Math.cos(x);
    }
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
              y: yValues,
              mode: "lines+markers",
              type: "scatter",
            },
          ]}
          layout={{
            title: titleQuation,
            paper_bgcolor: 'white', 

            width: 540,
            height: 295, 
            xaxis: {
              title: "x",
            },
            yaxis: {
              title: "f(x)",
                scaleanchor: "f(x)", 
            },
            aspectratio: { x: 1, y: 1 },
          }}
          />
        </div>
      );
}

import React, { useEffect, useRef } from "react";
import Desmos from "desmos";

function DesmosGraph({ Fx, pairs }) {
  const desmosContainerRef = useRef(null);

  useEffect(() => {
    // alert(Fx);
    let quations = Fx.split("zz");
    // alert(quations[4]);
    const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
    // calculator.setOptions({ expressions: false });
    let minX = 99999;
    let maxX = -999;
    for (let i = 1; i < 12; i++) {
      const pairName = "pair" + i;
      const [x, y] = pairs[pairName].split(" ");

      const xValue = parseFloat(x);
      const yValue = parseFloat(y);
      let id_name = "point" + i;
      calculator.setExpression({
        // id: id_name,
        latex: `(${xValue},${yValue})`,
        pointStyle: Desmos.Styles.POINT,
        color: "#ff0000",
      });

      if (xValue <= minX) {
        minX = pairs[pairName];
      }
      if (yValue >= maxX) {
        maxX = pairs[pairName];
      }
    }
    if (Object.keys(quations).length === 7) {
      calculator.setExpression({
        id: "graph1",
        latex: `${quations[0].replace("P1", "y")}`,
        color: "#461d9f",
      });

      calculator.setExpression({
        id: "graph2",
        latex: `${quations[1].replace("P1", "y")}`,
        color: "#FF5733",
      });
      calculator.setExpression({
        id: "graph3",
        latex: `${quations[2].replace("P1", "y")}`,
        color: "#6C5CE7",
      });

      calculator.setExpression({
        id: "graph4",
        latex: `${quations[3].replace("P1", "y")}`,
        color: "#F08A5D",
      });

      calculator.setExpression({
        id: "graph5",
        latex: `${quations[4].replace("P1", "y")}`,
        color: "#5F27CD",
      });
      calculator.setExpression({
        id: "graph6",
        latex: `${quations[5].replace("P1", "y")}`,
        color: "000",
      });
    }

    let left = parseFloat(minX) - 0.3 * parseFloat(minX);
    let right = parseFloat(maxX) + 0.3 * parseFloat(maxX);

    return () => {
      calculator.destroy();
    };
  }, [Fx, pairs]);

  return (
    <div ref={desmosContainerRef} style={{ width: "540px", height: "295px" }} />
  );
}

export default DesmosGraph;

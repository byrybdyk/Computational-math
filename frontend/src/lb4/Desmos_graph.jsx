import React, { useEffect, useRef } from "react";
import Desmos from "desmos";

function DesmosGraph({ Fx, pairs }) {
  const desmosContainerRef = useRef(null);
  let titleQuation = "";

  useEffect(() => {
    // alert(Fx);
    const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
    calculator.setOptions({ expressions: false });
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
    calculator.setExpression({
      id: "graph1",
      latex: `${Fx.replace("P1", "y")}`,
      color: "#461d9f",
    });
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

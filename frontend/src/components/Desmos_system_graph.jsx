import React, { useEffect, useRef } from 'react';
import Desmos from 'desmos';

function DesmosSystemGraph({ leftBorder, rightBorder, systemNumber }) {
  const desmosContainerRef = useRef(null);
  let equation1 = "";
  let equation2 = "";

  useEffect(() => {
    let left = parseFloat(leftBorder) - 0.3 * parseFloat(leftBorder);
    let right = parseFloat(rightBorder) + 0.3 * parseFloat(rightBorder);

    const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
    if (systemNumber === '1') {
      equation1 = "x = -0.1x^2- 0.2y^2+0.3";
      equation2 = "y = -0.2x^2 - 0.1xy+0.7";
      calculator.setOptions({ expressions: false });
    } else if (systemNumber === '2') {
      equation1 = "x=3y^2+0.5x^2";
      equation2 = "y\\ =\\sin\\left(x\\right)^{2}";
    } else {
      equation1 = "";
      equation2 = "";
    }

    calculator.setExpression({ id: 'graph1', latex: equation1 });
    calculator.setExpression({ id: 'graph2', latex: equation2 });

    // calculator.setMathBounds({
    //   left: left,
    //   right: right,
    //   bottom: -10,
    //   top: 10,
    // });

    return () => {
      calculator.destroy();
    };
  }, [systemNumber, leftBorder, rightBorder]);

  return <div ref={desmosContainerRef} style={{ width: '540px', height: '295px' }} />;
}

export default DesmosSystemGraph;

import React, { useEffect, useRef } from 'react';
import Desmos from 'desmos';

function DesmosGraph({ leftBorder, rightBorder, quationNumber }) {
  const desmosContainerRef = useRef(null);
  let titleQuation = "";

  useEffect(() => {
    let left = parseFloat(leftBorder) - 0.3 * parseFloat(leftBorder);
    let right = parseFloat(rightBorder) + 0.3 * parseFloat(rightBorder);

    const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
    if (quationNumber === '1') {
      titleQuation = "y=x^2-3x+2";
      calculator.setOptions({ expressions: false });
    } else if (quationNumber === '2') {
      titleQuation = "y=x^3+2x^2-5";
      calculator.setOptions({ expressions: false });
    } else if (quationNumber === '3') {
      titleQuation = "y\\ =\\ \\sin\\left(x\\right)-\\cos\\left(x\\right)";
    } else {
      titleQuation = "";
    }

    
    calculator.setExpression({ id: 'graph1', latex: titleQuation});

    calculator.setMathBounds({
      left: left,
      right: right,
      bottom: -10,
      top: 10,
    });

    

    return () => {
      calculator.destroy();
    };
  }, [quationNumber, leftBorder, rightBorder]);

  return <div ref={desmosContainerRef} style={{ width: '540px', height: '295px' }} />;
}

export default DesmosGraph;

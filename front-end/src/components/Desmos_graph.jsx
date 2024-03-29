import React, { useEffect, useRef } from 'react';
import Desmos from 'desmos';

function Desmos_graph({ quationNumber }) {
  const desmosContainerRef = useRef(null);
  let titleQuation = "";
  if(quationNumber =='1'){
    alert("A");
    titleQuation ="y=x^2-3x+2";
  }
  if(quationNumber =='2'){
    titleQuation ="y=x^3+2x^2-5";
  }
  if(quationNumber =='3'){
    titleQuation ="y=sin(x)-cos(x)";
  }
  else{
    titleQuation ="";
  }
  useEffect(() => {
    const calculator = Desmos.GraphingCalculator(desmosContainerRef.current);
    calculator.setExpression({ id: 'graph1', latex: titleQuation });

    return () => {
      calculator.destroy();
    };
  }, []);

  return <div ref={desmosContainerRef} style={{ width: '540px', height: '295px' }} />;
}

export default Desmos_graph;

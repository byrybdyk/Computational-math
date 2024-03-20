import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Home_page';
import LB2Page from './lb2/lab2';

function App() {
  return (
      <Router>
        <div className='background'>
            <div className='main'>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/lb2" element={<LB2Page/>}/>
                </Routes>
            </div>
            
        </div> 
      </Router>
  );
}

export default App;

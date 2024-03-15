import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Home_page';
import TestPage from './test';
import LB2Page from './lb2/lab2';

function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/test_page" element={<TestPage />} />
              <Route path="/lb2page" element={<LB2Page/>}/>
          </Routes>
      </Router>
  );
}

export default App;

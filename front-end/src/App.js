import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './Home_page';
import TestPage from './test';

function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/test_page" element={<TestPage />} />
          </Routes>
      </Router>
  );
}

export default App;

// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import Sidebar from './components/Sidebar';
import UserRegister from './components/UserRegister';
import LoginPage from './components/LoginPage';
import { Box } from '@mui/material';

function App() {
  return (
    <Router>
      <Box sx={{ display: 'flex' }}>
        {/* Sidebar for navigation */}
        <Sidebar />
        
        {/* Main content area */}
        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <Routes>
            {/* Home page route */}
            <Route path="/" element={<HomePage />} />
            
            <Route path="/user-register" element={<UserRegister />} />
            
            <Route path="/user-login" element={<LoginPage />} />
            {/* Add more routes here for other pages like User Management, Team Management, etc. */}
          </Routes>
        </Box>
      </Box>
    </Router>
  );
}

export default App;

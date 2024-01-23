// LoginPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './login-page.css';

const LoginPage = () => {
  const navigate = useNavigate()
  const [userId, setUserId] = useState('');
  const [password, setPassword] = useState('');

  const handleUserIdChange = (event) => {
    setUserId(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };


  const loginAdmin = async () => {
    try {
      // Perform the API request to get the session token
      const response = await fetch('http://127.0.0.1:8000/authorisation/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: userId,
          password: password,
        }),
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }
      console.log(response)
      // Parse the response and get the session token
      if(response.ok){
      const data = await response.json();
      const session_token = data.session_token;

      // Save the session token locally (you might want to use a more secure method)
      localStorage.setItem('sessionToken', session_token);

      // Determine the account type based on the username
      const isUserAdmin = userId.toLowerCase().includes('admin');

      // Redirect to the appropriate page
      if (isUserAdmin) {
        navigate('/admin');
      } else {
        navigate('/user');
      }
    }
    } catch (error) {
      console.error('Error during login:', error.message);
    }
  };

  const navigateToSignup = () => {
    // Redirect to the signup page
    navigate('/signup');
  };

  return (
    <div className="login-container">
      <img
        loading="lazy"
        src="https://static.wixstatic.com/media/85c200_6a8d1536dfb74604b5e839845c9795ff~mv2.png/v1/crop/x_4,y_0,w_229,h_62/fill/w_130,h_35,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Group%2031.png"
        className="img"
      />
      <div className="login-form">
        <h1>Welcome back!</h1>
        <p>Enter your details to login</p>
        <div className="form-input">
        <label htmlFor="yourUserId">User ID</label>
        <input
          type="text"
          id="yourUserId"
          placeholder="Enter your user ID"
          value={userId}
          onChange={handleUserIdChange}
        />
      </div>
      <div className="form-input">
        <label htmlFor="yourInputId">Password</label>
        <input
          type="password"
          id="yourInputId"
          placeholder="***********"
          value={password}
          onChange={handlePasswordChange}
        />
      </div>
        <div className="form-options">
          <div className="remember-me">
            <input type="checkbox" id="rememberMe" />
            <label htmlFor="rememberMe">Remember me</label>
          </div>
          <button className="forgot-password">Forgot password ?</button>
        </div>
        <div className="form-options">
          <button className="login-button" onClick={loginAdmin}>
            Log in
          </button>
          <button className="signup-button" onClick={navigateToSignup}>
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;

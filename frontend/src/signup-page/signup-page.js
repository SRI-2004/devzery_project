// src/SignupPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './signup-page.css'
const SignupPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    profession: '',
    location: '',
    phone_number: '',
    email_id: '',
    username: '',
    password: '',
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSignup = async () => {
    try {
      // Make a POST request to the signup API endpoint
      const response = await fetch('http://127.0.0.1:8000/authorisation/signup/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Signup failed');
      }

      // Redirect to the login page upon successful signup
      navigate('/login');
    } catch (error) {
      console.error('Error during signup:', error.message);
    }
  };

  return (
    <div className="login-container">
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/1a7462a3-86e2-4c9f-ae69-33a079f1a629?"
        className="img"
      />
      <div className="login-form">
        <h1>Sign Up</h1>
        <p>Enter your details to create an account</p>
        <div className="form-input">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Enter your name"
          />
        </div>
        <div className="form-input">
          <label htmlFor="age">Age</label>
          <input
            type="number"
            id="age"
            name="age"
            value={formData.age}
            onChange={handleChange}
            placeholder="Enter your age"
          />
        </div>
        <div className="form-input">
          <label htmlFor="profession">Profession</label>
          <input
            type="text"
            id="profession"
            name="profession"
            value={formData.profession}
            onChange={handleChange}
            placeholder="Enter your profession"
          />
        </div>
        <div className="form-input">
          <label htmlFor="location">Location</label>
          <input
            type="text"
            id="location"
            name="location"
            value={formData.location}
            onChange={handleChange}
            placeholder="Enter your location"
          />
        </div>
        <div className="form-input">
          <label htmlFor="phone_number">Phone Number</label>
          <input
            type="tel"
            id="phone_number"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
            placeholder="Enter your phone number"
          />
        </div>
        <div className="form-input">
          <label htmlFor="email_id">Email</label>
          <input
            type="email"
            id="email_id"
            name="email_id"
            value={formData.email_id}
            onChange={handleChange}
            placeholder="Enter your email"
          />
        </div>
        <div className="form-input">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            placeholder="Choose a username"
          />
        </div>
        <div className="form-input">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Choose a password"
          />
        </div>
        <button className="login-button" onClick={handleSignup}>
          Sign Up
        </button>
      </div>
    </div>
  );
};

export default SignupPage;

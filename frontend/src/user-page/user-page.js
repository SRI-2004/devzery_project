// src/UserPage.js
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './user-page.css';
const UserPage = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch user data using the locally stored session token
    const fetchUserData = async () => {
      try {
        // Get the session token from local storage
        const sessionToken = localStorage.getItem('sessionToken');

        // Make a POST request to the API with the session token
        const response = await fetch('http://127.0.0.1:8000/user/user_info/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            session_token: sessionToken,
          }),
        });

        if (!response.ok) {
          throw new Error('Failed to fetch user data');
        }

        // Parse the response and set the user state
        const userData = await response.json();
        const user_data = userData.user_details;
        console.log(user_data);
        setUser(user_data);
      } catch (error) {
        console.error('Error fetching user data:', error.message);
      }
    };

    fetchUserData();
  }, []); 

  const navigateToLogin = async () => {
    try {
      // Replace 'http://your-django-backend.com' with the actual URL of your Django backend
      const sessionToken = localStorage.getItem('sessionToken');
      const response = await fetch('http://127.0.0.1:8000/user/logout/', {
        method: 'POST',  // You might use 'GET' or 'DELETE' based on your backend setup
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_token: sessionToken,
        }),
      });

      if (response.ok) {
        // Successful logout, you can redirect or perform other actions here
        navigate('/')
        console.log('Logout successful');
      } else {
        // Handle errors or failed logout
        console.error('Logout failed');
      }
    } catch (error) {
      console.error('Error during logout:', error.message);
    }
  }
  return (
    <div className="user-container">
    <div className="top-row">
      <img
        className="logo"
        src="https://static.wixstatic.com/media/85c200_6a8d1536dfb74604b5e839845c9795ff~mv2.png/v1/crop/x_4,y_0,w_229,h_62/fill/w_130,h_35,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Group%2031.png"
        alt="Logo"
      />
      <div className="logout-btn">
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/ea8f6b4a-9a39-4c28-85ab-3a49dc1ef1e8?"
          alt="Logout Image"
        />
        <button onClick={navigateToLogin}>Log out</button>
      </div>
    </div>

    {user && (
      <div className="info-container">
        <div className="personal">
          <h2>Personal Info</h2>
          <div className="personal-details">
            <p className="name">{user.name}</p>
            <p className="info-item">Position: {user.profession}</p>
            <p className="info-item">Email: {user.email_id}</p>
            <p className="info-item">Phone Number: {user.phone_number}</p>
            <p className="info-item">Location: {user.location}</p>
          </div>
        </div>
        <div className="account">
          <h2>Account Info</h2>
          <div className="account-details">
            <p className="info-item">Age: {user.age}</p>
            <p className="info-item">ID: {user.unique_id}</p>
            <p className="info-item">username: {user.username}</p>
            <p className="info-item">Admin: False</p>
            <p className="info-item">Location: {user.location}</p>
          </div>
        </div>
      </div>
    )}
  </div>
  );
};

export default UserPage;

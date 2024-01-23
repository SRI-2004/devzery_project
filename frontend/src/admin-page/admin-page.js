// src/AdminPage.js
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './admin-page.css'
const AdminPage = () => {
  const [activeUsers, setActiveUsers] = useState([]);
  const navigate = useNavigate();
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch active users data using the locally stored session token
    const fetchActiveUsers = async () => {
      try {
        // Get the session token from local storage
        const sessionToken = localStorage.getItem('sessionToken');

        // Make a POST request to the API with the session token
        const response = await fetch('http://127.0.0.1:8000/admin_user/get_profiles/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            session_token: sessionToken,
          }),
        });

        if (!response.ok) {
          throw new Error('Failed to fetch active users data');
        }

        // Parse the response and set the active users state
        const activeUsersData = await response.json();
        const user_data = activeUsersData.profiles;
        setActiveUsers(user_data);
      } catch (error) {
        console.error('Error fetching active users data:', error.message);
      }
    };

    fetchActiveUsers();
  }, []); // Empty dependency array ensures the effect runs once on mount
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
      
      const sessionToken = localStorage.getItem('sessionToken');
      const response = await fetch('http://127.0.0.1:8000/user/logout/', {
        method: 'POST',  
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_token: sessionToken,
        }),
      });

      if (response.ok) {
        navigate('/')
        console.log('Logout successful');
      } else {
        console.error('Logout failed');
      }
    } catch (error) {
      console.error('Error during logout:', error.message);
    }
  }
  return (
    <div>
      <div className="header">
        <div className="logo-container">
          <img
        src="https://static.wixstatic.com/media/85c200_6a8d1536dfb74604b5e839845c9795ff~mv2.png/v1/crop/x_4,y_0,w_229,h_62/fill/w_130,h_35,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Group%2031.png"
            alt="Logo"
            className="logo"
          />
        </div>
        <div className="div-7">
          <button className="logout-button" onClick={navigateToLogin}>
            <img
              src="https://cdn.builder.io/api/v1/image/assets/TEMP/ea8f6b4a-9a39-4c28-85ab-3a49dc1ef1e8?"
              alt="Logout"
              className="logout-icon"
            />
            Logout
          </button>
        </div>
      </div>

      <div className="container">
        <div className="dashboard-container">
          <div className="dashboard">
            <h1>Dashboard</h1>
            <div className="active-users">
              <p className="info-item">name: {user?.name}</p>
              <p className="info-item">User ID: {user?.unique_id}</p>
              <p className="info-item">Admin: True</p>
            </div>
          </div>
        </div>
        <div className="login-history-container">
          <div className="login-history">
            <h2>Current Profiles</h2>
            <table className="log-table">
              <thead>
                <tr>
                  <th>User ID</th>
                  <th>Username</th>
                  <th>Profession</th>
                  <th>Email</th>
                  <th>Phone Number</th>
                </tr>
              </thead>
              <tbody>
                {activeUsers.map((user) => (
                  <tr key={user.unique_id}>
                    <td>{user.unique_id}</td>
                    <td>{user.name}</td>
                    <td>{user.profession}</td>
                    <td>{user.email_id}</td>
                    <td>{user.phone_number}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminPage;

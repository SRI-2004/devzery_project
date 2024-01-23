
# DevZery Backend and Frontend

This project consists of a Django-based backend and a React frontend for an authentication system.

## Backend

### Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

### Description

The backend provides authentication and authorization features, including user signup, login, and email verification. It also includes functionality for password reset.

### Features

- User Signup with email verification.
- User Login with session management.
- Password Reset with email-based token verification.
- Get account information
- Get information of all active users through admin access

### Requirements

Make sure you have the following installed:

- Python (version 3.10)
- Django (version 5.0.1)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure database settings:

   Update the `DATABASES` setting in `settings.py` with your database configuration.

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```


### Usage

1. Run the development server:

   ```bash
   python manage.py runserver
   ```

2. Access the API at `http://localhost:8000/`.

3. [Add any other usage instructions]

### API Endpoints

- **Signup:**

  `POST /authorisation/signup/`

- **Login:**

  `POST /authorisation/login/`

- **Forgot Password:**

  `POST /authorisation/forgot_password/`

- **Reset Password:**

  `POST /authorisation/reset_password/`

- **Get Profiles:**
  
  `POST /admin_user/get_profiles/`

- **User Info:**

  `POST /user/user_info/`


## Frontend

### Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

### Introduction

The frontend is a simple React application that interacts with the authentication backend. It allows users to log in, log out, and view their profile information.

### Features

- User login functionality
- User logout functionality
- Display user profile information
- Responsive design

### Prerequisites

Ensure you have the following software installed before running the application:

- Node.js
- npm (Node Package Manager)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-frontend-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-frontend-project
    ```

3. Install dependencies:

    ```bash
    npm install
    ```

### Usage

Run the development server:

```bash
npm start
```

Visit [http://localhost:3000](http://localhost:3000) in your browser to view the application.

### Folder Structure

```
/src
  /login-page
    - login-page.js
    - login-page.css
  /admin-page
    - admin-page.js
    - admin-page.css
  /user-page
    -user-page.js
    -user-page.css
  /signup-page
    -signup-page.js
    -signup-page.css
  App.js
  index.js
/public
  index.html
```
### Contributing

Feel free to contribute by submitting issues or pull requests. Please follow the contribution guidelines.

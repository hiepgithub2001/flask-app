import React from 'react';
import APIservice from '../APIservice';
import Login from './Login';
import Register from './Register';
import { useState } from 'react';
import ArticleModal from '../ArticleService/ArticleModal';

function LoginServiceModal() {
  const [regisMode, setRegisMode] = useState(false);
  const [loginMode, setLoginMode] = useState(false);
  const [loginSuccess, setLoginSuccess] = useState(false);

  const handleLogin = async ({ email, password }) => {
    // Perform login logic here
    console.log('Login:', email, password);
    await APIservice.UserLogin({ email, password })
      .then(data => {
        if (data.status === 'login successfully!') {
          console.log('Login successfully!')
          setLoginSuccess(true);
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const handleRegister = ({ email, password }) => {
    // Perform registration logic here
    console.log('Register:', email, password);
    APIservice.UserRegister({ email, password }).then((data) => {
      if (data.id) {
        setRegisMode(false);
      }
    });
  };

  const handleLogout = async () => {
    // Perform logout logic here
    setLoginSuccess(false);

    // Call APIservice.Logout() here
    await APIservice.Logout().then((data) => {
      if (data.status === 'logout successfully!') {
        setLoginSuccess(false);
        setRegisMode(false);
        setLoginMode(false);
      }
    });
  }

  return (
    <div>
      {!loginSuccess ? (
        <>
          {!(regisMode || loginMode) && (
            <div>
              <h1>Welcome!</h1>
              <button
                style={{ marginRight: '10px' }}
                className="btn btn-primary"
                onClick={() => {
                  setRegisMode(true);
                  setLoginMode(false);
                }}
              >
                Sign Up
              </button>
              <button
                className="btn btn-danger"
                onClick={() => {
                  setLoginMode(true);
                  setRegisMode(false);
                }}
              >
                Sign In
              </button>
            </div>
          )}
          {regisMode && <Register onRegister={handleRegister} />}
          {loginMode && <Login onLogin={handleLogin} />}

          {(regisMode || loginMode) && (
            <button
              style={{ marginTop: '10px' }}
              className="btn btn-secondary"
              onClick={() => {
                setRegisMode(false);
                setLoginMode(false);
              }}
            >
              Back to Home
            </button>
          )}
        </>
      ) : (
        <>
          <ArticleModal />
          <button
            className="btn btn-warning"
            onClick={() => {
              handleLogout();
            }}
          >
            Log Out
          </button>
        </>
      )}
    </div>
  );
}

export default LoginServiceModal;

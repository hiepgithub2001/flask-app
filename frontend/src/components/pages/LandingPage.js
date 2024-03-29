import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import APIservice from '../APIservice';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  const [user, setUser] = useState(null);

  const logoutUser = async () => {
    await APIservice.Logout();
    window.location.href = '/';
  };

  useEffect(() => {
    (async () => {
      try {
        await APIservice.GetCurrentUser().then((resp) => {
          if (resp.id) {
            setUser(resp);
          }
          console.log(resp);
        });
      } catch (error) {
        console.log('Not authenticated');
      }
    })();
  }, []);
  return (
    <div>
      <h1 className="center">Welcome to this React Application</h1>
      <hr></hr>
      {user != null ? (
        <div>
          <Link to="/article" className="btn btn-danger my-3 mx-5">
            Article Service
          </Link>
          <Link to="/chatting" className="btn btn-danger my-3 mx-5">
            Chatting Service
          </Link>
          <h2 className="centerText ">You are Successfully Logged in</h2>
          <h4 className="centerText pt-4">ID: {user.id}</h4>
          <h4 className="centerText pt-4">Email: {user.email}</h4>

          <Button
            className="button123 my-5"
            variant="outline-secondary"
            onClick={logoutUser}
          >
            Logout
          </Button>
        </div>
      ) : (
        <div>
          <h2 className="centerText">
            <h4>
              <strong>You are not logged in</strong>
            </h4>
          </h2>
          <Container>
            <Row className="mt-5">
              <Col md={{ span: 4, offset: 2 }}>
                <a href="/login">
                  {' '}
                  <Button variant="outline-primary">Login</Button>
                </a>
              </Col>
              <Col md={3}>
                <a href="/register">
                  <Button variant="outline-secondary">Register</Button>
                </a>
              </Col>
            </Row>
          </Container>
        </div>
      )}
    </div>
  );
};

export default LandingPage;

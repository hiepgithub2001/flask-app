import React from 'react';
import { useState } from 'react';

function Register(props) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can perform validation here

    // Call onRegister callback with email and password
    props.onRegister({ email, password });
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div style={{ marginTop: '10px' }}>
          <label
            htmlFor="password"
          >Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button
          style={{ marginTop: '10px' }}
          className="btn btn-primary"
          type="submit"
        >Register</button>
      </form>
    </div>
  );
}

export default Register;

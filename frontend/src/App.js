import './App.css';
import {useState, useEffect} from 'react';

function App() {

  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/get', {
      'methods': 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(resp => resp.json())
    .then(resp => console.log(resp.json()))
    .catch(error => console.log(error))
  }, []);

  return (
    <div className="App">
      <h1> Welcome hitran! </h1>
    </div>
  ); 
}

export default App;

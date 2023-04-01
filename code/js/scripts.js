import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/v1/';

axios.get(`${API_URL}Myquize/`)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
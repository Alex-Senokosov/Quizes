const quizTable = document.getElementById('quiz-table');
const quizTableBody = quizTable.getElementsByTagName('tbody')[0];

fetch('http://127.0.0.1:8000/api/v1/Myquize/', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
  }
})
.then(response => response.json())
.then(data => {
  console.log(`User: ${data.user}`);
  data.results.forEach(quiz => {
    const row = quizTableBody.insertRow();
    row.insertCell().appendChild(document.createTextNode(quiz.id));
    row.insertCell().appendChild(document.createTextNode(quiz.title));
    row.insertCell().appendChild(document.createTextNode(quiz.question));
    row.insertCell().appendChild(document.createTextNode(quiz.answer_1));
    row.insertCell().appendChild(document.createTextNode(quiz.answer_2));
    row.insertCell().appendChild(document.createTextNode(quiz.answer_3));
    row.insertCell().appendChild(document.createTextNode(quiz.answer_correct));
  });
})
.catch(error => console.error(error));

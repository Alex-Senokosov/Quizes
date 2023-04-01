const API_URL = 'http://127.0.0.1:8000/api/v1/Myquize/';

axios.get(API_URL)
  .then(response => {
    const quizList = document.getElementById('quiz-list');
    const ul = document.createElement('ul');

    response.data.results.forEach(quiz => {
      const li = document.createElement('li');
      li.innerHTML = `<strong>${quiz.title}</strong>: ${quiz.content}`;
      ul.appendChild(li);
    });

    quizList.innerHTML = '';
    quizList.appendChild(ul);
  })
  .catch(error => {
    console.log(error);
  });

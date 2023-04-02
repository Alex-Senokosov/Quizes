const API_URL = 'http://127.0.0.1:8000/api/v1/Myquize/';

axios.get(API_URL)
  .then(response => {
    const quizList = document.getElementById('quiz-list');
    const ul = document.createElement('ul');

    response.data.results.forEach(quiz => {
      const li = document.createElement('li');
      const link = document.createElement('a');
      link.innerHTML = `<strong>${quiz.title}</strong>: ${quiz.content}`;
      link.setAttribute("onclick", `window.location.href='http://127.0.0.1:8000/api/v1/Myquize/${quiz.id}/?format=json'`);
      li.appendChild(link);
      ul.appendChild(li);
    });

    quizList.innerHTML = '';
    quizList.appendChild(ul);
  })
  .catch(error => {
    console.log(error);
  });



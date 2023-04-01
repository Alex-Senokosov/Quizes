function loadData() {
  const quizesContainer = document.getElementById('quizes');

  fetch('/api/v1/Myquize/')
    .then(response => response.json())
    .then(data => {
      // очистим контейнер перед вставкой данных
      quizesContainer.innerHTML = '';

      // создадим элементы для каждого квиза и добавим их в контейнер
      data.forEach(quiz => {
        const quizDiv = document.createElement('div');
        quizDiv.innerHTML = `<h2>${quiz.title}</h2><p>${quiz.description}</p>`;
        quizesContainer.appendChild(quizDiv);
      });
    })
    .catch(error => console.error(error));
}

window.addEventListener('load', loadData);

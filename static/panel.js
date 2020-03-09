var questions = [
  {
    question: "Who invented the 'C' language?",
    A: "Dennis Ritchie",
    B: "James Gosling",
    C: "Guido van Rossum",
    D: "Brendan Eich",
    answer: "1"
  },
  {
    question: "How many types of heading does an HTML contain?",
    A: "2",
    B: "4",
    C: "6",
    D: "10",
    answer: "3"
  },
  {
    question: "What backend framework was used to build this website?",
    A: "Django",
    B: "Flask",
    C: "Express",
    D: "Ruby on Rails",
    answer: "2"
  }
];

var scoreCount = 0;
var currentQuestion = 0;
var quizContainer = document.getElementById("quiz");
var questionElement = document.getElementById("question");
var optionA = document.getElementById("A");
var optionB = document.getElementById("B");
var optionC = document.getElementById("C");
var optionD = document.getElementById("D");
var next = document.getElementById("next");
var score = document.getElementById("score");
var tryAgain = document.getElementById("tryAgain");

var totalQuestions = questions.length;

function loadQuestion(questionNum) {
  questionElement.textContent = questions[questionNum].question;
  optionA.textContent = questions[questionNum].A;
  optionB.textContent = questions[questionNum].B;
  optionC.textContent = questions[questionNum].C;
  optionD.textContent = questions[questionNum].D;
}

function nextQuestion() {
  var selected = document.querySelector("input[type=radio]:checked");
  var useranswer = selected.value;
  if (useranswer == questions[currentQuestion].answer) {
    scoreCount += 1;
  }
  deactivate();
  selected.checked = false;
  currentQuestion++;
  if (currentQuestion == totalQuestions) {
    quizContainer.style.display = "none";
    next.style.display = "none";
    score.style.display = "";
    tryAgain.style.display = "";
    score.innerHTML = "Your Score <br>" + scoreCount;
    return;
  }
  loadQuestion(currentQuestion);
}

function activate() {
  var resetBtn = document.getElementById("next");
  resetBtn.disabled = false;
}

function deactivate() {
  var resetBtn = document.getElementById("next");
  resetBtn.disabled = true;
}

function resetQuiz() {
  scoreCount = 0;
  currentQuestion = 0;
  quizContainer.style.display = "";
  next.style.display = "";
  score.style.display = "none";
  tryAgain.style.display = "none";
  loadQuestion(currentQuestion);
}

loadQuestion(currentQuestion);

const question = document.getElementById("question");
// Array.from() converts to an array from HTML collection
const choices = Array.from(document.getElementsByClassName("choice-text"));

let currentQuestion = {};
// acceptingAnswers creates a small delay before letting someone answer again
let acceptingAnswers = false;
let score = 0;
let questionCounter = 0;
// will take questions out of the array so there is always a new question to give
let availableQuesions = [];

//each question is an object
let questions = [
    {
        question: 'Inside which HTML element do we put the JavaScript??',
        choice1: '<script>',
        choice2: '<javascript>',
        choice3: '<js>',
        choice4: '<scripting>',
        answer: 1,
    },
    {
        question:
            "What is the correct syntax for referring to an external script called 'xxx.js'?",
        choice1: "<script href='xxx.js'>",
        choice2: "<script name='xxx.js'>",
        choice3: "<script src='xxx.js'>",
        choice4: "<script file='xxx.js'>",
        answer: 3,
    },
    {
        question: " How do you write 'Hello World' in an alert box?",
        choice1: "msgBox('Hello World');",
        choice2: "alertBox('Hello World');",
        choice3: "msg('Hello World');",
        choice4: "alert('Hello World');",
        answer: 4,
    },
];

//Constants
const CORRECT_BONUS = 10;
const MAX_QUESTIONS = 3;

startGame = () => {
    questionCounter = 0;
    score = 0;
     //the spread operation: ... says take the questions array and spread out each of its items into a new array
    // if just set to questions, both variables would point to the same thing. We need a copy so when making changes, one doesnt affect the other
    availableQuesions = [...questions];
    getNewQuestion();
};

getNewQuestion = () => {
    if (availableQuesions.length === 0 || questionCounter >= MAX_QUESTIONS) {
        //what to do if we run out of questions.. go to the end page
        return window.location.assign('/end.html');
    }
    questionCounter++;
    //want a random number. Math.floor takes lower number of float to give integer. 
    const questionIndex = Math.floor(Math.random() * availableQuesions.length);
    currentQuestion = availableQuesions[questionIndex];
    //set html El inner text to the question we just loaded
    question.innerText = currentQuestion.question;

    // for each choice, iterate over each choice
    choices.forEach((choice) => {
        const number = choice.dataset['number'];
        choice.innerText = currentQuestion['choice' + number];
    });

    // get rid of question just used
    availableQuesions.splice(questionIndex, 1);
    acceptingAnswers = true;
};

choices.forEach((choice) => {
    choice.addEventListener('click', (e) => {
        if (!acceptingAnswers) return;

        acceptingAnswers = false;
        const selectedChoice = e.target;
        const selectedAnswer = selectedChoice.dataset['number'];
        getNewQuestion();
    });
});

startGame();
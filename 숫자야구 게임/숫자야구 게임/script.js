let answer = [];
let attempts = 9;
// 게임 끝났는지 아닌지 체크
let gameEnded = false;

function initGame() {
    attempts = 9;
    answer = [];
    // 0~9 중에 겹치지 않게 3개 뽑기 (중복 X)
    while (answer.length < 3) {
        const randomNum = Math.floor(Math.random() * 10);
        if (!answer.includes(randomNum)) { 
            answer.push(randomNum); 
        }
    }
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    // 결과창도 비우기
    document.getElementById('results').innerHTML = '';
    document.getElementById('game-result-img').src = '';
    document.getElementById('game-result-img').style.display = 'none';
    document.getElementById('attempts').textContent = attempts;
    gameEnded = false;
    // 버튼 다시 누를 수 있게 
    document.querySelector('.submit-button').disabled = false;
}

function check_numbers() {
    if (gameEnded) return;
    const num1 = document.getElementById('number1').value;
    const num2 = document.getElementById('number2').value;
    const num3 = document.getElementById('number3').value;
    if (num1 === '' || num2 === '' || num3 === '') {
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        return;
    }
    // 입력값 숫자로 바꿔서 배열에 넣음
    const userInput = [parseInt(num1), parseInt(num2), parseInt(num3)];
    // 스트라이크랑 볼 세는 부분 (위치, 값 비교)
    let strikes = 0, balls = 0;
    for (let i = 0; i < 3; i++) {
        if (userInput[i] === answer[i]) strikes++; // 자리랑 숫자 다 맞으면 스트라이크
        else if (answer.includes(userInput[i])) balls++; // 숫자만 맞으면 볼
    }
    // 결과 어떻게 보여줄지
    let resultText = '';
    if (strikes === 0 && balls === 0) {
        resultText = 'O';
    } else {
        resultText = `${strikes}S ${balls}B`;
    }
    // 결과 계속 밑에 쌓임
    const resultDiv = document.getElementById('results');
    const newResult = document.createElement('div');
    newResult.textContent = `${userInput.join('')} : ${resultText}`;
    resultDiv.appendChild(newResult);
    attempts--;
    document.getElementById('attempts').textContent = attempts;
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    // 게임 끝났는지 체크 (3스트라이크 or 기회 다 씀)
    if (strikes === 3) {
        gameEnded = true;
        document.getElementById('game-result-img').src = 'success.png';
        document.getElementById('game-result-img').style.display = 'block';
        document.querySelector('.submit-button').disabled = true;
    } else if (attempts === 0) {
        gameEnded = true;
        document.getElementById('game-result-img').src = 'fail.png';
        document.getElementById('game-result-img').style.display = 'block';
        document.querySelector('.submit-button').disabled = true;
    }
}

window.onload = function() {
    initGame();
};

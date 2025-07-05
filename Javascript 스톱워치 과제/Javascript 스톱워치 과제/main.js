// 스톱워치 변수
let timer = null;
let elapsed = 0; // ms 단위
let running = false;

// DOM 
const display = document.getElementById('display');
const startBtn = document.getElementById('start');
const stopBtn = document.getElementById('stop');
const resetBtn = document.getElementById('reset');
const recordList = document.getElementById('recordList');
const deleteAllBtn = document.getElementById('deleteAll');
const selectAll = document.getElementById('selectAll');
const deleteSelectedBtn = document.getElementById('deleteSelected');

// 시간 
function formatTime(ms) {
  const totalSec = Math.floor(ms / 10);
  const min = String(Math.floor(totalSec / 6000)).padStart(2, '0');
  const sec = String(Math.floor((totalSec % 6000) / 100)).padStart(2, '0');
  const ms2 = String(totalSec % 100).padStart(2, '0');
  return `${min} : ${sec} : ${ms2}`;
}

// 시간 표시
function updateDisplay() {
  display.textContent = formatTime(elapsed);
}

// 시작
startBtn.onclick = function() {
  if (running) return;
  running = true;
  let last = Date.now();
  timer = setInterval(() => {
    const now = Date.now();
    elapsed += now - last;
    last = now;
    updateDisplay();
  }, 10);
};

// 정지
stopBtn.onclick = function() {
  if (!running) return;
  running = false;
  clearInterval(timer);
  // stop 시 기록 자동 추가
  addRecord(formatTime(elapsed));
};

// 리셋
resetBtn.onclick = function() {
  running = false;
  clearInterval(timer);
  elapsed = 0;
  updateDisplay();
};

// 기록 리스트 추가
display.onclick = function() {
  if (!running) return;
  addRecord(formatTime(elapsed));
};


function addRecord(timeStr) {
  const li = document.createElement('li');
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  li.appendChild(checkbox);
  const span = document.createElement('span');
  span.textContent = timeStr;
  li.appendChild(span);
  recordList.appendChild(li);
}

// 전체 선택 및 해제
selectAll.onchange = function() {
  const checkboxes = recordList.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(cb => cb.checked = selectAll.checked);
};

// 체크박스 변경헸을 때 전체선택 상태도 적용
function updateSelectAllState() {
  const checkboxes = recordList.querySelectorAll('input[type="checkbox"]');
  const checked = recordList.querySelectorAll('input[type="checkbox"]:checked');
  selectAll.checked = checkboxes.length > 0 && checkboxes.length === checked.length;
}


// 선택 삭제
deleteSelectedBtn.onclick = function() {
  const checked = recordList.querySelectorAll('input[type="checkbox"]:checked');
  checked.forEach(cb => cb.parentElement.remove());
};

// 초기화면
updateDisplay(); 
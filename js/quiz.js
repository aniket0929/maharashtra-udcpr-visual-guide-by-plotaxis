/**
 * UDCPR Interactive Quiz Engine
 */

window.initQuiz = function (containerId, questions, lessonId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let userAnswers = {};
  let score = 0;

  function render() {
    let html = `
      <div class="quiz-header">
        <div class="quiz-title">
          <span>📝 Interactive Knowledge Check</span>
        </div>
        <div class="quiz-score-badge" id="${containerId}-score">
          Score: 0 / ${questions.length}
        </div>
      </div>
    `;

    questions.forEach((q, qIdx) => {
      html += `
        <div class="quiz-question" id="${containerId}-q-${qIdx}">
          <div class="quiz-q-text">${qIdx + 1}. ${q.question}</div>
          <div class="quiz-options">
      `;

      q.options.forEach((opt, optIdx) => {
        html += `
          <button type="button" class="quiz-option-btn" data-qid="${qIdx}" data-oid="${optIdx}">
            <span style="font-family:var(--font-mono); opacity:0.6;">[${String.fromCharCode(65 + optIdx)}]</span>
            <span>${opt}</span>
          </button>
        `;
      });

      html += `
          </div>
          <div class="quiz-explanation" id="${containerId}-exp-${qIdx}">
            <strong>💡 Explanation:</strong> ${q.explanation}
          </div>
        </div>
      `;
    });

    container.innerHTML = html;

    // Attach click events
    container.querySelectorAll('.quiz-option-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        const qIdx = parseInt(this.getAttribute('data-qid'));
        const optIdx = parseInt(this.getAttribute('data-oid'));

        if (userAnswers[qIdx] !== undefined) return; // already answered
        userAnswers[qIdx] = optIdx;

        const isCorrect = optIdx === questions[qIdx].correctAnswer;
        const qBlock = document.getElementById(`${containerId}-q-${qIdx}`);
        const expBlock = document.getElementById(`${containerId}-exp-${qIdx}`);

        const allOptBtns = qBlock.querySelectorAll('.quiz-option-btn');
        allOptBtns.forEach((b, idx) => {
          if (idx === questions[qIdx].correctAnswer) {
            b.classList.add('selected-correct');
          } else if (idx === optIdx && !isCorrect) {
            b.classList.add('selected-wrong');
          }
        });

        expBlock.classList.add('show');

        // Recalculate score
        score = 0;
        Object.keys(userAnswers).forEach(k => {
          if (userAnswers[k] === questions[k].correctAnswer) score++;
        });

        const scoreBadge = document.getElementById(`${containerId}-score`);
        if (scoreBadge) {
          scoreBadge.textContent = `Score: ${score} / ${questions.length}`;
        }

        // Check if finished
        if (Object.keys(userAnswers).length === questions.length) {
          if (window.LearnerProgress && lessonId) {
            window.LearnerProgress.recordQuizScore(lessonId, score, questions.length);
            if (score >= Math.ceil(questions.length * 0.75)) {
              window.LearnerProgress.markLessonComplete(lessonId);
            }
          }
        }
      });
    });
  }

  render();
};

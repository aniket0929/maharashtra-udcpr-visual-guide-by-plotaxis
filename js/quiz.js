/**
 * UDCPR Interactive Quiz & Lesson Completion Engine
 */

window.initQuiz = function (containerId, questions, lessonId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  let userAnswers = {};
  let score = 0;

  // 1. Completion Block Setup
  let completionBlock = document.getElementById('completion-block');
  if (!completionBlock) {
    // If not statically present, create dynamically right after the quiz section
    completionBlock = document.createElement('div');
    completionBlock.id = 'completion-block';
    completionBlock.className = 'lesson-completion-card';
    completionBlock.innerHTML = `
      <div class="lesson-completion-info">
        <span class="kicker-muted">LESSON PROGRESSION</span>
        <div class="lesson-completion-title" id="completion-title">Lesson In Progress</div>
        <div class="lesson-completion-subtitle" id="completion-sub">
          Click to mark this lesson complete, or score &ge; 75% on the verification quiz to complete automatically.
        </div>
      </div>
      <button type="button" class="btn-mark-complete" id="btn-mark-complete">
        <span class="btn-icon" id="btn-completion-icon">○</span>
        <span class="btn-text" id="btn-completion-text">Mark as Completed</span>
      </button>
    `;
    const quizSection = container.closest('section') || container;
    quizSection.parentNode.insertBefore(completionBlock, quizSection.nextSibling);
  }

  const btnMarkComplete = document.getElementById('btn-mark-complete');
  const btnCompletionIcon = document.getElementById('btn-completion-icon');
  const btnCompletionText = document.getElementById('btn-completion-text');
  const completionTitle = document.getElementById('completion-title');
  const completionSub = document.getElementById('completion-sub');

  function syncCompletionUI() {
    if (!window.LearnerProgress || !lessonId) return;
    const isDone = window.LearnerProgress.isLessonComplete(lessonId);

    if (completionBlock) {
      if (isDone) {
        completionBlock.classList.add('completed');
      } else {
        completionBlock.classList.remove('completed');
      }
    }

    if (btnMarkComplete) {
      if (isDone) {
        btnMarkComplete.classList.add('completed');
      } else {
        btnMarkComplete.classList.remove('completed');
      }
    }

    if (btnCompletionIcon) {
      btnCompletionIcon.textContent = isDone ? '✓' : '○';
    }

    if (btnCompletionText) {
      btnCompletionText.textContent = isDone ? 'Lesson Completed' : 'Mark as Completed';
    }

    if (completionTitle) {
      completionTitle.textContent = isDone ? '✓ Lesson Completed' : 'Lesson In Progress';
    }

    if (completionSub) {
      if (isDone) {
        completionSub.textContent = 'Saved to your curriculum progress tracker. Click again if you wish to reset.';
      } else {
        completionSub.textContent = 'Click to mark this lesson complete, or score \u2265 75% on the verification quiz to complete automatically.';
      }
    }
  }

  if (btnMarkComplete) {
    btnMarkComplete.onclick = function () {
      if (window.LearnerProgress && lessonId) {
        window.LearnerProgress.toggleLessonComplete(lessonId);
        syncCompletionUI();
      }
    };
  }

  // Initial completion check
  syncCompletionUI();

  // 2. Render Quiz
  function render() {
    // Check if previously taken
    let prevBadge = `Score: 0 / ${questions.length}`;
    let showRetakeOnStart = false;
    if (window.LearnerProgress && lessonId) {
      const prog = window.LearnerProgress.get();
      if (prog.quizScores && prog.quizScores[lessonId]) {
        const prev = prog.quizScores[lessonId];
        prevBadge = `Previous Score: ${prev.score} / ${prev.total}`;
        showRetakeOnStart = true;
      }
    }

    let html = `
      <div class="quiz-header" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
        <div class="quiz-title">
          <span>📝 Interactive Knowledge Check</span>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="quiz-score-badge" id="${containerId}-score">
            ${prevBadge}
          </div>
          <button type="button" class="btn-retake-quiz" id="${containerId}-retake-btn" style="display:${showRetakeOnStart ? 'inline-flex' : 'none'};">
            ↻ Retake Quiz
          </button>
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

    // Attach retake click
    const retakeBtn = document.getElementById(`${containerId}-retake-btn`);
    if (retakeBtn) {
      retakeBtn.addEventListener('click', function () {
        userAnswers = {};
        score = 0;
        render();
      });
    }

    // Attach option click events
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
          if (retakeBtn) {
            retakeBtn.style.display = 'inline-flex';
          }
          if (window.LearnerProgress && lessonId) {
            window.LearnerProgress.recordQuizScore(lessonId, score, questions.length);
            if (score >= Math.ceil(questions.length * 0.75)) {
              window.LearnerProgress.markLessonComplete(lessonId);
              syncCompletionUI();
            }
          }
        }
      });
    });
  }

  render();
};

/**
 * UDCPR From Scratch - Global App Logic & Progress Tracking
 */

(function () {
  'use strict';

  // 1. Theme Management (Dark / Light)
  const THEME_KEY = 'udcpr_theme';
  const savedTheme = localStorage.getItem(THEME_KEY) || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);

  window.toggleTheme = function () {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem(THEME_KEY, next);
  };

  // 2. Learner Progress Tracker (localStorage)
  const PROGRESS_KEY = 'udcpr_learner_progress';

  window.LearnerProgress = {
    get: function () {
      try {
        return JSON.parse(localStorage.getItem(PROGRESS_KEY)) || {
          completedLessons: [],
          quizScores: {},
          bookmarks: []
        };
      } catch (e) {
        return { completedLessons: [], quizScores: {}, bookmarks: [] };
      }
    },
    save: function (data) {
      localStorage.setItem(PROGRESS_KEY, JSON.stringify(data));
      this.updateUI();
    },
    markLessonComplete: function (lessonId) {
      const data = this.get();
      if (!data.completedLessons.includes(lessonId)) {
        data.completedLessons.push(lessonId);
        this.save(data);
      }
    },
    recordQuizScore: function (lessonId, score, total) {
      const data = this.get();
      data.quizScores[lessonId] = { score, total, date: new Date().toISOString() };
      this.save(data);
    },
    updateUI: function () {
      const data = this.get();
      const countEl = document.getElementById('completed-lessons-count');
      if (countEl) {
        countEl.textContent = data.completedLessons.length;
      }
      const progressPercentEl = document.getElementById('total-progress-percent');
      if (progressPercentEl) {
        // Total active core lessons = 47 (Ch 1: 4, Ch 2: 5, Ch 3: 6, Ch 4: 6, Ch 5: 5, Ch 6: 6, Ch 7: 6, Ch 8: 4, Ch 9: 5)
        const pct = Math.min(100, Math.round((data.completedLessons.length / 47) * 100));
        progressPercentEl.textContent = pct + '%';
      }
    }
  };

  document.addEventListener('DOMContentLoaded', function () {
    LearnerProgress.updateUI();
  });
})();

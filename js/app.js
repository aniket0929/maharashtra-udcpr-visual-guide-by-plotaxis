/**
 * UDCPR Visual Guide - Global App Logic & Progress Tracking
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
    unmarkLessonComplete: function (lessonId) {
      const data = this.get();
      const idx = data.completedLessons.indexOf(lessonId);
      if (idx > -1) {
        data.completedLessons.splice(idx, 1);
        this.save(data);
      }
    },
    isLessonComplete: function (lessonId) {
      const data = this.get();
      return Array.isArray(data.completedLessons) && data.completedLessons.includes(lessonId);
    },
    toggleLessonComplete: function (lessonId) {
      if (this.isLessonComplete(lessonId)) {
        this.unmarkLessonComplete(lessonId);
        return false;
      } else {
        this.markLessonComplete(lessonId);
        return true;
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
        // Total active core lessons = 76 (Ch 1: 4, Ch 2: 5, Ch 3: 6, Ch 4: 6, Ch 5: 5, Ch 6: 6, Ch 7: 6, Ch 8: 4, Ch 9: 5, Ch 10: 7, Ch 11: 4, Ch 12: 4, Ch 13: 4, Ch 14: 7, Ch 15: 3)
        const pct = Math.min(100, Math.round((data.completedLessons.length / 76) * 100));
        progressPercentEl.textContent = pct + '%';
      }
    }
  };

  // 3. Mobile Hamburger Navigation
  function initMobileMenu() {
    const navTools = document.querySelector('.sheet-nav .nav-tools');
    const navMenu = document.querySelector('.sheet-nav .nav-menu');
    if (!navTools || !navMenu) return;

    if (!document.getElementById('mobile-menu-btn')) {
      const btn = document.createElement('button');
      btn.id = 'mobile-menu-btn';
      btn.className = 'menu-toggle-btn tool-btn';
      btn.type = 'button';
      btn.setAttribute('aria-label', 'Toggle navigation menu');
      btn.setAttribute('aria-expanded', 'false');
      btn.innerHTML = `
        <span class="hamburger-bars" aria-hidden="true">
          <span></span><span></span><span></span>
        </span>
        <span class="menu-btn-text">MENU</span>
      `;

      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        const isOpen = navMenu.classList.toggle('mobile-open');
        btn.classList.toggle('open', isOpen);
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });

      // Close menu when clicking outside
      document.addEventListener('click', function (e) {
        if (!navMenu.contains(e.target) && !btn.contains(e.target)) {
          navMenu.classList.remove('mobile-open');
          btn.classList.remove('open');
          btn.setAttribute('aria-expanded', 'false');
        }
      });

      // Close menu on ESC key
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && navMenu.classList.contains('mobile-open')) {
          navMenu.classList.remove('mobile-open');
          btn.classList.remove('open');
          btn.setAttribute('aria-expanded', 'false');
        }
      });

      // Close menu when clicking any nav link
      navMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function () {
          navMenu.classList.remove('mobile-open');
          btn.classList.remove('open');
          btn.setAttribute('aria-expanded', 'false');
        });
      });

      navTools.appendChild(btn);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    LearnerProgress.updateUI();
    initMobileMenu();
  });
})();

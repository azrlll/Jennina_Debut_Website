/**
 * Jennina's 18th Birthday Debut Royal Invitation
 * Theme: Royal Emerald Green, Gold & Cream — Enchanted Garden
 * Subtitle: "A Decade and Eight"
 * Phase 1: Interactive Royal Opening & Revealed Golden Framed Invitation
 */

(function () {
  'use strict';

  // DOM Elements
  const body = document.body;
  const scrollTrigger = document.getElementById('scrollTrigger');
  const openingScene = document.getElementById('openingScene');
  const revealedScene = document.getElementById('revealedScene');
  const btnReplay = document.getElementById('btnReplay');
  const srAnnounce = document.getElementById('srAnnounce');
  const sparkleCanvas = document.getElementById('sparkleCanvas');

  // Check user motion preference
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // State
  let isOpening = false;
  let isOpen = false;

  /**
   * Screen reader announcer
   */
  function announce(message) {
    if (srAnnounce) {
      srAnnounce.textContent = '';
      setTimeout(() => {
        srAnnounce.textContent = message;
      }, 50);
    }
  }

  /**
   * Trigger Royal Scroll Opening
   */
  function openInvitation() {
    if (isOpening || isOpen) return;
    isOpening = true;

    // Accessibility
    scrollTrigger.setAttribute('aria-expanded', 'true');
    announce("Opening Jennina's royal invitation...");

    // Get seal position for sparkling burst
    const sealElem = scrollTrigger.querySelector('.wax-seal');
    if (sealElem && particleSystem) {
      const rect = sealElem.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;
      particleSystem.createBurst(x, y, 45);
    }

    if (prefersReducedMotion) {
      // Instant switch for reduced motion
      body.classList.add('invitation-open');
      openingScene.setAttribute('aria-hidden', 'true');
      revealedScene.setAttribute('aria-hidden', 'false');
      isOpen = true;
      isOpening = false;
      announce("Jennina's 18th Birthday invitation is now displayed.");
      btnReplay.focus();
      return;
    }

    // Step 1: Start unrolling and curtain parting
    body.classList.add('scroll-opening');

    // Step 2: Complete unroll and reveal the golden framed card
    setTimeout(() => {
      body.classList.remove('scroll-opening');
      body.classList.add('invitation-open');
      openingScene.setAttribute('aria-hidden', 'true');
      revealedScene.setAttribute('aria-hidden', 'false');
      isOpen = true;
      isOpening = false;

      // Focus replay button for keyboard flow
      if (btnReplay) {
        btnReplay.focus();
      }

      announce("Jennina's 18th Birthday invitation revealed inside a golden baroque frame.");
    }, 900);
  }

  /**
   * Replay / Close Scroll Interaction
   */
  function closeInvitation() {
    if (isOpening || !isOpen) return;

    if (prefersReducedMotion) {
      body.classList.remove('invitation-open');
      openingScene.setAttribute('aria-hidden', 'false');
      revealedScene.setAttribute('aria-hidden', 'true');
      scrollTrigger.setAttribute('aria-expanded', 'false');
      isOpen = false;
      scrollTrigger.focus();
      announce("Invitation scroll closed. Ready to open again.");
      return;
    }

    // Fade out revealed scene smoothly
    revealedScene.style.opacity = '0';
    revealedScene.style.transform = 'scale(0.92)';

    setTimeout(() => {
      body.classList.remove('invitation-open');
      revealedScene.style.opacity = '';
      revealedScene.style.transform = '';
      openingScene.setAttribute('aria-hidden', 'false');
      revealedScene.setAttribute('aria-hidden', 'true');
      scrollTrigger.setAttribute('aria-expanded', 'false');
      isOpen = false;

      // Reset scroll trigger focus
      scrollTrigger.focus();
      announce("Invitation scroll closed. Ready to open again.");
    }, 400);
  }

  /* ------------------------------------------------------------------------
     EVENT LISTENERS (Keyboard & Mouse / Touch)
     ------------------------------------------------------------------------ */
  // Click / Tap on Scroll
  scrollTrigger.addEventListener('click', (e) => {
    e.preventDefault();
    openInvitation();
  });

  // Keyboard accessibility: Enter or Space triggers scroll open
  scrollTrigger.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      openInvitation();
    }
  });

  // Replay Button Click
  if (btnReplay) {
    btnReplay.addEventListener('click', (e) => {
      e.preventDefault();
      closeInvitation();
    });

    btnReplay.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        closeInvitation();
      }
    });
  }

  /* ------------------------------------------------------------------------
     LIGHTWEIGHT GOLD PARTICLES & ENCHANTED FIREFLIES SYSTEM
     ------------------------------------------------------------------------ */
  class ParticleSystem {
    constructor(canvas) {
      this.canvas = canvas;
      this.ctx = canvas.getContext('2d');
      this.particles = [];
      this.burstParticles = [];
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      this.animationId = null;
      this.maxParticles = window.innerWidth < 768 ? 35 : 65;

      this.init();
    }

    init() {
      this.resize();
      window.addEventListener('resize', () => this.resize(), { passive: true });

      // Create ambient floating gold dust & fireflies
      for (let i = 0; i < this.maxParticles; i++) {
        this.particles.push(this.createParticle(true));
      }

      this.start();
    }

    resize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      this.canvas.width = this.width * dpr;
      this.canvas.height = this.height * dpr;
      this.ctx.scale(dpr, dpr);
    }

    createParticle(randomY = false) {
      const isFirefly = Math.random() < 0.25;
      return {
        x: Math.random() * this.width,
        y: randomY ? Math.random() * this.height : this.height + 10,
        radius: isFirefly ? Math.random() * 2.2 + 1.2 : Math.random() * 1.5 + 0.6,
        color: isFirefly ? '#FFE899' : (Math.random() > 0.4 ? '#D4AF37' : '#F8F1DF'),
        speedY: -(Math.random() * 0.45 + 0.15),
        speedX: (Math.random() - 0.5) * 0.35,
        alpha: Math.random() * 0.6 + 0.2,
        alphaSpeed: (Math.random() * 0.015 + 0.005) * (Math.random() > 0.5 ? 1 : -1),
        maxAlpha: isFirefly ? 0.85 : 0.65,
        minAlpha: 0.1,
        wobble: Math.random() * Math.PI * 2,
        wobbleSpeed: Math.random() * 0.02 + 0.01,
        isFirefly: isFirefly
      };
    }

    createBurst(originX, originY, count = 40) {
      if (prefersReducedMotion) return;
      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 5.5 + 1.5;
        this.burstParticles.push({
          x: originX,
          y: originY,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 1.2,
          radius: Math.random() * 2.8 + 1,
          color: Math.random() > 0.3 ? '#FFF2C6' : '#D4AF37',
          alpha: 1,
          decay: Math.random() * 0.025 + 0.015,
          gravity: 0.08
        });
      }
    }

    start() {
      if (prefersReducedMotion) return;

      const animate = () => {
        this.update();
        this.draw();
        this.animationId = requestAnimationFrame(animate);
      };
      this.animationId = requestAnimationFrame(animate);
    }

    stop() {
      if (this.animationId) {
        cancelAnimationFrame(this.animationId);
        this.animationId = null;
      }
    }

    update() {
      // Update ambient particles
      for (let i = 0; i < this.particles.length; i++) {
        const p = this.particles[i];
        p.wobble += p.wobbleSpeed;
        p.x += p.speedX + Math.sin(p.wobble) * 0.35;
        p.y += p.speedY;

        p.alpha += p.alphaSpeed;
        if (p.alpha > p.maxAlpha || p.alpha < p.minAlpha) {
          p.alphaSpeed = -p.alphaSpeed;
        }

        // Reset when out of top or bounds
        if (p.y < -15 || p.x < -20 || p.x > this.width + 20) {
          this.particles[i] = this.createParticle(false);
        }
      }

      // Update burst particles
      for (let i = this.burstParticles.length - 1; i >= 0; i--) {
        const bp = this.burstParticles[i];
        bp.x += bp.vx;
        bp.y += bp.vy;
        bp.vy += bp.gravity;
        bp.vx *= 0.98;
        bp.alpha -= bp.decay;

        if (bp.alpha <= 0) {
          this.burstParticles.splice(i, 1);
        }
      }
    }

    draw() {
      this.ctx.clearRect(0, 0, this.width, this.height);

      // Draw ambient particles
      for (let i = 0; i < this.particles.length; i++) {
        const p = this.particles[i];
        this.ctx.save();
        this.ctx.globalAlpha = Math.max(0, Math.min(1, p.alpha));
        this.ctx.fillStyle = p.color;

        if (p.isFirefly) {
          this.ctx.shadowBlur = 8;
          this.ctx.shadowColor = 'rgba(255, 230, 150, 0.8)';
        }

        this.ctx.beginPath();
        this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();
      }

      // Draw burst particles
      for (let i = 0; i < this.burstParticles.length; i++) {
        const bp = this.burstParticles[i];
        this.ctx.save();
        this.ctx.globalAlpha = Math.max(0, bp.alpha);
        this.ctx.fillStyle = bp.color;
        this.ctx.shadowBlur = 10;
        this.ctx.shadowColor = 'rgba(212, 175, 55, 0.9)';
        this.ctx.beginPath();
        this.ctx.arc(bp.x, bp.y, bp.radius, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();
      }
    }
  }

  // Initialize particle system if canvas exists
  let particleSystem = null;
  if (sparkleCanvas && !prefersReducedMotion) {
    particleSystem = new ParticleSystem(sparkleCanvas);
  }

  // Pause particles when tab is hidden to conserve performance
  document.addEventListener('visibilitychange', () => {
    if (particleSystem) {
      if (document.hidden) {
        particleSystem.stop();
      } else {
        particleSystem.start();
      }
    }
  });

  /* ------------------------------------------------------------------------
     PHASE 2: LIVE ROYAL COUNTDOWN TIMER
     Target: February 5, 2027 at 3:00 PM Asia/Manila (UTC+08:00)
     ------------------------------------------------------------------------ */
  const countDays = document.getElementById('countDays');
  const countHours = document.getElementById('countHours');
  const countMinutes = document.getElementById('countMinutes');
  const countSeconds = document.getElementById('countSeconds');
  const countdownGrid = document.getElementById('countdownGrid');
  const countdownArrived = document.getElementById('countdownArrived');

  // Exact target timestamp: February 5, 2027 at 3:00 PM Asia/Manila (UTC+08:00)
  const TARGET_DATE = new Date('2027-02-05T15:00:00+08:00').getTime();

  function updateDigit(element, newValue) {
    if (!element) return;
    const formatted = String(newValue).padStart(2, '0');
    if (element.textContent !== formatted) {
      element.textContent = formatted;
      if (!prefersReducedMotion) {
        element.classList.remove('digit-tick');
        void element.offsetWidth; // Trigger reflow for smooth transition
        element.classList.add('digit-tick');
      }
    }
  }

  function updateCountdown() {
    const now = Date.now();
    const distance = TARGET_DATE - now;

    // Do not show negative countdown values
    if (distance <= 0) {
      if (countDays) countDays.textContent = '00';
      if (countHours) countHours.textContent = '00';
      if (countMinutes) countMinutes.textContent = '00';
      if (countSeconds) countSeconds.textContent = '00';

      if (countdownGrid) countdownGrid.style.display = 'none';
      if (countdownArrived) countdownArrived.style.display = 'flex';
      return;
    }

    const msInSecond = 1000;
    const msInMinute = msInSecond * 60;
    const msInHour = msInMinute * 60;
    const msInDay = msInHour * 24;

    const days = Math.floor(distance / msInDay);
    const hours = Math.floor((distance % msInDay) / msInHour);
    const minutes = Math.floor((distance % msInHour) / msInMinute);
    const seconds = Math.floor((distance % msInMinute) / msInSecond);

    updateDigit(countDays, days);
    updateDigit(countHours, hours);
    updateDigit(countMinutes, minutes);
    updateDigit(countSeconds, seconds);
  }

  // Initial immediate calculation & 1-second interval loop
  updateCountdown();
  setInterval(updateCountdown, 1000);

  /* ------------------------------------------------------------------------
     PHASE 3: 18 TRADITIONS PROGRAM DATA & DYNAMIC RENDERING
     Sections:
       - 18 Roses + 18 Candles & Gifts (Reference: Page 2 of PDF)
       - 18 Blue Bills + 18 Shots (Reference: Page 3 of PDF)
     ------------------------------------------------------------------------ */
  const TRADITIONS_REGISTRY = {
    roses: {
      id: 'roses',
      containerId: 'listRoses',
      title: '18 Roses',
      tagline: 'The First Dance & Guiding Gentlemen',
      names: [
        'Jielun Martija',
        'Ralph Chandler',
        'Kurt Uy',
        'Kody Uy',
        'Kevin Real',
        'Karl Real',
        'Giovanni Mendoza',
        'Kimpee Sta. Rufina',
        'Angelo Torqueza',
        'Jemil Alegre',
        'Alexander Hadloc',
        'Ahmir Caballero',
        'Prince Cruz',
        'Rasheed Sobrepeña',
        'Emmanuel Espiritu',
        'Michael Uy',
        'Roland Berango',
        'Hanz Chandler'
      ]
    },
    candles: {
      id: 'candles',
      containerId: 'listCandles',
      title: '18 Candles & Gifts',
      tagline: 'The Guiding Lights & Warm Wishes',
      names: [
        'Lesly Piñonal',
        'Katrine De Luna',
        'Jerlen Buenzalida',
        'Jeremy Isipin',
        'Lerizel Martos',
        'Mae Castillejos',
        'Jessica De Jesus',
        'Amber Castillano',
        'Amber Timbang',
        'Earl Ricofuerto',
        'Aeyesha Ygrubay',
        'Franzchesca Ramiscal',
        'Kashmire Clemente',
        'Regine Magallanes',
        'Josie Caoile',
        'Ma. Shaina Uy',
        'Queenie May Uy',
        'Jane Chandler'
      ]
    },
    blueBills: {
      id: 'blueBills',
      containerId: 'listBlueBills',
      title: '18 Blue Bills',
      tagline: 'Prosperity & Future Horizons',
      names: [
        'Maria Luz Avinado',
        'Khaye Prodigo',
        'Regen Sansolis',
        'Zara Sangalan',
        'Janine Retoma',
        'Wilynne Sual',
        'Raymund Nava',
        'Armina Buendicho',
        'Ronnie Cabanting',
        'Andrea Gonzales',
        'Christ Marie Lagat',
        'Susette Amora',
        'Eden Boiser',
        'Gessa Dellomas',
        'Maricel Tangalin',
        'Rose Marie Uy',
        'Rosanna Real',
        'Influcella Berango'
      ]
    },
    shots: {
      id: 'shots',
      containerId: 'listShots',
      title: '18 Shots',
      tagline: 'Celebratory Cheers & Lasting Bonds',
      names: [
        'Katrine De Luna',
        'Alexander Hadloc',
        'Jerlen Buenzalida',
        'Franzchesca Ramiscal',
        'Kashmire Clemente',
        'Rasheed Sobrepeña',
        'Jeremy Isipin',
        'Mae Castillejos',
        'Amber Timbang',
        'Ralph Chandler',
        'Angelo Torqueza',
        'Kimpee Sta. Rufina',
        'Maria Luz Avinado',
        'Rico Romero',
        'Wilynn Sual',
        'Kody Uy',
        'Karl Real',
        'Queenie May Uy'
      ]
    }
  };

  /**
   * Validate that all traditions contain exactly 18 honorees
   */
  function validateTraditionsRegistry(registry) {
    let allValid = true;
    for (const [key, item] of Object.entries(registry)) {
      const count = Array.isArray(item.names) ? item.names.length : 0;
      if (count !== 18) {
        console.error(`[VALIDATION ERROR] ${item.title} contains ${count} names; expected exactly 18.`);
        allValid = false;
      } else {
        console.log(`[PASS] Validated ${item.title}: exactly 18 honorees confirmed.`);
      }
    }
    return allValid;
  }

  /**
   * Dynamically populate the 4 program lists into the DOM
   */
  function populateTraditionLists() {
    validateTraditionsRegistry(TRADITIONS_REGISTRY);

    for (const [key, item] of Object.entries(TRADITIONS_REGISTRY)) {
      const listElement = document.getElementById(item.containerId);
      if (!listElement) continue;

      listElement.innerHTML = '';
      const fragment = document.createDocumentFragment();

      item.names.forEach((name, index) => {
        const li = document.createElement('li');
        li.className = 'entourage-item';

        const indexBadge = document.createElement('span');
        indexBadge.className = 'entourage-index';
        indexBadge.textContent = String(index + 1).padStart(2, '0');
        indexBadge.setAttribute('aria-hidden', 'true');

        const nameSpan = document.createElement('span');
        nameSpan.className = 'entourage-name';
        nameSpan.textContent = name;

        li.appendChild(indexBadge);
        li.appendChild(nameSpan);
        fragment.appendChild(li);
      });

      listElement.appendChild(fragment);
    }
  }

  /**
   * Accessible Tab Switching for Mobile Viewports
   */
  function initMobileTraditionTabs() {
    const tabConfigs = [
      {
        tabs: ['tabRoses', 'tabCandles'],
        panels: ['panelRoses', 'panelCandles']
      },
      {
        tabs: ['tabBlueBills', 'tabShots'],
        panels: ['panelBlueBills', 'panelShots']
      }
    ];

    tabConfigs.forEach(config => {
      const tabElements = config.tabs.map(id => document.getElementById(id)).filter(Boolean);
      const panelElements = config.panels.map(id => document.getElementById(id)).filter(Boolean);

      tabElements.forEach((tabBtn, index) => {
        function activateTab() {
          tabElements.forEach((btn, i) => {
            const isActive = i === index;
            btn.classList.toggle('active', isActive);
            btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
            btn.setAttribute('tabindex', isActive ? '0' : '-1');
          });

          panelElements.forEach((panel, i) => {
            const isActive = i === index;
            panel.classList.toggle('panel-active', isActive);
            if (window.innerWidth < 768) {
              panel.setAttribute('aria-hidden', isActive ? 'false' : 'true');
            }
          });
        }

        tabBtn.addEventListener('click', activateTab);

        tabBtn.addEventListener('keydown', (e) => {
          let targetIndex = null;
          if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
            targetIndex = (index + 1) % tabElements.length;
          } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            targetIndex = (index - 1 + tabElements.length) % tabElements.length;
          } else if (e.key === 'Home') {
            targetIndex = 0;
          } else if (e.key === 'End') {
            targetIndex = tabElements.length - 1;
          }

          if (targetIndex !== null) {
            e.preventDefault();
            tabElements[targetIndex].focus();
            tabElements[targetIndex].click();
          }
        });
      });
    });

    // Handle screen resize to reset aria-hidden on desktop
    function handleResize() {
      const isDesktop = window.innerWidth >= 768;
      ['panelRoses', 'panelCandles', 'panelBlueBills', 'panelShots'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          if (isDesktop) {
            el.removeAttribute('aria-hidden');
          } else {
            el.setAttribute('aria-hidden', el.classList.contains('panel-active') ? 'false' : 'true');
          }
        }
      });
    }

    window.addEventListener('resize', handleResize);
    handleResize();
  }

  /* ------------------------------------------------------------------------
     PHASE 4: ROYAL ATTIRE, COLOR PALETTES & GALLERIES CONFIGURATION
     Sections:
       - Royal Attire (18th Roses + Guests) (Pages 4 & 5 of PDF)
       - Gift Guide (Page 5 of PDF)
       - Important Reminders (Page 6 of PDF)
     ------------------------------------------------------------------------ */
  const ATTIRE_CONFIG = {
    roses: {
      id: 'roses',
      swatchesContainerId: 'swatchesRoses',
      galleryContainerId: 'galleryRoses',
      title: 'For the 18th Roses',
      role: "Formal Men's Royal Attire Inspiration",
      colors: [
        { name: 'Navy Blue', hex: '#142247', isLight: false },
        { name: 'Black', hex: '#010101', isLight: false },
        { name: 'White (Inner)', hex: '#FDFDFD', isLight: true, note: 'Inner Shirt' },
        { name: 'Brown', hex: '#4A2711', isLight: false },
        { name: 'Dark Grey', hex: '#6C6D72', isLight: false }
      ],
      outfits: [
        { src: 'assets/attire/attire-men-1.png', alt: "Men's Formal Royal Tuxedo Inspiration 1" },
        { src: 'assets/attire/attire-men-2.png', alt: "Men's Formal Royal Tuxedo Inspiration 2" },
        { src: 'assets/attire/attire-men-3.png', alt: "Men's Formal Royal Tuxedo Inspiration 3" },
        { src: 'assets/attire/attire-men-4.png', alt: "Men's Formal Royal Tuxedo Inspiration 4" },
        { src: 'assets/attire/attire-men-5.png', alt: "Men's Formal Royal Tuxedo Inspiration 5" }
      ]
    },
    guests: {
      id: 'guests',
      swatchesContainerId: 'swatchesGuests',
      galleryContainerId: 'galleryGuests',
      title: 'For the Guests',
      role: "Women's Elegant Modern Royal Formalwear & Gowns",
      // Configurable palette: allows toggling colors or adding new ones
      colors: [
        { name: 'Ivory', hex: '#FFF5DC', isLight: true, enabled: true },
        { name: 'Khaki', hex: '#C6B69C', isLight: true, enabled: true },
        { name: 'Plum', hex: '#58233E', isLight: false, enabled: true },
        { name: 'Brown', hex: '#361F11', isLight: false, enabled: true },
        { name: 'Rust', hex: '#BE4B0C', isLight: false, enabled: true },
        // Mustard Yellow included from PDF reference; configurable via enabled flag
        { name: 'Mustard Yellow', hex: '#E3AF01', isLight: false, enabled: true, note: 'PDF Reference Palette' }
      ],
      outfits: [
        { src: 'assets/attire/attire-women-1.png', alt: "Women's Royal Formal Gown Inspiration 1" },
        { src: 'assets/attire/attire-women-2.png', alt: "Women's Royal Formal Gown Inspiration 2" },
        { src: 'assets/attire/attire-women-3.png', alt: "Women's Royal Formal Gown Inspiration 3" },
        { src: 'assets/attire/attire-women-4.png', alt: "Women's Royal Formal Gown Inspiration 4" },
        { src: 'assets/attire/attire-women-5.png', alt: "Women's Royal Formal Gown Inspiration 5" },
        { src: 'assets/attire/attire-women-6.png', alt: "Women's Royal Formal Gown Inspiration 6" }
      ]
    }
  };

  /**
   * Dynamically Populate Royal Attire Swatches & Gallery Cards
   */
  function populateAttireSection() {
    for (const [key, config] of Object.entries(ATTIRE_CONFIG)) {
      // 1. Populate Swatches
      const swatchesBox = document.getElementById(config.swatchesContainerId);
      if (swatchesBox) {
        swatchesBox.innerHTML = '';
        const swatchesFrag = document.createDocumentFragment();

        config.colors.forEach(col => {
          if (col.enabled !== false) {
            const swatchEl = document.createElement('div');
            swatchEl.className = 'color-swatch-item';
            swatchEl.setAttribute('role', 'listitem');
            swatchEl.setAttribute('title', `${col.name} (${col.hex})`);
            swatchEl.setAttribute('tabindex', '0');

            const circle = document.createElement('span');
            circle.className = 'swatch-color-circle';
            circle.style.backgroundColor = col.hex;
            if (col.isLight) {
              circle.classList.add('swatch-light');
            }

            const label = document.createElement('span');
            label.className = 'swatch-color-name';
            label.textContent = col.name;

            swatchEl.appendChild(circle);
            swatchEl.appendChild(label);
            swatchesFrag.appendChild(swatchEl);
          }
        });

        swatchesBox.appendChild(swatchesFrag);
      }

      // 2. Populate Outfits Gallery
      const galleryBox = document.getElementById(config.galleryContainerId);
      if (galleryBox) {
        galleryBox.innerHTML = '';
        const galleryFrag = document.createDocumentFragment();

        config.outfits.forEach(outfit => {
          const cardEl = document.createElement('div');
          cardEl.className = 'attire-photo-card';

          const frameEl = document.createElement('div');
          frameEl.className = 'photo-frame-inner';

          const imgEl = document.createElement('img');
          imgEl.src = outfit.src;
          imgEl.alt = outfit.alt;
          imgEl.className = 'attire-outfit-img';
          imgEl.loading = 'eager';

          frameEl.appendChild(imgEl);
          cardEl.appendChild(frameEl);
          galleryFrag.appendChild(cardEl);
        });

        galleryBox.appendChild(galleryFrag);
      }
    }
  }

  /**
   * Unified Viewport Intersection Observer for all Luxury Sections
   */
  function initSectionObserver() {
    const animatedSections = document.querySelectorAll('.royal-section');
    if (!animatedSections.length) return;

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      animatedSections.forEach(sec => sec.classList.add('is-visible'));
      return;
    }

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.10,
      rootMargin: '0px 0px -40px 0px'
    });

    animatedSections.forEach(sec => observer.observe(sec));
  }


  // ==========================================================================
  // PHASE 5: SECTION 10 — ZITE RSVP INTEGRATION
  // Primary Reference: Page 6 of DEBUT INVITATION.pdf
  // ==========================================================================

  /**
   * Official Zite RSVP Configuration
   * ---------------------------------
   * The RSVP system is being hosted separately using Zite.
   * Paste the official published Zite RSVP website URL below when available.
   *
   * IMPORTANT:
   * Do NOT use the editor link (e.g., https://app.zite.com/editor/oinyLbhrWgus/edit/gXFa)
   * as the destination. The system will detect and reject editor links.
   *
   * Example of a valid published link: "https://jennina18thdebut.zite.site"
   */
  const RSVP_URL = "https://3gtkwbxbwf.zite.so";

  /**
   * Optional Facebook Messenger RSVP Configuration
   * ----------------------------------------------
   * If the celebrant wants guests to reply via Messenger, paste the link below:
   * Example: "https://m.me/jennina.debut"
   * If left empty, the Messenger RSVP button remains safely hidden.
   */
  const MESSENGER_URL = "";

  /**
   * Detects whether a given URL is an internal Zite editor/admin link
   */
  function isZiteEditorUrl(url) {
    if (!url || typeof url !== 'string') return false;
    const lower = url.trim().toLowerCase();
    return lower.includes('zite.com/editor') || lower.includes('/edit/') || lower.includes('editor.zite');
  }

  /**
   * Initializes and manages the Zite RSVP and Messenger integration
   * Supports optional parameter overrides for testability without mutating source constants.
   */
  function initRsvpIntegration(customRsvpUrl, customMessengerUrl) {
    const btnZite = document.getElementById('btnZiteRsvp');
    const lblZite = document.getElementById('lblZiteRsvp');
    const btnMessenger = document.getElementById('btnMessengerRsvp');
    const statusNote = document.getElementById('rsvpStatusNote');

    if (!btnZite) return;

    // Determine effective URLs (passed arguments take precedence for testing)
    const effectiveRsvpUrl = typeof customRsvpUrl !== 'undefined' ? customRsvpUrl : RSVP_URL;
    const effectiveMessengerUrl = typeof customMessengerUrl !== 'undefined' ? customMessengerUrl : MESSENGER_URL;

    const trimmedRsvp = (effectiveRsvpUrl || '').trim();
    const isEditor = isZiteEditorUrl(trimmedRsvp);
    const hasValidPublishedUrl = Boolean(trimmedRsvp && !isEditor);

    // Remove any previously attached click listener by cloning or direct property assignment
    btnZite.onclick = null;

    if (hasValidPublishedUrl) {
      // ----------------------------------------------------------------------
      // ACTIVATED STATE: Valid Published Zite RSVP URL
      // ----------------------------------------------------------------------
      btnZite.href = trimmedRsvp;
      btnZite.target = "_blank";
      btnZite.rel = "noopener noreferrer";
      btnZite.classList.remove('btn-disabled');
      btnZite.removeAttribute('aria-disabled');
      btnZite.setAttribute('title', 'Open official Zite RSVP form in a new tab');
      if (lblZite) lblZite.textContent = "Confirm Your Attendance";

      if (statusNote) {
        statusNote.textContent = "You will be safely redirected to our official RSVP page.";
        statusNote.className = "rsvp-status-note status-active";
      }
    } else {
      // ----------------------------------------------------------------------
      // DISABLED STATE: Empty URL or Disallowed Editor URL
      // ----------------------------------------------------------------------
      btnZite.href = "javascript:void(0);";
      btnZite.removeAttribute('target');
      btnZite.removeAttribute('rel');
      btnZite.classList.add('btn-disabled');
      btnZite.setAttribute('aria-disabled', 'true');
      btnZite.setAttribute('title', 'RSVP form link will be available soon');
      if (lblZite) lblZite.textContent = "RSVP Link Coming Soon";

      if (isEditor) {
        console.warn("[Zite RSVP Integration] The configured URL is an editor link ('" + trimmedRsvp + "') which is not accessible to guests. Please configure the published Zite RSVP URL.");
        if (statusNote) {
          statusNote.textContent = "RSVP link is currently being prepared. Kindly check back shortly!";
          statusNote.className = "rsvp-status-note status-pending";
        }
      } else {
        if (statusNote) {
          statusNote.textContent = "The official RSVP page will open here soon. Kindly check back shortly!";
          statusNote.className = "rsvp-status-note status-pending";
        }
      }

      // Safe click interceptor: Prevents navigation and courteously informs the guest
      btnZite.onclick = function (e) {
        e.preventDefault();
        if (statusNote) {
          statusNote.textContent = "The official RSVP link is being finalized. Kindly check back shortly!";
          statusNote.className = "rsvp-status-note status-pending";
        }
        announce("The official RSVP link is coming soon. Please check back shortly.");
      };
    }

    // ------------------------------------------------------------------------
    // OPTIONAL MESSENGER RSVP INTEGRATION
    // ------------------------------------------------------------------------
    if (btnMessenger) {
      const trimmedMessenger = (effectiveMessengerUrl || '').trim();
      if (trimmedMessenger) {
        btnMessenger.href = trimmedMessenger;
        btnMessenger.target = "_blank";
        btnMessenger.rel = "noopener noreferrer";
        btnMessenger.style.display = "inline-flex";
      } else {
        btnMessenger.style.display = "none";
        btnMessenger.removeAttribute('href');
      }
    }
  }

  // Expose test helper on window for automated verification without modifying source
  window.__setRsvpUrlsForTesting = function (ziteUrl, messengerUrl) {
    initRsvpIntegration(ziteUrl, messengerUrl);
  };

  /**
   * Official Invitation Lightbox Modal
   * Allows guests (especially on mobile) to tap to view an enlarged version
   */
  function initInvitationLightbox() {
    const container = document.querySelector('.official-invitation-container');
    const modal = document.getElementById('invitationLightbox');
    const closeBtn = document.getElementById('lightboxCloseBtn');
    const backdrop = document.getElementById('lightboxBackdrop');

    if (!container || !modal) return;

    function openModal() {
      modal.removeAttribute('hidden');
      requestAnimationFrame(() => modal.classList.add('active'));
      document.body.style.overflow = 'hidden';
      if (closeBtn) closeBtn.focus();
    }

    function closeModal() {
      modal.classList.remove('active');
      setTimeout(() => {
        modal.setAttribute('hidden', '');
        document.body.style.overflow = '';
        container.focus();
      }, 300);
    }

    container.addEventListener('click', openModal);
    container.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openModal();
      }
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (backdrop) backdrop.addEventListener('click', closeModal);
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // Initialize Dynamic Elements
  populateTraditionLists();
  initMobileTraditionTabs();
  populateAttireSection();
  initSectionObserver();
  initRsvpIntegration();
  initInvitationLightbox();


})();

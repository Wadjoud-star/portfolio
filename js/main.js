// ── Projets ──
const projects = [
  {
    id: 'factis',
    name: 'Factis',
    color: '#6366f1',
    featured: true,
    status: 'soon',
    stack: ['Next.js', 'TypeScript', 'Prisma', 'PostgreSQL', 'Stripe', 'Tailwind'],
    github: 'https://github.com/Wadjoud-star/factis',
    demo: null,
    image: 'assets/projects/factis-landing.png',
    gallery: [
      { src: 'assets/projects/factis-landing.png', labelKey: 'projects.gallery.landing' },
      { src: 'assets/projects/factis-dashboard.png', labelKey: 'projects.gallery.dashboard' },
      { src: 'assets/projects/factis-client.png', labelKey: 'projects.gallery.client' },
      { src: 'assets/projects/factis-facture.png', labelKey: 'projects.gallery.newInvoice' },
      { src: 'assets/projects/factis-factures.png', labelKey: 'projects.gallery.invoiceList' },
      { src: 'assets/projects/factis-depenses.png', labelKey: 'projects.gallery.expenses' }
    ]
  },
  {
    id: 'beniphone',
    name: 'Beniphone',
    color: '#8b5cf6',
    featured: true,
    status: 'soon',
    stack: ['React', 'Vite', 'Tailwind', 'Node.js', 'Express', 'Prisma'],
    github: 'https://github.com/Wadjoud-star/beniphone',
    demo: null,
    image: 'assets/projects/beniphone-landing.png',
    gallery: [
      { src: 'assets/projects/beniphone-landing.png', labelKey: 'projects.gallery.landing' },
      { src: 'assets/projects/beniphone-catalogue.png', labelKey: 'projects.gallery.catalog' },
      { src: 'assets/projects/beniphone-parcours.png', labelKey: 'projects.gallery.journey' },
      { src: 'assets/projects/beniphone-acheteur.png', labelKey: 'projects.gallery.buyerSpace' },
      { src: 'assets/projects/beniphone-vendeur.png', labelKey: 'projects.gallery.sellerSpace' },
      { src: 'assets/projects/beniphone-annonce.png', labelKey: 'projects.gallery.listing' },
      { src: 'assets/projects/beniphone-messagerie.png', labelKey: 'projects.gallery.messaging' },
      { src: 'assets/projects/beniphone-admin.png', labelKey: 'projects.gallery.admin' }
    ]
  },
  {
    id: 'smartcms',
    name: 'Smart CMS IA',
    color: '#06b6d4',
    featured: false,
    status: 'soon',
    stack: ['Next.js', 'OpenAI', 'Supabase', 'Stripe', 'TipTap'],
    github: 'https://github.com/Wadjoud-star/smart-cms-ia',
    demo: null,
    image: 'assets/projects/smartcms-landing.png',
    gallery: [
      { src: 'assets/projects/smartcms-landing.png', labelKey: 'projects.gallery.landing' },
      { src: 'assets/projects/smartcms-projets.png', labelKey: 'projects.gallery.projects' },
      { src: 'assets/projects/smartcms-editeur.png', labelKey: 'projects.gallery.editor' },
      { src: 'assets/projects/smartcms-linkedin.png', labelKey: 'projects.gallery.linkedin' },
      { src: 'assets/projects/smartcms-twitter.png', labelKey: 'projects.gallery.twitter' },
      { src: 'assets/projects/smartcms-illustration.png', labelKey: 'projects.gallery.illustration' }
    ]
  },
  {
    id: 'demenagement',
    name: 'Mon Déménagement',
    color: '#10b981',
    featured: false,
    status: 'live',
    stack: ['PHP', 'MySQL', 'Bootstrap', 'JavaScript'],
    github: 'https://github.com/Wadjoud-star/Plateforme-D-m-nagement',
    demo: 'http://d-m-nagement.web1337.net/demenagement',
    image: 'assets/projects/demenagement-accueil.png',
    gallery: [
      { src: 'assets/projects/demenagement-accueil.png', labelKey: 'projects.gallery.home' },
      { src: 'assets/projects/demenagement-client.png', labelKey: 'projects.gallery.client' },
      { src: 'assets/projects/demenagement-demenageur.png', labelKey: 'projects.gallery.mover' }
    ],
    video: 'assets/videos/déménagement.mov'
  },
  {
    id: 'clubsport',
    name: 'Club Sport',
    color: '#f59e0b',
    featured: false,
    status: 'local',
    stack: ['Java', 'JSP/Servlets', 'MySQL', 'Docker'],
    github: 'https://github.com/Wadjoud-star/Projet-S8',
    demo: 'local',
    image: 'assets/projects/clubsport-recherche.png',
    gallery: [
      { src: 'assets/projects/clubsport-recherche.png', labelKey: 'projects.gallery.search' },
      { src: 'assets/projects/clubsport-dashboard-elu.png', labelKey: 'projects.gallery.officialDashboard' },
      { src: 'assets/projects/clubsport-statistiques.png', labelKey: 'projects.gallery.stats' },
      { src: 'assets/projects/clubsport-cartographie.png', labelKey: 'projects.gallery.mapping' },
      { src: 'assets/projects/clubsport-espace-club.png', labelKey: 'projects.gallery.clubSpace' }
    ]
  }
];

let openModalId = null;

// ── Badge de statut (En ligne, Bientôt, Local) ──
function statusBadge(status) {
  const labels = {
    live: { fr: 'En ligne', en: 'Live', cls: 'badge-live' },
    soon: { fr: 'Bientôt', en: 'Soon', cls: 'badge-soon' },
    local: { fr: 'Local', en: 'Local', cls: 'badge-local' }
  };
  const s = labels[status] || labels.soon;
  return `<span class="badge ${s.cls}">${s[currentLang]}</span>`;
}

// ── Affichage des compétences ──
function renderSkills() {
  const wrap = document.getElementById('skills-wrap');
  if (!wrap) return;

  wrap.innerHTML = skillsData.map(group => `
    <div class="skill-group">
      <h3><span>${group.icon}</span> ${t(group.key)}</h3>
      <div class="skill-chips">
        ${group.items.map(item => `<span class="chip">${item}</span>`).join('')}
      </div>
    </div>
  `).join('');
}

// ── Liens GitHub / Démo ──
function buildProjectLinks(project) {
  const githubLink = project.github
    ? `<a href="${project.github}" target="_blank" rel="noopener" class="project-link">→ ${t('projects.github')}</a>`
    : `<span class="project-link disabled">${t('projects.github')}</span>`;

  let demoLink;
  if (project.demo === 'local') {
    demoLink = `<span class="project-link disabled">${t('projects.demo')} (${t('projects.local')})</span>`;
  } else if (project.demo) {
    demoLink = `<a href="${project.demo}" target="_blank" rel="noopener" class="project-link">→ ${t('projects.demo')}</a>`;
  } else {
    demoLink = `<span class="project-link disabled">${t('projects.demo')}</span>`;
  }

  return githubLink + demoLink;
}

// ── Cartes projets (compactes) ──
function renderProjects() {
  const grid = document.getElementById('projects-grid');
  if (!grid) return;

  grid.innerHTML = projects.map((project, i) => {
    const desc = projectTexts[project.id][currentLang];
    const type = projectTypes[project.id][currentLang];
    const tags = project.stack.map(s => `<span class="tag">${s}</span>`).join('');
    const featuredClass = project.featured ? ' featured' : '';

    const mainImage = project.image || (project.gallery && project.gallery[0].src);
    const imageContent = mainImage
      ? `<img src="${mainImage}" alt="${project.name}">`
      : `<span class="project-placeholder">${project.name.substring(0, 2)}</span>`;

    return `
      <article class="project-card${featuredClass} fade-in" style="transition-delay: ${i * 0.08}s"
               data-id="${project.id}" tabindex="0" role="button" aria-label="${project.name}">
        <div class="project-image" style="background: linear-gradient(160deg, ${project.color}22, ${project.color}08);">
          <div class="project-badges">
            <span class="badge badge-type">${type}</span>
            ${statusBadge(project.status)}
          </div>
          ${imageContent}
        </div>
        <div class="project-body">
          <h3>${project.name}</h3>
          <p>${desc}</p>
          <div class="project-tags">${tags}</div>
          <div class="project-links">${buildProjectLinks(project)}</div>
          <span class="project-hint">${t('projects.viewDetail')}</span>
        </div>
      </article>
    `;
  }).join('');

  observeFadeIns();
  initProjectCards();
}

// ── Clic sur une carte → ouvre le modal ──
function initProjectCards() {
  document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('click', () => openProjectModal(card.dataset.id));
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openProjectModal(card.dataset.id);
      }
    });
    // Empêche le modal de s'ouvrir quand on clique sur un lien
    card.querySelectorAll('.project-link:not(.disabled)').forEach(link => {
      link.addEventListener('click', e => e.stopPropagation());
    });
  });
}

// ── Type MIME selon l'extension vidéo ──
function getVideoType(src) {
  if (src.endsWith('.mov')) return 'video/quicktime';
  if (src.endsWith('.webm')) return 'video/webm';
  return 'video/mp4';
}

// ── Contenu du modal ──
function openProjectModal(id) {
  const project = projects.find(p => p.id === id);
  if (!project) return;

  openModalId = id;
  const modal = document.getElementById('project-modal');
  const body = document.getElementById('modal-body');
  const type = projectTypes[project.id][currentLang];
  const detail = projectDetails[project.id][currentLang];
  const tags = project.stack.map(s => `<span class="tag">${s}</span>`).join('');
  const mainImage = project.image || (project.gallery && project.gallery[0].src);

  let galleryHTML = '';
  if (project.gallery) {
    galleryHTML = `
      <div class="modal-gallery">
        <div class="modal-gallery-main">
          <img id="modal-main-img" src="${project.gallery[0].src}" alt="${project.name}">
        </div>
        <div class="modal-gallery-thumbs">
          ${project.gallery.map((item, idx) => `
            <button type="button" class="gallery-thumb${idx === 0 ? ' active' : ''}" data-src="${item.src}">
              <img src="${item.src}" alt="${t(item.labelKey)}">
              <span>${t(item.labelKey)}</span>
            </button>
          `).join('')}
        </div>
      </div>`;
  }

  let featuresHTML = '';
  const features = projectFeatures[project.id];
  if (features) {
    featuresHTML = `
      <div class="modal-features">
        <h4>${t('projects.features')}</h4>
        <ul>${features[currentLang].map(f => `<li>${f}</li>`).join('')}</ul>
      </div>`;
  }

  let videoHTML = '';
  if (project.video) {
    videoHTML = `
      <div class="modal-video">
        <h4>${t('projects.video')}</h4>
        <video controls preload="metadata" poster="${mainImage || ''}">
          <source src="${project.video}" type="${getVideoType(project.video)}">
        </video>
        <p class="video-placeholder">${t('projects.videoSoon')}</p>
      </div>`;
  }

  body.innerHTML = `
    <div class="modal-header">
      <div class="modal-badges">
        <span class="badge badge-type">${type}</span>
        ${statusBadge(project.status)}
      </div>
      <h2>${project.name}</h2>
      <div class="project-tags">${tags}</div>
    </div>
    ${galleryHTML}
    <p class="modal-desc">${detail}</p>
    ${featuresHTML}
    ${videoHTML}
    <div class="modal-links">${buildProjectLinks(project)}</div>
  `;

  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';

  initModalGallery();
  checkModalVideo();
}

function refreshOpenModal() {
  if (openModalId) openProjectModal(openModalId);
}

function closeProjectModal() {
  const modal = document.getElementById('project-modal');
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  openModalId = null;

  // Stop la vidéo si en cours
  const video = modal.querySelector('video');
  if (video) video.pause();
}

// ── Galerie dans le modal ──
function initModalGallery() {
  document.querySelectorAll('#modal-body .gallery-thumb').forEach(thumb => {
    thumb.addEventListener('click', () => {
      const mainImg = document.getElementById('modal-main-img');
      if (mainImg) mainImg.src = thumb.dataset.src;
      document.querySelectorAll('#modal-body .gallery-thumb').forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');
    });
  });
}

// ── Vérifie si la vidéo existe ──
function checkModalVideo() {
  const block = document.querySelector('#modal-body .modal-video');
  if (!block) return;

  const video = block.querySelector('video');
  const placeholder = block.querySelector('.video-placeholder');
  const src = video.querySelector('source')?.getAttribute('src');

  fetch(src, { method: 'HEAD' })
    .then(res => {
      if (res.ok) {
        placeholder.style.display = 'none';
      } else {
        video.style.display = 'none';
      }
    })
    .catch(() => {
      video.style.display = 'none';
    });
}

// ── Initialisation du modal ──
function initModal() {
  document.getElementById('modal-close').addEventListener('click', closeProjectModal);
  document.getElementById('modal-backdrop').addEventListener('click', closeProjectModal);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeProjectModal();
  });
}

// ── Animation texte rotatif (hero) ──
let typingIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingTimer = null;

function restartTyping() {
  clearTimeout(typingTimer);
  typingIndex = 0;
  charIndex = 0;
  isDeleting = false;
  typeNextChar();
}

function typeNextChar() {
  const el = document.getElementById('typing');
  if (!el) return;

  const roles = typingRoles[currentLang];
  const current = roles[typingIndex];

  if (!isDeleting) {
    el.textContent = current.substring(0, charIndex + 1);
    charIndex++;
    if (charIndex === current.length) {
      isDeleting = true;
      typingTimer = setTimeout(typeNextChar, 2000);
      return;
    }
    typingTimer = setTimeout(typeNextChar, 80);
  } else {
    el.textContent = current.substring(0, charIndex - 1);
    charIndex--;
    if (charIndex === 0) {
      isDeleting = false;
      typingIndex = (typingIndex + 1) % roles.length;
      typingTimer = setTimeout(typeNextChar, 400);
      return;
    }
    typingTimer = setTimeout(typeNextChar, 40);
  }
}

// ── Animations au scroll ──
function observeFadeIns() {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('.fade-in:not(.visible)').forEach(el => observer.observe(el));
}

// ── Navigation active + scroll progress ──
function initScroll() {
  const header = document.getElementById('header');
  const progress = document.getElementById('scroll-progress');
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a[data-section]');

  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);

    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (scrollTop / docHeight * 100) + '%';

    let current = '';
    sections.forEach(section => {
      if (scrollTop >= section.offsetTop - 120) {
        current = section.id;
      }
    });
    navLinks.forEach(link => {
      link.classList.toggle('active', link.dataset.section === current);
    });
  });
}

// ── Menu mobile ──
function initNav() {
  const toggle = document.getElementById('nav-toggle');
  const links = document.getElementById('nav-links');

  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });

  links.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      links.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// ── Bouton retour en haut ──
function initBackTop() {
  document.getElementById('back-top').addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ── Langue ──
function initLangButton() {
  document.getElementById('lang-btn').addEventListener('click', () => {
    setLanguage(currentLang === 'fr' ? 'en' : 'fr');
  });
}

// ── Démarrage ──
document.addEventListener('DOMContentLoaded', () => {
  document.documentElement.classList.add('js-ready');
  initLanguage();
  renderSkills();
  renderProjects();
  observeFadeIns();
  typeNextChar();
  initScroll();
  initNav();
  initBackTop();
  initLangButton();
  initModal();
});

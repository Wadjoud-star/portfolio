// Traductions FR / EN
const translations = {
  fr: {
    'nav.about': 'À propos',
    'nav.skills': 'Compétences',
    'nav.projects': 'Projets',
    'nav.experience': 'Parcours',
    'nav.contact': 'Contact',

    'hero.badge': 'Disponible pour alternance & missions freelance',
    'hero.greeting': 'Bonjour, je suis',
    'hero.rolePrefix': 'Développeur',
    'hero.desc': "J'accompagne entreprises et recruteurs avec des applications web complètes — du backend à l'interface, de l'idée au déploiement.",
    'hero.cta.projects': 'Voir mes projets',
    'hero.cta.contact': 'Me contacter',
    'hero.cta.cv': 'Télécharger mon CV',
    'hero.stat.projects': 'Projets livrés',
    'hero.stat.school': 'Ingénieur Dev Web',

    'stats.projects': 'Projets réalisés',
    'stats.tech': 'Technologies',
    'stats.profile': 'Profil polyvalent',
    'stats.lang': 'Bilingue',

    'about.title': 'À propos',
    'about.p1': "Élève ingénieur à l'ESIGELEC Rouen (bac+5, développement web full stack), je conçois des applications web de A à Z : analyse, développement, tests et déploiement.",
    'about.p2': "Mon profil s'adresse autant aux recruteurs qu'aux clients freelance — je livre des projets concrets, maintenables et orientés métier.",
    'about.q1': 'Autonome',
    'about.q2': 'Force de proposition',
    'about.q3': "Esprit d'équipe",
    'about.q4': 'Rigoureux',
    'about.location': 'Localisation',
    'about.education': 'Formation',
    'about.languages': 'Langues',
    'about.languagesValue': 'Français (natif) · Anglais B2',

    'skills.title': 'Compétences',
    'skills.backend': 'Backend & Web',
    'skills.frontend': 'Frontend',
    'skills.api': 'API & Bases de données',
    'skills.devops': 'DevOps & Outils',

    'projects.title': 'Projets',
    'projects.desc': 'Des applications complètes, pensées pour un vrai usage.',
    'projects.github': 'Code',
    'projects.demo': 'Démo',
    'projects.soon': 'Bientôt',
    'projects.local': 'Local',
    'projects.video': 'Vidéo démo',
    'projects.videoSoon': 'Vidéo bientôt disponible',
    'projects.gallery.home': 'Accueil',
    'projects.gallery.client': 'Client',
    'projects.gallery.mover': 'Déménageur',
    'projects.gallery.landing': 'Landing',
    'projects.gallery.dashboard': 'Dashboard',
    'projects.gallery.invoice': 'Factures',
    'projects.gallery.newInvoice': 'Nouvelle facture',
    'projects.gallery.invoiceList': 'Liste factures',
    'projects.gallery.expenses': 'Dépenses',
    'projects.gallery.catalog': 'Catalogue',
    'projects.gallery.journey': 'Parcours utilisateur',
    'projects.gallery.buyerSpace': 'Espace acheteur',
    'projects.gallery.sellerSpace': 'Espace vendeur',
    'projects.gallery.listing': 'Nouvelle annonce',
    'projects.gallery.messaging': 'Messagerie',
    'projects.gallery.admin': 'Administration',
    'projects.gallery.search': 'Recherche & carte',
    'projects.gallery.officialDashboard': 'Espace élu',
    'projects.gallery.stats': 'Statistiques',
    'projects.gallery.mapping': 'Cartographie',
    'projects.gallery.clubSpace': 'Espace club',
    'projects.gallery.projects': 'Mes projets',
    'projects.gallery.editor': 'Éditeur blog',
    'projects.gallery.linkedin': 'Post LinkedIn',
    'projects.gallery.twitter': 'Tweet X',
    'projects.gallery.illustration': 'Illustration IA',
    'projects.viewDetail': 'Voir le détail →',
    'projects.features': 'Fonctionnalités',
    'projects.close': 'Fermer',

    'experience.title': 'Parcours',
    'experience.esigelec.title': "Diplôme d'Ingénieur — Dev Web Full Stack",
    'experience.esigelec.desc': 'PHP, Java, C#, Angular, TypeScript, Docker, API REST, WordPress, Agile',
    'experience.prep.title': 'Cycle préparatoire',
    'experience.promo.title': 'Stagiaire Informatique',
    'experience.promo.desc': "Recueil des besoins, diagnostic d'incidents, maintenance parc informatique et serveurs",

    'contact.title': 'Travaillons ensemble',
    'contact.desc': 'Alternance, mission freelance ou simple échange — je réponds sous 24h.',
    'contact.email': 'Envoyer un email',
    'contact.cv': 'Télécharger mon CV',

    'footer.rights': 'Tous droits réservés'
  },

  en: {
    'nav.about': 'About',
    'nav.skills': 'Skills',
    'nav.projects': 'Projects',
    'nav.experience': 'Experience',
    'nav.contact': 'Contact',

    'hero.badge': 'Available for apprenticeship & freelance work',
    'hero.greeting': "Hi, I'm",
    'hero.rolePrefix': 'Developer',
    'hero.desc': 'I help companies and recruiters with complete web applications — from backend to UI, from idea to deployment.',
    'hero.cta.projects': 'View my projects',
    'hero.cta.contact': 'Get in touch',
    'hero.cta.cv': 'Download my CV',
    'hero.stat.projects': 'Projects delivered',
    'hero.stat.school': 'Web Dev Engineer',

    'stats.projects': 'Projects built',
    'stats.tech': 'Technologies',
    'stats.profile': 'Versatile profile',
    'stats.lang': 'Bilingual',

    'about.title': 'About',
    'about.p1': 'Engineering student at ESIGELEC Rouen (MSc, full stack web development), I build web applications end-to-end: analysis, development, testing and deployment.',
    'about.p2': 'My profile suits both recruiters and freelance clients — I deliver concrete, maintainable, business-oriented projects.',
    'about.q1': 'Self-driven',
    'about.q2': 'Proactive',
    'about.q3': 'Team player',
    'about.q4': 'Detail-oriented',
    'about.location': 'Location',
    'about.education': 'Education',
    'about.languages': 'Languages',
    'about.languagesValue': 'French (native) · English B2',

    'skills.title': 'Skills',
    'skills.backend': 'Backend & Web',
    'skills.frontend': 'Frontend',
    'skills.api': 'API & Databases',
    'skills.devops': 'DevOps & Tools',

    'projects.title': 'Projects',
    'projects.desc': 'Complete applications built for real-world use.',
    'projects.github': 'Code',
    'projects.demo': 'Demo',
    'projects.soon': 'Soon',
    'projects.local': 'Local',
    'projects.video': 'Demo video',
    'projects.videoSoon': 'Video coming soon',
    'projects.gallery.home': 'Home',
    'projects.gallery.client': 'Client',
    'projects.gallery.mover': 'Mover',
    'projects.gallery.landing': 'Landing',
    'projects.gallery.dashboard': 'Dashboard',
    'projects.gallery.invoice': 'Invoices',
    'projects.gallery.newInvoice': 'New invoice',
    'projects.gallery.invoiceList': 'Invoice list',
    'projects.gallery.expenses': 'Expenses',
    'projects.gallery.catalog': 'Catalog',
    'projects.gallery.journey': 'User journey',
    'projects.gallery.buyerSpace': 'Buyer space',
    'projects.gallery.sellerSpace': 'Seller space',
    'projects.gallery.listing': 'New listing',
    'projects.gallery.messaging': 'Messaging',
    'projects.gallery.admin': 'Administration',
    'projects.gallery.search': 'Search & map',
    'projects.gallery.officialDashboard': 'Official dashboard',
    'projects.gallery.stats': 'Statistics',
    'projects.gallery.mapping': 'Mapping',
    'projects.gallery.clubSpace': 'Club space',
    'projects.gallery.projects': 'My projects',
    'projects.gallery.editor': 'Blog editor',
    'projects.gallery.linkedin': 'LinkedIn post',
    'projects.gallery.twitter': 'X tweet',
    'projects.gallery.illustration': 'AI illustration',
    'projects.viewDetail': 'View details →',
    'projects.features': 'Features',
    'projects.close': 'Close',

    'experience.title': 'Experience',
    'experience.esigelec.title': 'Engineering Degree — Full Stack Web Dev',
    'experience.esigelec.desc': 'PHP, Java, C#, Angular, TypeScript, Docker, REST API, WordPress, Agile',
    'experience.prep.title': 'Preparatory cycle',
    'experience.promo.title': 'IT Intern',
    'experience.promo.desc': 'Requirements gathering, incident diagnosis, IT infrastructure and server maintenance',

    'contact.title': "Let's work together",
    'contact.desc': 'Apprenticeship, freelance project or just a chat — I reply within 24h.',
    'contact.email': 'Send an email',
    'contact.cv': 'Download my CV',

    'footer.rights': 'All rights reserved'
  }
};

// Rôles affichés en rotation dans le hero
const typingRoles = {
  fr: ['Fullstack', 'React & Next.js', 'PHP & Java', 'API REST'],
  en: ['Fullstack', 'React & Next.js', 'PHP & Java', 'REST APIs']
};

// Descriptions des projets
const projectTexts = {
  factis: {
    fr: 'Mini-SaaS de facturation pour freelances et micro-entrepreneurs. France (TVA, SIRET) et Bénin (FCFA, IFU). Factures PDF, analytics, abonnement Stripe.',
    en: 'Billing mini-SaaS for freelancers and micro-entrepreneurs. France (VAT, SIRET) and Benin (FCFA, IFU). PDF invoices, analytics, Stripe subscription.'
  },
  beniphone: {
    fr: 'Marketplace Apple full-stack (Bénin) — catalogue, KYC vendeur, chat avec offres, transactions tracées et dashboard admin.',
    en: 'Full-stack Apple marketplace (Benin) — catalog, seller KYC, chat with offers, tracked transactions and admin dashboard.'
  },
  smartcms: {
    fr: 'CMS intelligent : un thème devient un pack complet (blog, LinkedIn, Twitter/X, illustration IA). Éditeur riche, SEO, export Markdown/HTML.',
    en: 'Smart CMS: turn a theme into a full content pack (blog, LinkedIn, Twitter/X, AI illustration). Rich editor, SEO, Markdown/HTML export.'
  },
  demenagement: {
    fr: 'Mise en relation particuliers / déménageurs. Annonces avec photos, propositions de prix, messagerie, évaluations et espace admin.',
    en: 'Connects individuals with movers. Listings with photos, price proposals, messaging, reviews and admin panel.'
  },
  clubsport: {
    fr: 'Exploration des clubs sportifs français. App JEE multi-rôles : cartographie, statistiques, exports et gestion de profils.',
    en: 'Explore French sports clubs. Multi-role JEE app: mapping, statistics, exports and profile management.'
  }
};

// Descriptions détaillées (modal)
const projectDetails = {
  factis: {
    fr: 'Mini-SaaS de facturation et gestion financière pour freelances et micro-entrepreneurs. France (TVA, SIRET, mentions légales) et Bénin (FCFA, IFU, e-MECeF). Inscription, onboarding, clients, factures PDF conformes, dépenses, analytics, abonnement Stripe (Gratuit / Pro) et envoi par email.',
    en: 'Billing and financial management mini-SaaS for freelancers and micro-entrepreneurs. France (VAT, SIRET, legal mentions) and Benin (FCFA, IFU, e-MECeF). Signup, onboarding, clients, compliant PDF invoices, expenses, analytics, Stripe subscription (Free / Pro) and email delivery.'
  },
  beniphone: {
    fr: 'Marketplace Apple full-stack dédiée au Bénin. Catalogue produits, vérification KYC des vendeurs, messagerie avec offres, transactions tracées et dashboard administrateur. Projet orienté UI/UX et architecture API complète.',
    en: 'Full-stack Apple marketplace for Benin. Product catalog, seller KYC verification, messaging with offers, tracked transactions and admin dashboard. Focus on UI/UX and complete API architecture.'
  },
  smartcms: {
    fr: 'CMS intelligent qui génère un pack de contenu complet à partir d\'un thème ou nom de produit : article de blog, posts LinkedIn et Twitter/X, illustration IA. Éditeur riche, optimisation SEO, export Markdown/HTML et historique des projets.',
    en: 'Smart CMS that generates a full content pack from a theme or product name: blog article, LinkedIn and Twitter/X posts, AI illustration. Rich editor, SEO optimization, Markdown/HTML export and project history.'
  },
  demenagement: {
    fr: 'Plateforme web de mise en relation entre particuliers et déménageurs professionnels. Les clients publient une annonce (volume, trajet, photos), reçoivent des propositions, choisissent un prestataire et évaluent la prestation. Les déménageurs consultent les annonces, posent des questions et soumettent des offres. Un espace admin supervise l\'activité.',
    en: 'Web platform connecting individuals with professional movers. Clients post listings (volume, route, photos), receive proposals, choose a provider and rate the service. Movers browse listings, ask questions and submit offers. An admin panel supervises all activity.'
  },
  clubsport: {
    fr: 'Application JEE multi-rôles pour centraliser l\'exploration des clubs sportifs français. Cartographie interactive, statistiques, exports de données et gestion de profils pour élus, membres et acteurs du sport.',
    en: 'Multi-role JEE application to centralize exploration of French sports clubs. Interactive mapping, statistics, data exports and profile management for officials, members and sports stakeholders.'
  }
};

// Fonctionnalités clés (modal)
const projectFeatures = {
  factis: {
    fr: [
      'Onboarding avec profil légal (France & Bénin)',
      'Factures PDF conformes et numérotation inviolable',
      'Gestion clients, dépenses et analytics',
      'Abonnement Stripe Gratuit / Pro'
    ],
    en: [
      'Onboarding with legal profile (France & Benin)',
      'Compliant PDF invoices and secure numbering',
      'Client, expense and analytics management',
      'Stripe Free / Pro subscription'
    ]
  },
  demenagement: {
    fr: ['Annonces avec photos et détails du volume', 'Propositions de prix et messagerie interne', 'Espaces Client, Déménageur et Admin', 'Évaluation des prestations'],
    en: ['Listings with photos and volume details', 'Price proposals and internal messaging', 'Client, Mover and Admin spaces', 'Service ratings']
  },
  beniphone: {
    fr: [
      'Catalogue Apple avec filtres et recherche',
      'KYC vendeur et publication d\'annonces modérées',
      'Négociation de prix tracée en messagerie',
      'Espaces acheteur, vendeur et admin'
    ],
    en: [
      'Apple catalog with filters and search',
      'Seller KYC and moderated listing publication',
      'Tracked price negotiation via messaging',
      'Buyer, seller and admin spaces'
    ]
  },
  smartcms: {
    fr: [
      'Génération IA : blog, LinkedIn, Twitter/X, illustration',
      'Jobs asynchrones avec progression en temps réel',
      'Éditeur riche TipTap avec auto-save',
      'Score SEO, export Markdown/HTML et abonnement Pro'
    ],
    en: [
      'AI generation: blog, LinkedIn, Twitter/X, illustration',
      'Async jobs with real-time progress',
      'TipTap rich editor with auto-save',
      'SEO score, Markdown/HTML export and Pro subscription'
    ]
  },
  clubsport: {
    fr: [
      'Recherche de clubs par fédération, commune ou rayon',
      'Cartographie choroplèthe et statistiques de licences',
      'Espace élu : exports CSV et tableaux de bord',
      'Espace club : actualités, horaires et cotisations'
    ],
    en: [
      'Club search by federation, municipality or radius',
      'Choropleth mapping and license statistics',
      'Official space: CSV exports and dashboards',
      'Club space: news, schedules and membership fees'
    ]
  }
};

// Types de projets (badge)
const projectTypes = {
  factis: { fr: 'SaaS', en: 'SaaS' },
  beniphone: { fr: 'Marketplace', en: 'Marketplace' },
  smartcms: { fr: 'CMS + IA', en: 'CMS + AI' },
  demenagement: { fr: 'Web App', en: 'Web App' },
  clubsport: { fr: 'JEE', en: 'JEE' }
};

// Compétences par catégorie
const skillsData = [
  { icon: '⚙️', key: 'skills.backend', items: ['PHP', 'Java', 'Spring Boot', 'C#', 'ASP.NET', 'Python', 'Node.js'] },
  { icon: '🎨', key: 'skills.frontend', items: ['HTML5', 'CSS3', 'JavaScript', 'TypeScript', 'React', 'Angular', 'Tailwind'] },
  { icon: '🔗', key: 'skills.api', items: ['REST API', 'Swagger', 'JWT', 'MySQL', 'PostgreSQL', 'Prisma', 'Oracle'] },
  { icon: '🚀', key: 'skills.devops', items: ['Git', 'Docker', 'CI/CD', 'Linux', 'WordPress', 'Stripe', 'Supabase'] }
];

let currentLang = 'fr';

function t(key) {
  return translations[currentLang][key] || key;
}

function setLanguage(lang) {
  currentLang = lang;
  document.documentElement.lang = lang;

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[lang][key]) {
      el.textContent = translations[lang][key];
    }
  });

  document.getElementById('lang-btn').textContent = lang === 'fr' ? 'EN' : 'FR';
  localStorage.setItem('portfolio-lang', lang);

  if (typeof renderSkills === 'function') renderSkills();
  if (typeof renderProjects === 'function') renderProjects();
  if (typeof restartTyping === 'function') restartTyping();
  if (typeof refreshOpenModal === 'function') refreshOpenModal();
}

function initLanguage() {
  const saved = localStorage.getItem('portfolio-lang');
  if (saved === 'en' || saved === 'fr') setLanguage(saved);
}

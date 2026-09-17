# Fiche de révision — Test Coderpad Winamax
### Stage Fullstack — Format de contenu interactif
**Objectif :** passer le test (~75–80 %) en 3 jours de révision ciblée  
**Deadline approximative :** mardi 22 septembre 2026 (7 jours depuis le mail du 15)  
**Stack du stage :** React · TypeScript · Node.js · JavaScript · MySQL · Redis

---

## Comment utiliser ce document

1. Lis une section pendant une pause (10–20 min).
2. Fais les exercices **à la main** (papier, Notes, ou IDE).
3. Coche les cases ☐ quand c’est fait.
4. Ne vise pas la perfection : vise **un code qui marche + lisible**.

**Règle d’or :** 80 % du temps sur JS/TS + React + petit Node.  
Redis / WebSocket = notions seulement.

---

## Plan des 3 jours

| Jour | Focus | Durée conseillée | Fait ? |
|------|--------|------------------|--------|
| **J1** | JavaScript / TypeScript | 2–3 h | ☐ |
| **J2** | React (state, listes, formulaires) | 2–3 h | ☐ |
| **J3** | Mini sujet Winamax + Node léger | 2–3 h | ☐ |
| **J4** | Passage du test Coderpad | 1–2 h | ☐ |
| **J5** | Marge / rattrapage | — | ☐ |

Date prévue du test : _______________  
Heure : _______________

---

# PARTIE 0 — Ce que Winamax attend vraiment

### Le sujet du stage (à avoir en tête)
Ils veulent un format riche (pas une notif) :
- composants interactifs
- lecteur vidéo
- réactions synchronisées (temps réel)
- état de consultation : **vu / pas vu / repris en cours**
- back-office éditorial (équipes non tech)
- métriques : ouvertures, complétion, décrochage

### Ce qu’un Coderpad teste souvent
- lire un énoncé et découper le problème
- manipuler des données (tableaux / objets)
- faire une UI React simple
- éventuellement 1–2 fonctions backend
- gérer les cas limites (liste vide, id inconnu…)

### Ce qu’ils ne te demanderont probablement PAS
- un monolithe Redis ultra avancé
- Kubernetes
- algorithmes de concours très durs
- connaître tout le métier poker/paris

**Notes perso :**
_______________________________________________
_______________________________________________

---

# PARTIE 1 — JavaScript / TypeScript (JOUR 1)

## 1.1 Les bases à maîtriser absolument

### Tableaux
```js
const items = [
  { id: 1, title: "Promo poker", status: "unread" },
  { id: 2, title: "Replay match", status: "watching" },
  { id: 3, title: "Bonus", status: "seen" },
];

items.map(i => i.title)
items.filter(i => i.status === "unread")
items.find(i => i.id === 2)
items.some(i => i.status === "watching")
items.every(i => i.id > 0)
items.reduce((acc, i) => acc + 1, 0)
```

### Objets
```js
const user = { id: 10, name: "Wadjoud" };
const updated = { ...user, name: "Wadjoud P." }; // copie + modif
const { id, name } = user; // destructuring
```

### Async / await
```js
async function loadContents() {
  try {
    const res = await fetch("/api/contents");
    const data = await res.json();
    return data;
  } catch (e) {
    console.error(e);
    return [];
  }
}
```

### TypeScript utile (pas besoin d’être expert)
```ts
type Status = "unread" | "watching" | "seen";

interface Content {
  id: number;
  title: string;
  status: Status;
  progress: number; // 0 à 100
}

function markSeen(c: Content): Content {
  return { ...c, status: "seen", progress: 100 };
}
```

☐ J’ai relu cette section  
☐ Je comprends map / filter / find  
☐ Je comprends async/await  
☐ Je comprends un `type` / `interface` simple

**Notes :**
_______________________________________________
_______________________________________________

---

## 1.2 Exercices JS/TS (fais-les vraiment)

### Exercice A — Filtrer les non lus
Données :
```js
const contents = [
  { id: 1, title: "A", status: "unread", progress: 0 },
  { id: 2, title: "B", status: "watching", progress: 40 },
  { id: 3, title: "C", status: "seen", progress: 100 },
  { id: 4, title: "D", status: "unread", progress: 0 },
];
```
**Consigne :** retourne uniquement les contenus `unread`.

**Ta solution :**
```js




```

**Correction :**
```js
const unread = contents.filter(c => c.status === "unread");
```

☐ Fait

---

### Exercice B — Compter par statut
**Consigne :** retourne un objet `{ unread: X, watching: Y, seen: Z }`.

**Ta solution :**
```js




```

**Correction :**
```js
const counts = contents.reduce(
  (acc, c) => {
    acc[c.status] = (acc[c.status] || 0) + 1;
    return acc;
  },
  { unread: 0, watching: 0, seen: 0 }
);
```

☐ Fait

---

### Exercice C — Marquer un contenu comme vu
**Consigne :** fonction `markAsSeen(list, id)` qui renvoie une **nouvelle** liste (sans muter l’ancienne), avec le contenu `id` passé à `seen` / `progress: 100`. Si id introuvable, renvoyer la liste telle quelle.

**Ta solution :**
```js




```

**Correction :**
```js
function markAsSeen(list, id) {
  return list.map(c =>
    c.id === id ? { ...c, status: "seen", progress: 100 } : c
  );
}
```

☐ Fait

---

### Exercice D — Reprendre en cours
**Consigne :** `updateProgress(list, id, progress)`  
- si `progress <= 0` → `unread`  
- si `0 < progress < 100` → `watching`  
- si `progress >= 100` → `seen` + progress = 100

**Ta solution :**
```js




```

**Correction :**
```js
function updateProgress(list, id, progress) {
  return list.map(c => {
    if (c.id !== id) return c;
    const p = Math.max(0, Math.min(100, progress));
    let status = "watching";
    if (p <= 0) status = "unread";
    if (p >= 100) status = "seen";
    return { ...c, progress: p, status };
  });
}
```

☐ Fait

---

### Exercice E — Async simple
**Consigne :** écris une fonction async `getTitle(id)` qui :
1. attend une Promise factice `fakeApi(id)` 
2. renvoie `data.title`
3. si erreur, renvoie `"Erreur"`

```js
function fakeApi(id) {
  return new Promise((resolve, reject) => {
    if (id === 0) reject(new Error("boom"));
    else resolve({ id, title: "Contenu " + id });
  });
}
```

**Ta solution :**
```js




```

**Correction :**
```js
async function getTitle(id) {
  try {
    const data = await fakeApi(id);
    return data.title;
  } catch {
    return "Erreur";
  }
}
```

☐ Fait

**Score Jour 1 :** ___ / 5 exercices  
**Ce qui bloque encore :**
_______________________________________________

---

# PARTIE 2 — React (JOUR 2)

## 2.1 Le minimum vital React

### Composant + state
```tsx
import { useState } from "react";

export function Counter() {
  const [n, setN] = useState(0);
  return (
    <button onClick={() => setN(n + 1)}>
      Cliqué {n} fois
    </button>
  );
}
```

### Liste
```tsx
function ContentList({ items }) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{item.title}</li>
      ))}
    </ul>
  );
}
```
⚠️ Toujours un `key` unique (souvent `id`).

### Formulaire contrôlé
```tsx
function Search() {
  const [q, setQ] = useState("");
  return (
    <input
      value={q}
      onChange={e => setQ(e.target.value)}
      placeholder="Rechercher..."
    />
  );
}
```

### useEffect (bases)
```tsx
useEffect(() => {
  // s'exécute au montage
  console.log("mounted");
}, []);
```

### Afficher selon un état
```tsx
function Badge({ status }) {
  if (status === "unread") return <span>Non vu</span>;
  if (status === "watching") return <span>En cours</span>;
  return <span>Vu</span>;
}
```

☐ Section lue  
☐ Je sais faire useState  
☐ Je sais afficher une liste avec key  
☐ Je sais faire un input contrôlé

**Notes :**
_______________________________________________
_______________________________________________

---

## 2.2 Exercices React

### Exercice F — Liste de contenus + badge
Crée un composant qui affiche :
- titre
- badge selon status (`unread` / `watching` / `seen`)
- barre simple de progression (texte `40%` suffit)

**Données initiales :**
```ts
const initial = [
  { id: 1, title: "Story poker", status: "unread", progress: 0 },
  { id: 2, title: "Interview coach", status: "watching", progress: 55 },
  { id: 3, title: "Bonus hebdo", status: "seen", progress: 100 },
];
```

**Ta solution (brouillon) :**
```tsx




```

**Correction (version simple) :**
```tsx
function Contents() {
  const [items] = useState(initial);

  return (
    <ul>
      {items.map(c => (
        <li key={c.id}>
          <strong>{c.title}</strong> — {c.status} — {c.progress}%
        </li>
      ))}
    </ul>
  );
}
```

☐ Fait

---

### Exercice G — Bouton “Marquer comme vu”
Ajoute un bouton par item qui passe le contenu en `seen` / `100`.

**Ta solution :**
```tsx




```

**Correction :**
```tsx
function Contents() {
  const [items, setItems] = useState(initial);

  function markSeen(id: number) {
    setItems(prev =>
      prev.map(c =>
        c.id === id ? { ...c, status: "seen", progress: 100 } : c
      )
    );
  }

  return (
    <ul>
      {items.map(c => (
        <li key={c.id}>
          {c.title} ({c.status})
          <button onClick={() => markSeen(c.id)}>Vu</button>
        </li>
      ))}
    </ul>
  );
}
```

☐ Fait

---

### Exercice H — Filtre “Non lus seulement”
Checkbox ou bouton qui filtre l’affichage.

**Idée :**
```tsx
const [onlyUnread, setOnlyUnread] = useState(false);
const visible = onlyUnread
  ? items.filter(c => c.status === "unread")
  : items;
```

**Ta solution :**
```tsx




```

☐ Fait

---

### Exercice I — Mini lecteur (sans vraie vidéo)
State : `playing` (bool) + `progress` (0–100)  
Boutons : Play / Pause / +10% / Reset  
Si progress arrive à 100 → status `seen`.

**Ta solution :**
```tsx




```

**Correction simplifiée :**
```tsx
function Player() {
  const [playing, setPlaying] = useState(false);
  const [progress, setProgress] = useState(0);

  function add10() {
    setProgress(p => Math.min(100, p + 10));
  }

  return (
    <div>
      <p>{playing ? "Lecture" : "Pause"} — {progress}%</p>
      <button onClick={() => setPlaying(true)}>Play</button>
      <button onClick={() => setPlaying(false)}>Pause</button>
      <button onClick={add10}>+10%</button>
      <button onClick={() => { setPlaying(false); setProgress(0); }}>
        Reset
      </button>
    </div>
  );
}
```

☐ Fait

**Score Jour 2 :** ___ / 4  
**Ce qui bloque encore :**
_______________________________________________

---

# PARTIE 3 — Node.js léger + modèle data (JOUR 3)

## 3.1 Backend minimal

Même sans Express ultra complet, sache écrire la **logique** :

```js
// "base de données" en mémoire pour un test
let contents = [
  { id: 1, title: "A", status: "unread", progress: 0 },
];

function listContents() {
  return contents;
}

function getContent(id) {
  return contents.find(c => c.id === Number(id)) || null;
}

function createContent(title) {
  const item = {
    id: Date.now(),
    title,
    status: "unread",
    progress: 0,
  };
  contents.push(item);
  return item;
}
```

### Si Express est dispo dans le pad
```js
app.get("/contents", (req, res) => {
  res.json(listContents());
});

app.post("/contents", (req, res) => {
  const { title } = req.body;
  if (!title) return res.status(400).json({ error: "title required" });
  res.status(201).json(createContent(title));
});

app.patch("/contents/:id/progress", (req, res) => {
  const { progress } = req.body;
  contents = updateProgress(contents, Number(req.params.id), progress);
  res.json(getContent(req.params.id));
});
```

☐ Section lue

---

## 3.2 MySQL — juste l’essentiel

### Tables mentales (sujet Winamax)
```sql
-- contenus éditoriaux
CREATE TABLE contents (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  video_url VARCHAR(500),
  created_at DATETIME
);

-- état de consultation PAR utilisateur
CREATE TABLE user_views (
  user_id INT NOT NULL,
  content_id INT NOT NULL,
  status ENUM('unread','watching','seen') DEFAULT 'unread',
  progress INT DEFAULT 0,
  opened_at DATETIME,
  completed_at DATETIME,
  PRIMARY KEY (user_id, content_id)
);
```

### Requêtes utiles
```sql
-- non lus d'un user
SELECT c.*
FROM contents c
LEFT JOIN user_views uv
  ON uv.content_id = c.id AND uv.user_id = 42
WHERE uv.status IS NULL OR uv.status = 'unread';

-- marquer vu
INSERT INTO user_views (user_id, content_id, status, progress, completed_at)
VALUES (42, 1, 'seen', 100, NOW())
ON DUPLICATE KEY UPDATE status='seen', progress=100, completed_at=NOW();
```

☐ J’ai compris le modèle `contents` + `user_views`

**Notes :**
_______________________________________________

---

## 3.3 Redis — 10 minutes chrono (pas plus)

Redis = cache clé → valeur, très rapide.

| Besoin | Idée Redis |
|--------|------------|
| Historique dernières recherches | liste `search:user:42` |
| Suggestions tendances | clé `trending` avec JSON |
| Compteur d’ouvertures | `INCR content:1:opens` |

Commandes :
```
SET user:42:last_content 15
GET user:42:last_content
INCR content:15:opens
LPUSH search:42 "poker"
LTRIM search:42 0 9
LRANGE search:42 0 9
```

Pour le test : savoir **expliquer** Redis suffit souvent.  
Coder Redis n’est indispensable que s’ils le demandent.

☐ Lu

---

## 3.4 Temps réel (notions 5 min)

- **HTTP classique** : demande → réponse
- **WebSocket** : connexion ouverte, messages dans les deux sens
- Cas Winamax : réactions synchronisées entre users

Tu peux juste écrire en commentaire :
```js
// Idealement: broadcast reaction via WebSocket aux viewers du même contentId
```

☐ Lu

---

## 3.5 Mini-projet du Jour 3 (LE PLUS IMPORTANT)

### Brief (comme un mini Coderpad)
> Construire une petite app “Stories Winamax” :
> 1. Liste de contenus avec statut
> 2. Bouton Play qui passe en `watching` et augmente la progression
> 3. À 100% → `seen`
> 4. Filtre “non lus”
> 5. (Bonus) fonction backend `POST /contents` + `PATCH /contents/:id/progress`
> 6. (Bonus) compteur d’ouvertures

### Checklist de livraison
☐ Liste affichée  
☐ Badge statut  
☐ Progression  
☐ Marquer vu  
☐ Filtre non lus  
☐ Cas liste vide géré (`Aucun contenu`)  
☐ Code lisible (noms clairs)  
☐ Bonus API  
☐ Bonus compteur

### Espace architecture (dessine / écris)
```
Composants :
- App
- ContentList
- ContentItem
- Player
- FilterBar

State global (où ?) :
_________________________________

Fonctions pures (hors React) :
- updateProgress
- markAsSeen
- countByStatus
```

### Metrics (vocabulaire stage)
| Métrique | Signification simple |
|----------|----------------------|
| Ouverture | user a ouvert le contenu |
| Complétion | progress = 100 / status = seen |
| Décrochage | ouvert puis abandon < 100 |

☐ Mini-projet terminé (même version simple)

**Temps passé Jour 3 :** _____  
**Ce qui marche :** ____________________________  
**Ce qui coince :** ____________________________

---

# PARTIE 4 — Cas limites (ils adorent ça)

Coche et prépare une réponse / un if :

☐ Liste vide → message “Aucun contenu”  
☐ id introuvable → ne crash pas  
☐ progress < 0 ou > 100 → clamp 0..100  
☐ title vide à la création → erreur 400 / message  
☐ double clic “Vu” → OK, reste seen  
☐ filtre actif + plus aucun unread → message dédié  
☐ réseau lent (si fetch) → loading / erreur simple

**Snippet clamp :**
```js
const p = Math.max(0, Math.min(100, progress));
```

---

# PARTIE 5 — Stratégie le jour J (Coderpad)

## Avant de coder (3 minutes)
1. Lis **tout** l’énoncé.
2. Liste les features obligatoires vs bonus.
3. Choisis la version simple qui marche.
4. Écris 3 lignes de plan en commentaire.

```js
// Plan:
// 1) modèle Content
// 2) liste + state
// 3) markSeen / progress
// 4) filtre
// 5) bonus API si temps
```

## Pendant
- Fais marcher le **happy path** d’abord
- Puis cas limites
- Noms clairs : `markAsSeen`, `onlyUnread`, `progress`
- Si bloqué > 8 min : simplifie et avance

## À la fin (5 min)
- Relis
- Teste id invalide / liste vide
- Supprime le code mort
- Laisse un court commentaire sur ce que tu ferais ensuite (WebSocket, Redis…)

## Checklist départ test
☐ Lien Coderpad trouvé (hors spam)  
☐ Navigateur à jour  
☐ Casque / calme  
☐ Eau  
☐ Cette fiche ouverte à côté (Partie 1–2–5)  
☐ Timer : ne pas commencer à 23h le dernier jour

**Date/heure choisie pour passer le test :** _______________

---

# PARTIE 6 — Antisèche ultra courte (à revoir 10 min avant)

### États consultation
`unread` → `watching` → `seen`

### updateProgress
```js
function updateProgress(list, id, progress) {
  return list.map(c => {
    if (c.id !== id) return c;
    const p = Math.max(0, Math.min(100, progress));
    const status = p <= 0 ? "unread" : p >= 100 ? "seen" : "watching";
    return { ...c, progress: p, status };
  });
}
```

### React mark seen
```tsx
setItems(prev =>
  prev.map(c => c.id === id ? { ...c, status: "seen", progress: 100 } : c)
);
```

### Filtre
```tsx
const visible = onlyUnread
  ? items.filter(c => c.status === "unread")
  : items;
```

### API Express mini
```js
app.get("/contents", (req, res) => res.json(contents));
app.post("/contents", (req, res) => {
  if (!req.body.title) return res.status(400).json({ error: "title required" });
  // create...
});
```

### Redis en une phrase
“Je mettrais le cache des tendances / historique de recherche dans Redis, et le durable (statuts users) en MySQL.”

---

# PARTIE 7 — Suivi perso

### Après chaque jour
| Jour | Faits | Difficulté /10 | Commentaire |
|------|-------|----------------|-------------|
| J1 JS/TS | ☐ | __ | |
| J2 React | ☐ | __ | |
| J3 Mini projet | ☐ | __ | |
| Test passé | ☐ | __ | |

### Après le test (à remplir)
Heure de début : _____  
Heure de fin : _____  
Ce qui était demandé :  
_______________________________________________  
_______________________________________________  
Ce qui m’a bloqué :  
_______________________________________________  
Ce que j’ai bien géré :  
_______________________________________________

---

## Mot de la fin

Tu n’as pas besoin d’une formation complète.  
Tu as besoin de **répéter 10 patterns** jusqu’à ce que ce soit automatique :

1. filter / map  
2. update immuable d’une liste  
3. useState  
4. liste + key  
5. input contrôlé  
6. badge selon status  
7. progress clamp 0..100  
8. petit plan avant de coder  
9. cas liste vide  
10. une phrase claire sur Redis / WS

**3 jours ciblés > 10 jours de tutoriels passifs.**

Force — tu peux le faire.

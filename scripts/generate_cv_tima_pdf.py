#!/usr/bin/env python3
"""Génère assets/cv-tima.pdf (PDF A4, Helvetica, sans dépendances)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-tima.pdf"


def esc(s: str) -> str:
    return (
        s.encode("latin-1", "replace").decode("latin-1")
        .replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )


class PDF:
    def __init__(self):
        self.lines = []
        self.y = 820  # points from bottom (A4 ~842)
        self.page_w = 595
        self.margin = 36
        self.content = []

    def set_y(self, y):
        self.y = y

    def text(self, x, size, string, bold=False):
        font = "F2" if bold else "F1"
        self.content.append(f"BT /{font} {size} Tf {x:.1f} {self.y:.1f} Td ({esc(string)}) Tj ET")

    def text_right(self, size, string, bold=False):
        # approximate width: 0.5 * size * len for Helvetica
        w = 0.48 * size * len(string)
        x = self.page_w - self.margin - w
        self.text(x, size, string, bold=bold)

    def multilines(self, size, text, leading=None, bold=False, max_chars=95):
        leading = leading or size + 2
        words = text.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if len(test) > max_chars:
                self.text(self.margin, size, line, bold=bold)
                self.y -= leading
                line = w
            else:
                line = test
        if line:
            self.text(self.margin, size, line, bold=bold)
            self.y -= leading

    def rule(self, color=(0.22, 0.19, 0.64), thickness=1.2):
        r, g, b = color
        self.content.append(f"{r} {g} {b} RG {thickness} w {self.margin} {self.y} m {self.page_w - self.margin} {self.y} l S")
        self.y -= 10

    def space(self, n=8):
        self.y -= n

    def section(self, title):
        self.space(4)
        self.text(self.margin, 10, title.upper(), bold=True)
        self.y -= 4
        self.rule(color=(0.82, 0.84, 0.86), thickness=0.6)
        self.space(2)

    def build(self) -> bytes:
        stream = ("\n".join(self.content) + "\n").encode("latin-1", "replace")
        objects = [
            b"1 0 obj<< /Type /Catalog /Pages 2 0 R >>endobj\n",
            b"2 0 obj<< /Type /Pages /Kids [3 0 R] /Count 1 >>endobj\n",
            (
                b"3 0 obj<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>endobj\n"
            ),
            b"4 0 obj<< /Length %d >>stream\n" % len(stream) + stream + b"endstream\nendobj\n",
            b"5 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>endobj\n",
            b"6 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>endobj\n",
        ]

        out = bytearray(b"%PDF-1.4\n")
        offsets = [0]
        for obj in objects:
            offsets.append(len(out))
            out.extend(obj)
        xref_pos = len(out)
        out.extend(f"xref\n0 {len(offsets)}\n".encode())
        out.extend(b"0000000000 65535 f \n")
        for off in offsets[1:]:
            out.extend(f"{off:010d} 00000 n \n".encode())
        out.extend(
            f"trailer<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode()
        )
        return bytes(out)


def main():
    p = PDF()
    m = p.margin

    # Header
    p.text(m, 18, "Wadjoud PHILIPPE", bold=True)
    p.y -= 16
    p.text(m, 11, "Eleve Ingenieur - Developpeur Full Stack / IA", bold=True)
    p.y -= 13
    p.text(m, 9, "Stage de fin d'etudes (fev. 2027) - Mobilite Paris - ESIGELEC Rouen")
    p.y -= 12
    p.text(m, 8, "wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39")
    p.y -= 10
    p.text(m, 8, "https://wadjoud-star.github.io/portfolio/  |  linkedin.com/in/wadjoud-philippe")
    p.y -= 10
    p.text(m, 8, "github.com/Wadjoud-star")
    p.y -= 8
    p.rule()

    p.section("Profil")
    p.multilines(
        8,
        "Eleve ingenieur bac+5 (ESIGELEC, developpement web full stack), je concoois des applications web "
        "de bout en bout : analyse metier, developpement Java / Spring & React, API REST, Docker et deploiement. "
        "Interesse par l'IA appliquee aux processus metier (OpenAI, generation de contenu, automatisation), "
        "les plateformes multi-roles (droits, admin, workflows) et les produits en production. "
        "Recherche un stage de fin d'etudes de 6 mois a partir de fevrier 2027 - profil autonome, Agile/Scrum, "
        "force de proposition, a l'aise en equipe produit.",
        leading=10,
        max_chars=98,
    )

    p.section("Competences techniques")
    skills = [
        ("Backend", "Java (JEE, Spring Boot), Kotlin (bases), Node.js, Express, PHP (MVC), C#, Python - API REST, JWT, Swagger"),
        ("Frontend", "React, Next.js, Angular, TypeScript, JavaScript, HTML5, CSS3, Tailwind, Bootstrap - UX, dashboards, multi-roles"),
        ("IA & Donnees", "OpenAI (API), LangChain (notions), generation de contenu IA, PostgreSQL, MySQL, Prisma, Oracle SQL"),
        ("DevOps & Methodes", "Docker, Kubernetes (notions), Git, CI/CD (GitLab), Linux, Agile/Scrum, securite (roles & droits)"),
    ]
    for title, txt in skills:
        p.text(m, 9, title, bold=True)
        p.y -= 11
        p.multilines(8, txt, leading=10, max_chars=100)
        p.space(2)

    p.section("Projets significatifs")
    projects = [
        (
            "Smart CMS IA - Generation de contenu & OpenAI",
            "2025",
            "CMS intelligent : generation IA (blog, LinkedIn, Twitter/X, illustration) via OpenAI, jobs asynchrones, editeur riche, score SEO, auth et historique.",
            "Next.js / React / OpenAI / Supabase / Stripe / TipTap / TypeScript",
        ),
        (
            "Beniphone - Marketplace multi-roles (processus & admin)",
            "2025",
            "Plateforme full-stack : catalogue, KYC vendeur, messagerie/negociation, transactions, moderation et dashboard admin. Roles et workflows metier.",
            "React / Node.js / Express / Prisma / MySQL / Tailwind / Agile",
        ),
        (
            "Factis - Mini-SaaS (droits, abonnements, production)",
            "2025",
            "SaaS de facturation France/Benin : onboarding, clients, factures PDF, analytics, Stripe, roles et conformite. Produit, API et deploiement.",
            "Next.js / TypeScript / Prisma / PostgreSQL / Stripe / Docker",
        ),
        (
            "Club Sport - Application Java multi-roles",
            "2025",
            "App JEE : recherche, cartographie, statistiques, exports CSV, espaces elu/club. Docker et Tomcat.",
            "Java / JSP-Servlets / MySQL / Docker / Tomcat",
        ),
        (
            "Mon Demenagement - Plateforme web en production",
            "2025",
            "Mise en relation clients/demenageurs : annonces, offres, messagerie, evaluations, admin. Analyse -> MVC -> production.",
            "PHP / MySQL / MVC / Bootstrap / JavaScript / Git",
        ),
    ]
    for title, date, desc, stack in projects:
        p.text(m, 9, title, bold=True)
        p.text_right(8, date, bold=True)
        p.y -= 11
        p.multilines(8, desc, leading=10, max_chars=100)
        p.text(m, 8, stack, bold=True)
        p.y -= 12

    p.section("Formation")
    p.text(m, 9, "Diplome d'Ingenieur - Dev Web Full Stack", bold=True)
    p.text_right(8, "2024 - 2027", bold=True)
    p.y -= 11
    p.text(m, 8, "ESIGELEC - Rouen", bold=True)
    p.y -= 10
    p.multilines(8, "Java, Spring, Angular, TypeScript, React, Docker, API REST, Agile/Scrum", leading=10)
    p.text(m, 9, "Cycle preparatoire integre", bold=True)
    p.text_right(8, "2022 - 2024", bold=True)
    p.y -= 11
    p.text(m, 8, "ESIGELEC - Cotonou, Benin", bold=True)
    p.y -= 12

    p.section("Experience")
    p.text(m, 9, "Stagiaire Informatique", bold=True)
    p.text_right(8, "Juil. - Aout 2023", bold=True)
    p.y -= 11
    p.text(m, 8, "PROMOPHARMA - Benin", bold=True)
    p.y -= 10
    p.multilines(8, "Recueil des besoins, diagnostic d'incidents, maintenance parc informatique et serveurs.", leading=10)

    p.section("Langues / Qualites / Centres d'interet")
    p.multilines(8, "Francais - langue maternelle  |  Anglais - B2 (docs techniques, specs)", leading=10)
    p.multilines(8, "Autonome / Force de proposition / Esprit d'equipe / Agile", leading=10)
    p.multilines(8, "IA appliquee & agents / LLM  ·  Produits SaaS & apps metier  ·  Open source / GitHub", leading=10)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = p.build()
    OUT.write_bytes(data)
    print(f"Wrote {OUT} ({len(data)} bytes), y_end={p.y:.0f}")


if __name__ == "__main__":
    main()

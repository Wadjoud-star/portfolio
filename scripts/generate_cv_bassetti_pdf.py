#!/usr/bin/env python3
"""Génère assets/cv-bassetti.pdf — CV BASSETTI (Développement & Intégration)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-bassetti.pdf"
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

ACCENT = (67, 56, 168)
ACCENT_DARK = (55, 48, 163)
TEXT = (17, 24, 39)
MUTED = (74, 85, 104)
LIGHT = (107, 114, 128)
RULE = (211, 211, 215)


class CV(FPDF):
    def __init__(self):
        super().__init__(format="A4", unit="mm")
        self.set_auto_page_break(auto=False)
        self.add_font("ArialU", "", FONT)
        self.add_font("ArialU", "B", FONT_BOLD)
        self.set_margins(12, 11, 12)
        self.add_page()

    def h1(self, s):
        self.set_font("ArialU", "B", 17.5)
        self.set_text_color(*TEXT)
        self.cell(0, 7.5, s, new_x="LMARGIN", new_y="NEXT")

    def role(self, s):
        self.set_font("ArialU", "B", 10.5)
        self.set_text_color(*ACCENT)
        self.cell(0, 5.5, s, new_x="LMARGIN", new_y="NEXT")

    def muted_line(self, s, size=8.2):
        self.set_font("ArialU", "", size)
        self.set_text_color(*MUTED)
        self.cell(0, 4.6, s, new_x="LMARGIN", new_y="NEXT")

    def contact(self, s):
        self.set_font("ArialU", "", 7.8)
        self.set_text_color(*ACCENT_DARK)
        self.cell(0, 4.2, s, new_x="LMARGIN", new_y="NEXT")

    def rule(self, thick=0.75):
        self.set_draw_color(*ACCENT)
        self.set_line_width(thick)
        y = self.get_y() + 1.2
        self.line(12, y, 198, y)
        self.set_y(y + 2.5)

    def thin_rule(self):
        self.set_draw_color(*RULE)
        self.set_line_width(0.2)
        y = self.get_y()
        self.line(12, y, 198, y)
        self.set_y(y + 1.8)

    def section(self, title):
        self.ln(2)
        self.set_font("ArialU", "B", 9.5)
        self.set_text_color(*ACCENT)
        self.cell(0, 4.5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.thin_rule()

    def para(self, s):
        self.set_font("ArialU", "", 7.8)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 3.9, s)

    def skill_grid(self, skills):
        col_w = 90
        gap = 6
        x0 = 12
        y0 = self.get_y()
        bottoms = []
        for i, (title, body) in enumerate(skills[:2]):
            x = x0 + i * (col_w + gap)
            self.set_xy(x, y0)
            self.set_font("ArialU", "B", 8.2)
            self.set_text_color(*TEXT)
            self.cell(col_w, 4.2, title, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x)
            self.set_font("ArialU", "", 7.3)
            self.set_text_color(*MUTED)
            self.multi_cell(col_w, 3.6, body)
            bottoms.append(self.get_y())
        y1 = max(bottoms) + 1.5
        bottoms = []
        for i, (title, body) in enumerate(skills[2:]):
            x = x0 + i * (col_w + gap)
            self.set_xy(x, y1)
            self.set_font("ArialU", "B", 8.2)
            self.set_text_color(*TEXT)
            self.cell(col_w, 4.2, title, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x)
            self.set_font("ArialU", "", 7.3)
            self.set_text_color(*MUTED)
            self.multi_cell(col_w, 3.6, body)
            bottoms.append(self.get_y())
        self.set_y(max(bottoms) + 0.5)
        self.set_x(12)

    def project(self, title, date, bullets, stack):
        self.set_font("ArialU", "B", 8.2)
        self.set_text_color(*TEXT)
        self.cell(152, 4.2, title)
        self.set_font("ArialU", "B", 7.2)
        self.set_text_color(*LIGHT)
        self.cell(0, 4.2, date, align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_font("ArialU", "", 7.5)
        self.set_text_color(*MUTED)
        for b in bullets:
            x = self.l_margin
            self.set_x(x)
            self.cell(3.5, 3.8, "-")
            self.set_x(x + 4.5)
            self.multi_cell(self.epw - 4.5, 3.8, b)
        self.set_x(self.l_margin)
        self.set_font("ArialU", "B", 7)
        self.set_text_color(*ACCENT)
        self.cell(0, 3.8, stack, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.9)

    def labeled(self, label, body):
        self.set_font("ArialU", "B", 7.8)
        self.set_text_color(*TEXT)
        self.cell(0, 3.9, label, new_x="LMARGIN", new_y="NEXT")
        self.set_font("ArialU", "", 7.4)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 3.8, body)
        self.ln(0.7)

    def job_header(self, title, date):
        self.set_font("ArialU", "B", 8.2)
        self.set_text_color(*TEXT)
        self.cell(152, 4.2, title)
        self.set_font("ArialU", "B", 7.2)
        self.set_text_color(*LIGHT)
        self.cell(0, 4.2, date, align="R", new_x="LMARGIN", new_y="NEXT")

    def company(self, s):
        self.set_font("ArialU", "B", 7.8)
        self.set_text_color(*ACCENT)
        self.cell(0, 3.8, s, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, s):
        self.set_font("ArialU", "", 7.5)
        self.set_text_color(*MUTED)
        x = self.l_margin
        self.set_x(x)
        self.cell(3.5, 3.8, "-")
        self.set_x(x + 4.5)
        self.multi_cell(self.epw - 4.5, 3.8, s)
        self.set_x(self.l_margin)


def main():
    pdf = CV()
    pdf.h1("Wadjoud PHILIPPE")
    pdf.role("Élève ingénieur — Développement & Intégration · solutions métier")
    pdf.muted_line(
        "Stage fin d'études 6 mois (fév. 2027) · ESIGELEC Rouen · BASSETTI — Dev & Intégration"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  ·  07 58 03 02 39")
    pdf.contact("Portfolio : https://wadjoud-star.github.io/portfolio/")
    pdf.contact(
        "linkedin.com/in/wadjoud-philippe  ·  github.com/Wadjoud-star"
    )
    pdf.rule()

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 à l'ESIGELEC (Rouen). Curieux, rigoureux, autonome, "
        "esprit d'équipe et entrepreneurial. J'aime comprendre les usages métier d'un client, "
        "formaliser un besoin, développer une solution à partir de briques existantes, "
        "et l'intégrer dans un logiciel déjà en place. Solides bases POO, langages web "
        "(JavaScript, CSS, HTML), SQL ; C# / ASP.NET (formation), Angular (formation). "
        "Créatif et structuré, motivé pour proposer des solutions techniques adaptées. "
        "Stage de fin d'études 6 mois dès février 2027."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            (
                "POO & back",
                "Programmation objet (Java, C# / .NET formation), logique métier, intégration",
            ),
            (
                "Langages web",
                "JavaScript, jQuery (bases), CSS, HTML, ASP.NET / ASP(x) (formation), TypeScript",
            ),
            (
                "Données & serveur",
                "SQL (MySQL, PostgreSQL), Windows Server / IIS / LDAP (notions), Angular (formation)",
            ),
            (
                "Méthode",
                "Cahier des charges (approche), Git, autonomie, collab client / équipe, créativité",
            ),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Mon Déménagement — Solution métier intégrée (prod)",
            "2025",
            [
                "Compréhension des usages, évolutions sur un logiciel déjà installé / en prod",
                "Correctifs, features, fiabilisation — autonomie et sens du service client",
            ],
            "PHP · MySQL · JavaScript · CSS · Git",
        ),
        (
            "Factis — Besoin → solution technique complète",
            "2025",
            [
                "Formalisation des besoins, développement à partir de composants existants (stack web)",
                "Intégration front/back/BDD, livraison itérative",
            ],
            "TypeScript · React · Node.js · PostgreSQL · SQL · Git · CI",
        ),
        (
            "Club Sport — POO Java · logique métier multi-rôles",
            "2025",
            [
                "Analyse métier, développement structuré, SQL, packaging — esprit d'équipe Agile",
            ],
            "Java · POO · MySQL · Docker · Git · Agile",
        ),
        (
            "Beniphone — Web JS + collab",
            "2025",
            [
                "Interfaces web, APIs, travail en équipe, intégration des retours",
            ],
            "JavaScript · React · CSS · MySQL · Git",
        ),
        (
            "Smart CMS IA — Créativité & nouvelles technologies",
            "2025",
            [
                "Exploration technique, propositions d'amélioration, documentation",
            ],
            "JavaScript · TypeScript · React · Git · CI",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur — Dev Web / Génie logiciel", "2024 – 2027")
    pdf.company("ESIGELEC — Rouen")
    pdf.para(
        "POO, JavaScript, CSS, SQL, C# / ASP.NET (formation), Angular (formation), "
        "Git, Agile, anglais technique"
    )
    pdf.ln(0.8)
    pdf.job_header("Cycle préparatoire intégré", "2022 – 2024")
    pdf.company("ESIGELEC — Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. – Août 2023")
    pdf.company("PROMOPHARMA — Bénin")
    pdf.bullet("Autonomie, relation client / métiers, rigueur, esprit d'équipe")

    pdf.section("Langues & disponibilité")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  ·  Anglais : B2 (docs techniques, specs)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage fin d'études 6 mois dès février 2027  ·  Convention + gratification",
    )
    pdf.labeled(
        "Portfolio",
        "https://wadjoud-star.github.io/portfolio/  — projets et détails techniques",
    )
    pdf.labeled(
        "Ce qui m'intéresse chez BASSETTI",
        "Cahier des charges client  ·  solutions sur composants existants  ·  intégration logiciel  ·  métier",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), y={pdf.get_y():.1f}")


if __name__ == "__main__":
    main()

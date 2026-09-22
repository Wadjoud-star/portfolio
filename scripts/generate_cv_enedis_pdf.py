#!/usr/bin/env python3
"""Génère assets/cv-enedis.pdf — CV Enedis (Python/Django, Java, React, PostGIS/géo)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-enedis.pdf"
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
        self.set_margins(12, 12, 12)
        self.add_page()

    def h1(self, s):
        self.set_font("ArialU", "B", 18)
        self.set_text_color(*TEXT)
        self.cell(0, 8, s, new_x="LMARGIN", new_y="NEXT")

    def role(self, s):
        self.set_font("ArialU", "B", 11)
        self.set_text_color(*ACCENT)
        self.cell(0, 6, s, new_x="LMARGIN", new_y="NEXT")

    def muted_line(self, s, size=8.5):
        self.set_font("ArialU", "", size)
        self.set_text_color(*MUTED)
        self.cell(0, 5, s, new_x="LMARGIN", new_y="NEXT")

    def contact(self, s):
        self.set_font("ArialU", "", 8)
        self.set_text_color(*ACCENT_DARK)
        self.cell(0, 4.5, s, new_x="LMARGIN", new_y="NEXT")

    def rule(self, thick=0.7):
        self.set_draw_color(*ACCENT)
        self.set_line_width(thick)
        y = self.get_y() + 1.5
        self.line(12, y, 198, y)
        self.set_y(y + 3)

    def thin_rule(self):
        self.set_draw_color(*RULE)
        self.set_line_width(0.2)
        y = self.get_y()
        self.line(12, y, 198, y)
        self.set_y(y + 2)

    def section(self, title):
        self.ln(2.5)
        self.set_font("ArialU", "B", 10)
        self.set_text_color(*ACCENT)
        self.cell(0, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.thin_rule()

    def para(self, s):
        self.set_font("ArialU", "", 8)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 4.2, s)

    def skill_grid(self, skills):
        col_w = 90
        gap = 6
        x0 = 12
        y0 = self.get_y()
        for i, (title, body) in enumerate(skills[:2]):
            x = x0 + i * (col_w + gap)
            self.set_xy(x, y0)
            self.set_font("ArialU", "B", 8.5)
            self.set_text_color(*TEXT)
            self.cell(col_w, 4.5, title, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x)
            self.set_font("ArialU", "", 7.5)
            self.set_text_color(*MUTED)
            self.multi_cell(col_w, 3.8, body)
        y1 = self.get_y()
        for i, (title, body) in enumerate(skills[2:]):
            x = x0 + i * (col_w + gap)
            self.set_xy(x, y1 + 2)
            self.set_font("ArialU", "B", 8.5)
            self.set_text_color(*TEXT)
            self.cell(col_w, 4.5, title, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x)
            self.set_font("ArialU", "", 7.5)
            self.set_text_color(*MUTED)
            self.multi_cell(col_w, 3.8, body)
        self.set_y(max(self.get_y(), y1) + 1)
        self.set_x(12)

    def project(self, title, date, bullets, stack):
        self.set_font("ArialU", "B", 8.5)
        self.set_text_color(*TEXT)
        self.cell(150, 4.5, title)
        self.set_font("ArialU", "B", 7.5)
        self.set_text_color(*LIGHT)
        self.cell(0, 4.5, date, align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_font("ArialU", "", 7.8)
        self.set_text_color(*MUTED)
        for b in bullets:
            x = self.l_margin
            self.set_x(x)
            self.cell(4, 4, "-")
            self.set_x(x + 5)
            self.multi_cell(self.epw - 5, 4, b)
        self.set_x(self.l_margin)
        self.set_font("ArialU", "B", 7.2)
        self.set_text_color(*ACCENT)
        self.cell(0, 4, stack, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.2)

    def labeled(self, label, body):
        self.set_font("ArialU", "B", 8)
        self.set_text_color(*TEXT)
        self.cell(0, 4.2, label, new_x="LMARGIN", new_y="NEXT")
        self.set_font("ArialU", "", 7.6)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 4, body)
        self.ln(1)

    def job_header(self, title, date):
        self.set_font("ArialU", "B", 8.5)
        self.set_text_color(*TEXT)
        self.cell(150, 4.5, title)
        self.set_font("ArialU", "B", 7.5)
        self.set_text_color(*LIGHT)
        self.cell(0, 4.5, date, align="R", new_x="LMARGIN", new_y="NEXT")

    def company(self, s):
        self.set_font("ArialU", "B", 8)
        self.set_text_color(*ACCENT)
        self.cell(0, 4, s, new_x="LMARGIN", new_y="NEXT")

    def bullet(self, s):
        self.set_font("ArialU", "", 7.8)
        self.set_text_color(*MUTED)
        x = self.l_margin
        self.set_x(x)
        self.cell(4, 4, "-")
        self.set_x(x + 5)
        self.multi_cell(self.epw - 5, 4, s)
        self.set_x(self.l_margin)


def main():
    pdf = CV()
    pdf.h1("Wadjoud PHILIPPE")
    pdf.role("Élève ingénieur - Développeur Python / Java / React")
    pdf.muted_line(
        "Stage 6 mois (fév. 2027) - Données géographiques / web - ESIGELEC Rouen"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star"
    )
    pdf.rule(0.8)

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 à l'ESIGELEC (Rouen). Je développe des apps web en Python, Java et "
        "React/JavaScript, avec un vrai intérêt pour les API et les bases de données (PostgreSQL/SQL). "
        "J'ai déjà travaillé sur de la cartographie / données spatiales en projet (recherche, cartes, "
        "stats). Curieux, rigoureux, à l'aise en équipe Agile : tests, revues, correctifs, amélioration "
        "continue. Je cherche un stage de 6 mois à partir de février 2027, motivé par un sujet à fort "
        "impact comme la donnée géographique réseau."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            ("Langages", "Python (Django / scripts), Java, JavaScript, TypeScript, React"),
            ("API & Web", "API REST, services backend, interfaces React, HTML/CSS"),
            ("Data & Géo", "PostgreSQL, SQL, MySQL, cartographie / données spatiales (projet), PostGIS (bases)"),
            ("Qualité & Méthodes", "Tests, revues de code, Git, Docker, Agile, diagnostic d'incidents"),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Club Sport - Java + cartographie / données géo",
            "2025",
            [
                "App multi-rôles avec recherche, cartographie et statistiques",
                "Accès SQL, exports, tests des parcours, Docker / Tomcat",
                "Premier contact concret avec des données spatiales / localisation",
            ],
            "Java | MySQL | Cartographie | Docker | Git | Agile",
        ),
        (
            "Factis - APIs + React + PostgreSQL",
            "2025",
            [
                "Conception d'APIs et d'écrans React (clients, factures, analytics)",
                "Optimisation des accès données PostgreSQL, tests, CI / Docker",
            ],
            "Python (scripts) | TypeScript | React | PostgreSQL | Docker | Git",
        ),
        (
            "Beniphone - Apps web & correctifs en équipe",
            "2025",
            [
                "Développement React / Node, analyse et correction d'incidents",
                "Travail pluridisciplinaire, priorisation, livraisons itératives",
            ],
            "React | JavaScript | Node.js | MySQL | Git",
        ),
        (
            "Smart CMS IA - Qualité & amélioration continue",
            "2025",
            [
                "Features full stack, jobs async, vérifs, revues et doc",
            ],
            "TypeScript | Python (scripts) | React | Git | CI",
        ),
        (
            "Mon Déménagement - Fiabilité en production",
            "2025",
            [
                "Maintenance évolutive, diagnostic d'anomalies, support utilisateurs",
            ],
            "PHP | MySQL | JavaScript | Git",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur - Dev Web Full Stack", "2024 - 2027")
    pdf.company("ESIGELEC - Rouen")
    pdf.para(
        "Python, Java, React, JavaScript, PostgreSQL/SQL, API REST, Docker, Agile/Scrum"
    )
    pdf.ln(1)
    pdf.job_header("Cycle préparatoire intégré", "2022 - 2024")
    pdf.company("ESIGELEC - Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. - Août 2023")
    pdf.company("PROMOPHARMA - Bénin")
    pdf.bullet("Rigueur, esprit d'équipe, diagnostic et support au quotidien")

    pdf.section("Langues & dispo")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  |  Anglais : B2 (docs techniques)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage 6 mois à partir de février 2027  |  Télétravail possible selon accord  |  Convention + gratification",
    )
    pdf.labeled(
        "Ce qui m'intéresse",
        "Python / Django / Java / React  |  API & PostgreSQL/PostGIS  |  Données géographiques / SIG  |  Agile",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Génère assets/cv-sopra-scrum.pdf — CV Sopra Steria (Java/Angular/JS, Scrum) — version soignée."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-sopra-scrum.pdf"
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
    pdf.role("Élève ingénieur — Développeur Java / Angular / Full Stack")
    pdf.muted_line(
        "Stage de fin d'études 6 mois (fév. 2027) · ESIGELEC Rouen · Scrum · Télétravail 2 j/sem."
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  ·  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  ·  linkedin.com/in/wadjoud-philippe  ·  github.com/Wadjoud-star"
    )
    pdf.rule()

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 à l'ESIGELEC (Rouen). Je développe en Java / JavaEE et Angular, "
        "et aussi en JavaScript full stack (Node.js, React / Vue). Autonome, curieux, rigoureux, "
        "avec un bon esprit de synthèse et le sens du collectif. J'aime comprendre les objectifs "
        "d'un projet, coder proprement, tester, et aller jusqu'au déploiement. À l'aise en Scrum "
        "(daily, sprint, revue, rétro). Je cherche un stage de fin d'études de 6 mois à partir "
        "de février 2027, motivé pour monter en compétences dans une équipe experte et rejoindre "
        "la dynamique Tech'Me UP."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            (
                "Backend",
                "Java, JavaEE / J2EE, Spring Boot, C# / .NET (bases), API REST, POO",
            ),
            (
                "Frontend",
                "Angular, TypeScript, React, Vue.js (bases), JavaScript, HTML/CSS",
            ),
            (
                "Full Stack JS",
                "Node.js, Express, React / Next.js, SQL (MySQL, PostgreSQL), Git",
            ),
            (
                "Méthodes & Qualité",
                "Scrum / Agile, conception → déploiement, tests, Docker, CI/CD, Linux",
            ),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Club Sport — Backend Java / JavaEE (conception → déploiement)",
            "2025",
            [
                "Analyse des objectifs, conception et développement d'une app multi-rôles",
                "Java / JEE : recherche, stats, exports, droits — tests des parcours, Docker / Tomcat",
                "Travail structuré en méthodes Agile, code clair et maintenable",
            ],
            "Java · JavaEE · Spring (formation) · MySQL · Docker · Git · Scrum",
        ),
        (
            "Factis — Full Stack JS (Node-like + UI dynamique)",
            "2025",
            [
                "Solution complète : APIs, écrans React/TypeScript, modelisation SQL",
                "Cycle de bout en bout : conception, développement, tests, mise en production",
                "Contribution concrète aux objectifs produit (clients, factures, analytics)",
            ],
            "React · TypeScript · Node.js · PostgreSQL · Docker · Git · CI",
        ),
        (
            "Beniphone — Angular/React skills + API Node.js",
            "2025",
            [
                "Interfaces dynamiques multi-rôles et backend JavaScript / Node.js",
                "Priorisation en équipe, livraisons itératives, esprit de service",
            ],
            "React · Angular (formation) · Node.js · MySQL · Git",
        ),
        (
            "Smart CMS IA — Technologies modernes & créativité",
            "2025",
            [
                "Exploration technique, features full stack, documentation et itérations",
            ],
            "Next.js · React · TypeScript · Node.js · Git · CI",
        ),
        (
            "Mon Déménagement — Cycle application en production",
            "2025",
            [
                "Maintenance / évolution : conception, déploiement, support utilisateurs",
            ],
            "PHP · MySQL · JavaScript · HTML/CSS · Git",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur — Dev Web Full Stack", "2024 – 2027")
    pdf.company("ESIGELEC — Rouen")
    pdf.para(
        "Java, JavaEE, Spring Boot, Angular, React, Vue.js, Node.js, TypeScript, Docker, Agile/Scrum"
    )
    pdf.ln(0.8)
    pdf.job_header("Cycle préparatoire intégré", "2022 – 2024")
    pdf.company("ESIGELEC — Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. – Août 2023")
    pdf.company("PROMOPHARMA — Bénin")
    pdf.bullet(
        "Autonomie, rigueur et sens du collectif sur support / maintenance — communication claire"
    )

    pdf.section("Langues & disponibilité")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  ·  Anglais : B2 (docs techniques, specs)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage fin d'études 6 mois dès février 2027  ·  Télétravail jusqu'à 2 j/semaine  ·  Ouvert CDI",
    )
    pdf.labeled(
        "Ce qui m'intéresse chez Sopra Steria",
        "Java / Angular / Node–React–Vue  ·  Scrum en équipe  ·  Cycle conception → déploiement  ·  Tech'Me UP",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), y={pdf.get_y():.1f}")


if __name__ == "__main__":
    main()

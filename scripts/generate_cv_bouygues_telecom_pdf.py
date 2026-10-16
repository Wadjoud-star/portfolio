#!/usr/bin/env python3
"""Génère assets/cv-bouygues-telecom.pdf — CV Bouygues Telecom (Java, vie client)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-bouygues-telecom.pdf"
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
    pdf.role("Élève ingénieur — Java · Git · outils d'IA")
    pdf.muted_line(
        "Stage 6 mois dès février 2027 · ESIGELEC Rouen · Bouygues Telecom · Meudon"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  ·  07 58 03 02 39")
    pdf.contact("Portfolio : https://wadjoud-star.github.io/portfolio/")
    pdf.contact("GitHub : https://github.com/Wadjoud-star")
    pdf.rule()

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur en dernière année à l'ESIGELEC (Rouen), spécialité informatique. "
        "Je code en Java. Spring Boot, je l'ai vu en formation, pas encore sur une "
        "appli en production. Git et Docker, je les utilise. Les pipelines CI, j'en "
        "ai les bases. Je me sers d'assistants d'IA pour coder, et je veux voir ce "
        "qu'ils apportent vraiment sur une migration, pas sur une démo. Robot Framework, "
        "je ne l'ai pas encore pratiqué. J'aime comprendre un existant, réutiliser "
        "ce qui marche, tester, et documenter. Rigoureux, autonome, à l'aise pour "
        "échanger avec des métiers différents. Français courant, anglais courant "
        "à l'écrit (B2). Dispo 6 mois dès février 2027, mobile sur Meudon-la-Forêt."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            (
                "Java",
                "Java, Spring Boot (formation), SQL, réutiliser l'existant",
            ),
            (
                "Qualité",
                "Tests de parcours, Git, documentation — Robot Framework à prendre",
            ),
            (
                "DevOps",
                "Docker, Git, CI/CD (bases) — pipelines à pratiquer en équipe",
            ),
            (
                "IA",
                "Assistants de code au quotidien, prototypes pour vérifier une idée",
            ),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Club Sport — Java, Docker, équipe",
            "2025",
            [
                "Appli Java, MySQL, Scrum, conteneur Docker, Git",
                "github.com/Wadjoud-star/Projet-S8",
            ],
            "Java · MySQL · Docker · Git · Scrum",
        ),
        (
            "Mon Déménagement — Faire évoluer un existant",
            "2025",
            [
                "Outil déjà en ligne, corrections à partir des retours",
                "github.com/Wadjoud-star/Plateforme-D-m-nagement",
            ],
            "JavaScript · MySQL · Git",
        ),
        (
            "Factis — Du code jusqu'au dépôt",
            "2025",
            [
                "Conception, réalisation, dépôt Git",
                "github.com/Wadjoud-star/factis",
            ],
            "TypeScript · PostgreSQL · Git",
        ),
        (
            "Smart CMS — IA sur un vrai outil",
            "2025",
            [
                "Assistant d'IA branché sur le produit, pas sur un exercice à part",
                "github.com/Wadjoud-star/smart-cms-ia",
            ],
            "TypeScript · Git · IA générative",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur — Informatique", "2024 – 2027")
    pdf.company("ESIGELEC — Rouen")
    pdf.para("Java, Spring (formation), Git, Docker, CI (bases), assistants d'IA")
    pdf.ln(0.8)
    pdf.job_header("Cycle préparatoire intégré", "2022 – 2024")
    pdf.company("ESIGELEC — Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. – Août 2023")
    pdf.company("PROMOPHARMA — Bénin")
    pdf.bullet("Autonomie, échanges avec des métiers non techniques, organisation")

    pdf.section("Disponibilité")
    pdf.labeled(
        "Stage",
        "6 mois dès février 2027  ·  Meudon-la-Forêt  ·  convention + gratification",
    )
    pdf.labeled(
        "Langues",
        "Français : courant  ·  Anglais : courant à l'écrit (B2 — docs, échanges)",
    )
    pdf.labeled(
        "Portfolio",
        "https://wadjoud-star.github.io/portfolio/",
    )
    pdf.labeled(
        "Ce qui m'intéresse chez Bouygues Telecom",
        "Comprendre un système vie client déjà en place, et aider à le faire "
        "passer vers la nouvelle solution. Je veux voir, sur un vrai projet, "
        "où l'IA accélère la migration, et où il faut encore lire le code, "
        "tester, et documenter. Puis livrer des composants Java qui s'appuient "
        "sur ce qui existe déjà.",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), y={pdf.get_y():.1f}")


if __name__ == "__main__":
    main()

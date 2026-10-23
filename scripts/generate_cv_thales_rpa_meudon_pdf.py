#!/usr/bin/env python3
"""Génère assets/cv-thales-rpa-meudon.pdf — CV Thales Meudon (RPA / automatisation)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-thales-rpa-meudon.pdf"
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
    pdf.role("Élève ingénieur — Python · SQL · automatisation")
    pdf.muted_line(
        "Stage 6 mois dès février 2027 · ESIGELEC Rouen · Thales · Meudon"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  ·  07 58 03 02 39")
    pdf.contact("Portfolio : https://wadjoud-star.github.io/portfolio/")
    pdf.contact("GitHub : https://github.com/Wadjoud-star")
    pdf.rule()

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur en dernière année à l'ESIGELEC (Rouen), en informatique. "
        "Je code en Python et en SQL. Office (Word, Excel, PowerPoint), je m'en sers. "
        "UiPath Studio, je ne l'ai pas encore pratiqué. Power BI et VBA non plus. "
        ".NET, ce sont des bases. Ce qui m'intéresse : comprendre un process avec "
        "son propriétaire, enlever ce qui ne sert à rien, puis automatiser et "
        "former les gens qui s'en servent. Curieux, autonome, proactif. "
        "Français courant, anglais courant à l'écrit (B2). "
        "Dispo 6 mois dès février 2027, mobile sur Meudon."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            (
                "Code",
                "Python, SQL, JavaScript — .NET (bases) — Perl / VBA : non",
            ),
            (
                "Office & data",
                "Word, Excel, PowerPoint — Power BI et UiPath à prendre en main",
            ),
            (
                "Process",
                "Comprendre un besoin, documenter, tester, former les utilisateurs",
            ),
            (
                "Travail",
                "Autonomie, échanges multi-sites, qualité des livrables",
            ),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Smart CMS — Python et données",
            "2025",
            [
                "Scripts Python pour structurer et traiter de l'information",
                "github.com/Wadjoud-star/smart-cms-ia",
            ],
            "Python · SQL · Git",
        ),
        (
            "Factis — SQL et suivi",
            "2025",
            [
                "Modèle de données, filtres, outil qu'on peut faire évoluer",
                "github.com/Wadjoud-star/factis",
            ],
            "TypeScript · PostgreSQL · Git",
        ),
        (
            "Mon Déménagement — Formation utilisateurs",
            "2025",
            [
                "Expliquer des changements, recueillir les retours, corriger",
                "github.com/Wadjoud-star/Plateforme-D-m-nagement",
            ],
            "JavaScript · MySQL · Git",
        ),
        (
            "Club Sport — Process en équipe",
            "2025",
            [
                "Besoins, livraison par étapes, documentation",
                "github.com/Wadjoud-star/Projet-S8",
            ],
            "Java · MySQL · Git · Scrum",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur — Informatique", "2024 – 2027")
    pdf.company("ESIGELEC — Rouen")
    pdf.para("Python, SQL, Office, Git — UiPath / Power BI / VBA à apprendre")
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
        "6 mois dès février 2027  ·  Meudon  ·  convention + gratification",
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
        "Ce qui m'intéresse chez Thales",
        "Le RPA pour alléger des process industriels, sur plusieurs sites. "
        "Je veux d'abord comprendre le process avec son propriétaire, "
        "enlever le superflu, puis automatiser, documenter, former. "
        "UiPath, je ne le connais pas encore : je le prends avec l'équipe IT RPA.",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), y={pdf.get_y():.1f}")


if __name__ == "__main__":
    main()

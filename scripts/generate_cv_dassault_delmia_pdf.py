#!/usr/bin/env python3
"""Génère assets/cv-dassault-delmia.pdf — CV Dassault DELMIA (Supply Chain Analytics / OOP)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-dassault-delmia.pdf"
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
    pdf.role("Élève ingénieur - Développeur logiciel / Analytics")
    pdf.muted_line(
        "Stage fin d'études Master (fév. 2027) - ESIGELEC Rouen - Anglais B2+"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star"
    )
    pdf.rule(0.8)

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 (ESIGELEC), Master Informatique / développement logiciel. "
        "Solides bases en POO et en analyse / résolution de problèmes. Motivé pour apprendre "
        "une stack propriétaire et monter en compétences sur l'architecture logicielle et le "
        "métier 3DEXPERIENCE. Intéressé par l'IA et les apps d'analytics. À l'aise en anglais "
        "pour une équipe internationale, bon esprit d'équipe et de communication. Je cherche "
        "un stage de fin d'études à partir de février 2027 sur des solutions Supply Chain Analytics."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            ("Développement", "POO (Java, C#, TypeScript), conception logicielle, APIs, documentation"),
            ("Data & Analytics", "SQL, dashboards / analytics métier, scripts Python, intérêt IA"),
            ("Qualité", "Analyse de problèmes, tests, doc technique, optimisation progressive"),
            ("Collab & Langues", "Travail en équipe, adaptabilité, anglais B2+ (équipe internationale)"),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Factis - Analytics métier & optimisation",
            "2025",
            [
                "Conception / développement de features analytics (clients, factures, indicateurs)",
                "Analyse des besoins, résolution de problèmes data, documentation technique",
            ],
            "TypeScript | SQL | PostgreSQL | Analytics | Git | Docker",
        ),
        (
            "Smart CMS IA - IA & apprentissage continue",
            "2025",
            [
                "Exploration IA générative, pipelines, itérations produit",
                "Forte motivation à apprendre une nouvelle stack et documenter les choix",
            ],
            "TypeScript | Python | IA | Git | CI",
        ),
        (
            "Club Sport - POO Java & architecture",
            "2025",
            [
                "Application orientée objet multi-rôles : conception, développement, optimisation",
                "Montée en compétences architecture logicielle / fonctionnelle",
            ],
            "Java | POO | MySQL | Docker | Git",
        ),
        (
            "Beniphone - Équipe internationale-ready",
            "2025",
            [
                "Développement en équipe, communication claire, adaptabilité aux besoins métier",
            ],
            "TypeScript | React | Node.js | Git",
        ),
        (
            "Mon Déménagement - Logiciel en production",
            "2025",
            [
                "Maintenance, analyse d'incidents, documentation des processus",
            ],
            "PHP | MySQL | Git",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur / Master - Dev logiciel Full Stack", "2024 - 2027")
    pdf.company("ESIGELEC - Rouen")
    pdf.para(
        "POO, architecture logicielle, data, anglais technique, IA (projets), Agile"
    )
    pdf.ln(1)
    pdf.job_header("Cycle préparatoire intégré", "2022 - 2024")
    pdf.company("ESIGELEC - Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. - Août 2023")
    pdf.company("PROMOPHARMA - Bénin")
    pdf.bullet("Esprit d'équipe, communication, résolution de problèmes au quotidien")

    pdf.section("Langues & dispo")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  |  Anglais : B2+ (collab internationale, docs, specs)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage fin d'études Master à partir de février 2027  |  Mobilité selon site DELMIA",
    )
    pdf.labeled(
        "Ce qui m'intéresse",
        "Supply Chain Analytics  |  3DEXPERIENCE / DELMIA  |  POO & architecture  |  IA & innovation",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

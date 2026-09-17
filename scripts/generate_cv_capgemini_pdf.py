#!/usr/bin/env python3
"""Génère assets/cv-capgemini.pdf — CV Capgemini avec accents FR (fpdf2 + Arial)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-capgemini.pdf"
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# Couleurs 0-255
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
        # row 1
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
        # row 2
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


def main():
    pdf = CV()
    pdf.h1("Wadjoud PHILIPPE")
    pdf.role("Élève ingénieur - Développeur Java / Webservices / SQL")
    pdf.muted_line("Stage de fin d'études M2 (fév. 2027) - ESIGELEC Rouen - Anglais B2+")
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star"
    )
    pdf.rule(0.8)

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur en M2 à l'ESIGELEC (Rouen). Je développe surtout en Java, avec des APIs REST "
        "et du SQL. Sur mes projets, j'ai l'habitude de partir d'un besoin, coder la feature, tester, "
        "corriger les bugs et laisser une doc claire. Je connais aussi un peu SOAP, Oracle et SQL Server. "
        "À l'aise en anglais (B2). Je cherche un stage de fin d'études à partir de février 2027, "
        "idéalement aux côtés de leads techniques."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            ("Java & Backend", "Java, Spring Boot, JEE, POO, APIs, conception de fonctionnalités"),
            ("Webservices", "REST (bon niveau), SOAP (bases), JSON, JWT, doc d'API"),
            ("Bases de données", "SQL, MySQL, PostgreSQL, bases Oracle / SQL Server"),
            ("Qualité & Delivery", "Tests d'intégration, Git, CI/CD, Docker, Jenkins/GitLab (bases)"),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Club Sport - App Java multi-rôles",
            "2025",
            [
                "Besoins métiers (rôles, recherche, stats) -> features Java / JEE + SQL",
                "Tests des parcours, correction de bugs, doc",
                "Mise en prod avec Docker / Tomcat",
            ],
            "Java | Spring (formation) | SQL | Docker | Git | Agile",
        ),
        (
            "Factis - APIs REST, SQL et CI",
            "2025",
            [
                "Features et APIs REST (clients, factures, analytics)",
                "Checks sur les données, tests des parcours bout en bout",
                "Docker / CI et petite doc technique",
            ],
            "TypeScript | API REST | PostgreSQL | Docker | Git | CI",
        ),
        (
            "Beniphone - Features et correctifs en équipe",
            "2025",
            [
                "Priorisation des tâches avec l'équipe",
                "Debug, correctifs, notes sur les écarts trouvés",
            ],
            "Node.js | REST | MySQL | React | Git",
        ),
        (
            "Smart CMS IA - Pipelines et vérifs",
            "2025",
            [
                "Jobs async, vérif des sorties, doc au fur et à mesure",
            ],
            "TypeScript | REST | SQL | Git | CI",
        ),
        (
            "Mon Déménagement - Prod / maintenance",
            "2025",
            [
                "Bugs en prod, correctifs, petites notes d'intervention",
            ],
            "PHP | SQL | JavaScript | Git",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.set_font("ArialU", "B", 8.5)
    pdf.set_text_color(*TEXT)
    pdf.cell(150, 4.5, "Diplôme d'ingénieur - Dev Web Full Stack (M1/M2)")
    pdf.set_font("ArialU", "B", 7.5)
    pdf.set_text_color(*LIGHT)
    pdf.cell(0, 4.5, "2024 - 2027", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialU", "B", 8)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 4, "ESIGELEC - Rouen", new_x="LMARGIN", new_y="NEXT")
    pdf.para("Java, Spring Boot, REST/SOAP, SQL, bases Oracle/SQL Server, CI/CD, anglais B2")
    pdf.ln(1)
    pdf.set_font("ArialU", "B", 8.5)
    pdf.set_text_color(*TEXT)
    pdf.cell(150, 4.5, "Cycle préparatoire intégré")
    pdf.set_font("ArialU", "B", 7.5)
    pdf.set_text_color(*LIGHT)
    pdf.cell(0, 4.5, "2022 - 2024", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialU", "B", 8)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 4, "ESIGELEC - Cotonou, Bénin", new_x="LMARGIN", new_y="NEXT")

    pdf.section("Expérience")
    pdf.set_font("ArialU", "B", 8.5)
    pdf.set_text_color(*TEXT)
    pdf.cell(150, 4.5, "Stagiaire informatique")
    pdf.set_font("ArialU", "B", 7.5)
    pdf.set_text_color(*LIGHT)
    pdf.cell(0, 4.5, "Juil. - Août 2023", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialU", "B", 8)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 4, "PROMOPHARMA - Bénin", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialU", "", 7.8)
    pdf.set_text_color(*MUTED)
    x = pdf.l_margin
    pdf.set_x(x)
    pdf.cell(4, 4, "-")
    pdf.set_x(x + 5)
    pdf.multi_cell(pdf.epw - 5, 4, "Support, bugs, petites docs - travail avec l'équipe technique")
    pdf.set_x(pdf.l_margin)

    pdf.section("Langues & dispo")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  |  Anglais : B2+ (docs, specs, échanges tech)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage de fin d'études à partir de février 2027  |  Mobile selon le site Capgemini",
    )
    pdf.labeled(
        "Ce qui m'intéresse",
        "Java, REST/SOAP, SQL, CI/CD, bosser proprement avec une équipe tech",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

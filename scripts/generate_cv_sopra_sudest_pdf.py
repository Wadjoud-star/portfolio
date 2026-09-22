#!/usr/bin/env python3
"""Génère assets/cv-sopra-sudest.pdf — CV Sopra Steria Sud-Est (Java/Spring/Angular, DevOps)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-sopra-sudest.pdf"
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
    pdf.role("Élève ingénieur - Développeur Java / Spring Boot / Angular")
    pdf.muted_line(
        "Stage fin d'études 4–6 mois (janv.–avr. 2027) - Mobilité Sud-Est - ESIGELEC Rouen"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star"
    )
    pdf.rule(0.8)

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 à l'ESIGELEC (Rouen). Je développe en Java / Spring Boot et Angular, "
        "et je touche aussi au PHP, .NET / C# et au JavaScript. Sur mes projets, je fais le cycle "
        "classique : comprendre le besoin, concevoir, coder, tester, déployer. À l'aise en Agile "
        "(daily, démos, retros) et avec Git, Docker, CI/CD. Motivé par des projets client concrets "
        "en équipe de 5–6 personnes. Je cherche un stage de 4 à 6 mois à partir de janvier–avril 2027, "
        "mobile Sud-Est."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            ("Backend", "Java, Spring Boot, JEE, PHP, C# / .NET (bases), API REST"),
            ("Frontend", "Angular, TypeScript, React, JavaScript, HTML/CSS"),
            ("Data & Qualité", "SQL (MySQL, PostgreSQL), tests, plans de tests, doc"),
            ("DevOps & Méthodes", "Git, GitLab CI, Docker, Jenkins (bases), Azure/AWS (notions), Agile"),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Club Sport - Java, conception → déploiement",
            "2025",
            [
                "Analyse des besoins, développement Java multi-rôles (recherche, stats, exports)",
                "Tests des parcours, correction de bugs, mise en prod Docker / Tomcat",
            ],
            "Java | Spring (formation) | MySQL | Docker | Git | Agile",
        ),
        (
            "Factis - Full stack + CI",
            "2025",
            [
                "Features métier (clients, factures, analytics), APIs et écrans",
                "Tests d'intégration des parcours, Docker / CI, petite doc technique",
            ],
            "TypeScript | React | PostgreSQL | Docker | Git | CI",
        ),
        (
            "Beniphone - Équipe produit / correctifs",
            "2025",
            [
                "Développement multi-rôles, priorisation, participation aux itérations",
                "Debug, correctifs, échanges proches d'un contexte client",
            ],
            "React | Node.js | MySQL | Git",
        ),
        (
            "Smart CMS IA - Features & industrialisation légère",
            "2025",
            [
                "Dev full stack, jobs async, vérifs, livraisons itératives",
            ],
            "TypeScript | Node.js | Git | CI",
        ),
        (
            "Mon Déménagement - Maintenance évolutive",
            "2025",
            [
                "Évolution d'une app en prod : specs légères, dev, qualification, support",
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
        "Java, Spring Boot, Angular, PHP, .NET (notions), Docker, GitLab CI, Agile/Scrum"
    )
    pdf.ln(1)
    pdf.job_header("Cycle préparatoire intégré", "2022 - 2024")
    pdf.company("ESIGELEC - Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. - Août 2023")
    pdf.company("PROMOPHARMA - Bénin")
    pdf.bullet("Support, bugs, petites docs - travail en équipe")

    pdf.section("Langues & dispo")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  |  Anglais : B2 (docs, specs)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage 4 à 6 mois - démarrage entre janvier et avril 2027  |  "
        "Mobilité Sud-Est  |  Télétravail jusqu'à 2 j/semaine  |  Ouvert CDI",
    )
    pdf.labeled(
        "Ce qui m'intéresse",
        "Java / Spring / Angular  |  DevOps (GitLab, Docker, Jenkins)  |  Agile en équipe  |  Tech'Me UP",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

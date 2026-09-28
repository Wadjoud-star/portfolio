#!/usr/bin/env python3
"""Génère assets/cv-sia-platform.pdf — CV Sia Platform Engineer (DevOps / Data Science)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-sia-platform.pdf"
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
    pdf.role("Élève ingénieur — Platform Engineer / DevOps (Data)")
    pdf.muted_line(
        "Stage fin d'études 6 mois (fév. 2027) · ESIGELEC Rouen · Sia — BU Data Science · Paris"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  ·  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  ·  linkedin.com/in/wadjoud-philippe  ·  github.com/Wadjoud-star"
    )
    pdf.rule()

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 à l'ESIGELEC (Rouen), bon niveau Python pour du backend "
        "et de l'automatisation. J'industrialise avec Docker, Git et des pipelines CI/CD, "
        "et j'ai une forte appétence pour monter sur Kubernetes, le Cloud et la mise "
        "en production de services data. Curieux, analyse et automatisation d'abord "
        "(\"automate all the things\"), j'aime travailler en équipe auprès de Data Scientists "
        "et Software Engineers. Sensible à la sécurité avant de pousser du code. "
        "Stage de fin d'études 6 mois à partir de février 2027 — Paris."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            (
                "Python & backend",
                "Python (scripts, APIs, microservices), JavaScript/TypeScript, Java, C# (bases)",
            ),
            (
                "Containers & orchestration",
                "Docker (pratique), Kubernetes (notions / appétit fort), packaging d'applications",
            ),
            (
                "Cloud & CI/CD",
                "Azure / AWS / GCP (bases), CI/CD (GitLab CI, Jenkins notions), Terraform (notions)",
            ),
            (
                "Data & méthodes",
                "SQL / PostgreSQL, pipelines data (projets), Git, Agile, anglais pro B2",
            ),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Factis — Containerisation & CI d'une app data/web",
            "2025",
            [
                "Dockerisation, pipelines CI, déploiement — automatisation de la livraison",
                "API + front ; focus fiabilité et industrialisation",
            ],
            "Python · TypeScript · Node.js · PostgreSQL · Docker · Git · CI",
        ),
        (
            "Smart CMS IA — Automatisation Python & services",
            "2025",
            [
                "Scripts / jobs serveur, APIs, traitement asynchrone — logique microservice légère",
                "CI, documentation ; sensibilisation sécurité et bonnes pratiques",
            ],
            "Python · TypeScript · React · Git · CI",
        ),
        (
            "Club Sport — Packaging & déploiement",
            "2025",
            [
                "Application Java containerisée (Docker / Tomcat), tests, livraison itérative",
            ],
            "Java · MySQL · Docker · Git · Agile",
        ),
        (
            "Beniphone — Back/front en équipe",
            "2025",
            [
                "APIs REST, collaboration Git, montée en compétence rapide sur le stack",
            ],
            "Node.js · React · MySQL · Git",
        ),
        (
            "Mon Déménagement — Production & maintenance",
            "2025",
            [
                "Évolutions en prod, rigueur, automatisation des tâches répétitives quand possible",
            ],
            "PHP · MySQL · JavaScript · Git",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur — Dev Web / Génie logiciel · Data", "2024 – 2027")
    pdf.company("ESIGELEC — Rouen")
    pdf.para(
        "Python, Docker, CI/CD, Cloud (bases), Kubernetes (notions), SQL, "
        "Java / TypeScript, Agile, anglais professionnel"
    )
    pdf.ln(0.8)
    pdf.job_header("Cycle préparatoire intégré", "2022 – 2024")
    pdf.company("ESIGELEC — Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. – Août 2023")
    pdf.company("PROMOPHARMA — Bénin")
    pdf.bullet("Autonomie, analyse, travail en équipe, appétit DIY pour résoudre les problèmes")

    pdf.section("Langues & disponibilité")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  ·  Anglais : B2 / courant pro (docs, clients, specs)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage fin d'études 6 mois dès février 2027  ·  Paris  ·  Convention + gratification · pré-embauche",
    )
    pdf.labeled(
        "Ce qui m'intéresse chez Sia",
        "Platform / DevOps Data  ·  Cloud & coûts  ·  K8s data workloads  ·  Python automation  ·  CI/CD",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), y={pdf.get_y():.1f}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Génère assets/cv-ateme-observability.pdf — CV Ateme (Go/Vue/K8s, monitoring)."""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-ateme-observability.pdf"
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
        bottoms = []
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
            bottoms.append(self.get_y())
        y1 = max(bottoms) + 2
        bottoms = []
        for i, (title, body) in enumerate(skills[2:]):
            x = x0 + i * (col_w + gap)
            self.set_xy(x, y1)
            self.set_font("ArialU", "B", 8.5)
            self.set_text_color(*TEXT)
            self.cell(col_w, 4.5, title, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x)
            self.set_font("ArialU", "", 7.5)
            self.set_text_color(*MUTED)
            self.multi_cell(col_w, 3.8, body)
            bottoms.append(self.get_y())
        self.set_y(max(bottoms) + 1)
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
    pdf.role("Élève ingénieur — Full Stack / Monitoring & Observabilité")
    pdf.muted_line(
        "Stage fin d'études (fév. 2027) — Mobilité Rennes ou Vélizy — ESIGELEC Rouen"
    )
    pdf.contact("wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39")
    pdf.contact(
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star"
    )
    pdf.rule(0.8)

    pdf.section("Profil")
    pdf.para(
        "Élève ingénieur bac+5 à l'ESIGELEC (Rouen). J'aime intervenir back et front sur un même "
        "outil, et comprendre une plateforme dans son ensemble. Solide en backend (Go en formation / "
        "langages proches : Python, Node, Java), frontend (Vue.js en formation, React/TypeScript "
        "en pratique), agrégation de données techniques et diagnostic. Sensible au monitoring "
        "(métriques, dashboards, détection d'anomalies), Docker / containers, CI et Git. Motivé "
        "pour monter vite sur Kubernetes, Prometheus et l'observabilité. Stage fin d'études à "
        "partir de février 2027 — Rennes ou Vélizy."
    )

    pdf.section("Compétences techniques")
    pdf.skill_grid(
        [
            (
                "Backend",
                "Go (formation), Python, Node.js, Java — APIs, agrégation de données, traitement",
            ),
            (
                "Frontend",
                "Vue.js (formation), React, TypeScript — UI de supervision / dashboards clairs",
            ),
            (
                "Observabilité & Data",
                "Métriques, logs, indicateurs d'anomalie, analytics ; Prometheus/Grafana (notions)",
            ),
            (
                "Infra & Qualité",
                "Git, Docker, CI/CD (GitLab CI notions), Kubernetes (notions), tests, revues",
            ),
        ]
    )

    pdf.section("Projets")
    projects = [
        (
            "Factis — Dashboards & agrégation de données techniques",
            "2025",
            [
                "Écrans d'analytics : restitution claire d'indicateurs (ouvertures, parcours, états)",
                "Backend + front : collecter, agréger, afficher — logique proche d'une vue de supervision",
            ],
            "TypeScript · React · PostgreSQL · Docker · Git · CI",
        ),
        (
            "Smart CMS IA — Diagnostic, jobs & suivi d'état",
            "2025",
            [
                "Pipelines / jobs async : suivi d'état, détection d'échecs, restitution UI",
                "Scripts Python, tests, doc — approche diagnostic / supervision applicative",
            ],
            "Python · TypeScript · React · Git · CI",
        ),
        (
            "Club Sport — Supervision métier multi-nœuds (logique)",
            "2025",
            [
                "Écrans de suivi multi-rôles, stats, exports — corrélation d'états applicatifs",
                "Déploiement containerisé Docker / Tomcat, tests des parcours",
            ],
            "Java · MySQL · Docker · Linux · Git",
        ),
        (
            "Beniphone — Full stack & identification d'anomalies",
            "2025",
            [
                "UI + API : workflows tracés, analyse d'écarts, correctifs en équipe",
            ],
            "React · Node.js · MySQL · Git",
        ),
        (
            "Mon Déménagement — Fiabilité en production",
            "2025",
            [
                "Diagnostic d'incidents, maintenance, packaging / livraison continue légère",
            ],
            "PHP · MySQL · JavaScript · Git",
        ),
    ]
    for t, d, b, s in projects:
        pdf.project(t, d, b, s)

    pdf.section("Formation")
    pdf.job_header("Diplôme d'ingénieur — Dev Web Full Stack / Génie logiciel", "2024 – 2027")
    pdf.company("ESIGELEC — Rouen")
    pdf.para(
        "Backend (Go/Python/Node/Java), Vue/React, Docker, CI, monitoring (notions), Kubernetes (notions)"
    )
    pdf.ln(1)
    pdf.job_header("Cycle préparatoire intégré", "2022 – 2024")
    pdf.company("ESIGELEC — Cotonou, Bénin")

    pdf.section("Expérience")
    pdf.job_header("Stagiaire informatique", "Juil. – Août 2023")
    pdf.company("PROMOPHARMA — Bénin")
    pdf.bullet("Esprit d'analyse, diagnostic, travail en équipe sur support / incidents")

    pdf.section("Langues & dispo")
    pdf.labeled(
        "Langues",
        "Français : langue maternelle  |  Anglais : B2 (docs techniques, équipe internationale)",
    )
    pdf.labeled(
        "Disponibilité",
        "Stage fin d'études dès février 2027  |  Mobilité Rennes ou Vélizy-Villacoublay",
    )
    pdf.labeled(
        "Ce qui m'intéresse",
        "Observabilité unifiée  |  Go + VueJS  |  Prometheus / Kubernetes  |  Full stack plateforme",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

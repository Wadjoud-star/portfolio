#!/usr/bin/env python3
"""Génère assets/cv-dassault-plouzane.pdf — CV Dassault Systèmes Plouzané (React/PHP)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-dassault-plouzane.pdf"

ACCENT = (0.263, 0.220, 0.659)
ACCENT_DARK = (0.216, 0.188, 0.639)
TEXT = (0.067, 0.094, 0.153)
MUTED = (0.290, 0.333, 0.408)
LIGHT = (0.420, 0.447, 0.502)
RULE = (0.827, 0.827, 0.843)


def esc(s: str) -> str:
    replacements = {
        "\u2014": "-", "\u2013": "-", "\u2022": "-", "\u2192": "->",
        "\u00b7": "|", "\u2026": "...", "\u00a0": " ",
        "\u0153": "oe", "\u0152": "OE",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
    return (
        s.encode("latin-1", "replace").decode("latin-1")
        .replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    )


def rgb(c):
    return f"{c[0]:.3f} {c[1]:.3f} {c[2]:.3f}"


class PDF:
    def __init__(self):
        self.y = 812
        self.page_w = 595
        self.margin = 34
        self.content = []

    def fill(self, c):
        self.content.append(f"{rgb(c)} rg")

    def stroke(self, c):
        self.content.append(f"{rgb(c)} RG")

    def text(self, x, size, string, bold=False, color=None):
        if color is not None:
            self.fill(color)
        font = "F2" if bold else "F1"
        self.content.append(
            f"BT /{font} {size} Tf {x:.1f} {self.y:.1f} Td ({esc(string)}) Tj ET"
        )

    def text_w(self, string, size, bold=False):
        return (0.52 if bold else 0.48) * size * len(string)

    def text_right(self, size, string, bold=False, color=None):
        x = self.page_w - self.margin - self.text_w(string, size, bold)
        self.text(x, size, string, bold=bold, color=color)

    def multilines(self, size, text, leading=None, bold=False, color=None, max_w=None, indent=0):
        leading = leading or (size + 2.2)
        max_w = max_w or (self.page_w - 2 * self.margin - indent)
        x = self.margin + indent
        words = text.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if self.text_w(test, size, bold) > max_w:
                self.text(x, size, line, bold=bold, color=color)
                self.y -= leading
                line = w
            else:
                line = test
        if line:
            self.text(x, size, line, bold=bold, color=color)
            self.y -= leading

    def bullet(self, text, size=7.6, leading=10.2, color=None):
        color = color or MUTED
        self.text(self.margin, size, "-", bold=True, color=ACCENT)
        self.multilines(size, text, leading=leading, color=color, indent=10)

    def rule(self, color=ACCENT, thickness=2.0):
        self.stroke(color)
        self.content.append(
            f"{thickness} w {self.margin} {self.y:.1f} m {self.page_w - self.margin} {self.y:.1f} l S"
        )
        self.y -= 8

    def thin_rule(self):
        self.rule(color=RULE, thickness=0.5)

    def space(self, n=7):
        self.y -= n

    def section(self, title):
        self.space(7)
        self.text(self.margin, 9.5, title.upper(), bold=True, color=ACCENT)
        self.y -= 4
        self.thin_rule()
        self.space(3)

    def build(self) -> bytes:
        stream = ("\n".join(self.content) + "\n").encode("latin-1", "replace")
        objects = [
            b"1 0 obj<< /Type /Catalog /Pages 2 0 R >>endobj\n",
            b"2 0 obj<< /Type /Pages /Kids [3 0 R] /Count 1 >>endobj\n",
            (
                b"3 0 obj<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
                b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>endobj\n"
            ),
            b"4 0 obj<< /Length %d >>stream\n" % len(stream) + stream + b"endstream\nendobj\n",
            b"5 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>endobj\n",
            b"6 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>endobj\n",
        ]
        out = bytearray(b"%PDF-1.4\n")
        offsets = [0]
        for obj in objects:
            offsets.append(len(out))
            out.extend(obj)
        xref = len(out)
        out.extend(f"xref\n0 {len(offsets)}\n".encode())
        out.extend(b"0000000000 65535 f \n")
        for off in offsets[1:]:
            out.extend(f"{off:010d} 00000 n \n".encode())
        out.extend(
            f"trailer<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
        )
        return bytes(out)


def main():
    p = PDF()
    m = p.margin

    p.text(m, 19, "Wadjoud PHILIPPE", bold=True, color=TEXT)
    p.y -= 14
    p.text(m, 10, "Eleve Ingenieur - Developpeur Full Stack React / PHP", bold=True, color=ACCENT)
    p.y -= 11
    p.text(m, 8.2, "Stage fin d'etudes 6 mois (fev. 2027) - Mobilite Plouzane - ESIGELEC Rouen", color=MUTED)
    p.y -= 10
    p.text(m, 7.8, "wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39", color=ACCENT_DARK)
    p.y -= 9
    p.text(
        m, 7.8,
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star",
        color=ACCENT_DARK,
    )
    p.y -= 7
    p.rule(thickness=2.2)

    p.section("Profil")
    p.multilines(
        7.8,
        "Eleve ingenieur bac+5 (ESIGELEC), developpeur full stack centre sur les SPA React/JavaScript "
        "et les API backend (PHP, Node.js), avec SQL (MySQL/MariaDB). Je contribue a la conception, "
        "au developpement et a la modernisation d'applications web : nouvelles fonctionnalites, "
        "refontes, POC et partage d'experimentations. Rigoureux, a l'aise en equipe internationale "
        "et en anglais. Recherche un stage de fin d'etudes de 6 mois a Plouzane a partir de fevrier 2027.",
        leading=9.8,
        color=MUTED,
    )

    p.section("Competences techniques")
    skills = [
        ("Frontend", "React, Next.js, JavaScript, TypeScript, HTML/CSS, SPA, Tailwind, Angular"),
        ("Backend & API", "PHP, Node.js, API REST, JWT, HTTPS / WSS (notions), integrations API tierces"),
        ("Data", "SQL (MySQL, MariaDB, PostgreSQL), modelisation, recherche / indexing (notions OpenSearch)"),
        ("Methodes & Outils", "Git, Docker, CI/CD, Agile/Scrum, Linux, anglais (equipe internationale)"),
    ]
    col_w = (p.page_w - 2 * m - 12) / 2
    start_y = p.y
    left_x, right_x = m, m + col_w + 12

    def skill_block(x, title, body, y0):
        p.y = y0
        p.text(x, 8.2, title, bold=True, color=TEXT)
        p.y -= 10
        words = body.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if p.text_w(test, 7.2) > col_w:
                p.text(x, 7.2, line, color=MUTED)
                p.y -= 9
                line = w
            else:
                line = test
        if line:
            p.text(x, 7.2, line, color=MUTED)
            p.y -= 9
        return p.y

    y_l = skill_block(left_x, skills[0][0], skills[0][1], start_y)
    y_r = skill_block(right_x, skills[1][0], skills[1][1], start_y)
    row2 = min(y_l, y_r) - 3
    y_l = skill_block(left_x, skills[2][0], skills[2][1], row2)
    y_r = skill_block(right_x, skills[3][0], skills[3][1], row2)
    p.y = min(y_l, y_r) - 1

    p.section("Projets significatifs")
    projects = [
        (
            "Factis - SPA React/TS + API + modernisation",
            "2025",
            [
                "Developpement full stack d'une plateforme metier (clients, factures, analytics)",
                "Interfaces SPA, services backend REST et modelisation SQL (PostgreSQL)",
                "Mise en production, iterations et evolution continue des fonctionnalites",
            ],
            "React | Next.js | TypeScript | Prisma | PostgreSQL | Docker | Git",
        ),
        (
            "Beniphone - Apps web multi-roles & besoins metier",
            "2025",
            [
                "Developpement frontend/backend : admin, moderation, transactions, parcours clients",
                "Prise en compte des besoins metier, communication transparente sur les blocages",
                "Livraisons iteratives, Git et documentation",
            ],
            "React | JavaScript | Node.js | Prisma | MySQL | Git",
        ),
        (
            "Mon Demenagement - Plateforme PHP / SQL en production",
            "2025",
            [
                "Maintenance et evolution d'une application web multi-roles (PHP, MySQL, JS)",
                "Nouvelles fonctionnalites selon les retours utilisateurs, support et qualification",
            ],
            "PHP | MySQL | MVC | JavaScript | HTML/CSS | Git",
        ),
        (
            "Smart CMS IA - POC, veille & partage",
            "2025",
            [
                "Exploration de solutions (API IA, jobs asynchrones) et evaluation de librairies",
                "Presentation des resultats et recommandations - focus modernisation stack",
            ],
            "Next.js | React | TypeScript | OpenAI | Supabase | Git",
        ),
        (
            "Club Sport - Application multi-roles (SI interne)",
            "2025",
            [
                "Conception / developpement d'ecrans metier, droits, exports et supervision",
                "Travail structure : analyse, developpement, deploiement Docker",
            ],
            "Java | MySQL | Docker | Git | Agile",
        ),
    ]

    for title, date, bullets, stack in projects:
        p.text(m, 8.5, title, bold=True, color=TEXT)
        p.text_right(7.5, date, bold=True, color=LIGHT)
        p.y -= 11
        for b in bullets:
            p.bullet(b)
        p.text(m, 7.2, stack, bold=True, color=ACCENT)
        p.y -= 12

    p.section("Formation")
    p.text(m, 8.2, "Diplome d'Ingenieur - Dev Web Full Stack", bold=True, color=TEXT)
    p.text_right(7.5, "2024 - 2027", bold=True, color=LIGHT)
    p.y -= 10
    p.text(m, 7.6, "ESIGELEC - Rouen", bold=True, color=ACCENT)
    p.y -= 10
    p.multilines(
        7.4,
        "React, JavaScript, TypeScript, PHP, SQL, API REST, HTTPS, Git, Docker, Agile/Scrum, anglais",
        leading=9.6,
        color=MUTED,
    )
    p.space(3)
    p.text(m, 8.2, "Cycle preparatoire integre", bold=True, color=TEXT)
    p.text_right(7.5, "2022 - 2024", bold=True, color=LIGHT)
    p.y -= 10
    p.text(m, 7.6, "ESIGELEC - Cotonou, Benin", bold=True, color=ACCENT)
    p.y -= 12

    p.section("Experience")
    p.text(m, 8.2, "Stagiaire Informatique", bold=True, color=TEXT)
    p.text_right(7.5, "Juil. - Aout 2023", bold=True, color=LIGHT)
    p.y -= 10
    p.text(m, 7.6, "PROMOPHARMA - Benin", bold=True, color=ACCENT)
    p.y -= 10
    p.bullet("Rigueur, perserverance et respect des consignes sur support / maintenance")
    p.bullet("Communication transparente avec l'equipe et les utilisateurs en cas de blocage")

    p.section("Langues, disponibilite et centres d'interet")
    p.text(m, 8, "Langues", bold=True, color=TEXT)
    p.y -= 10
    p.multilines(
        7.5,
        "Francais : langue maternelle  |  Anglais : B2 (docs, specs, echanges en contexte international)",
        leading=9.8,
        color=MUTED,
    )
    p.space(3)
    p.text(m, 8, "Disponibilite & mobilite", bold=True, color=TEXT)
    p.y -= 10
    p.multilines(
        7.5,
        "Stage fin d'etudes 6 mois a partir de fevrier 2027  |  Mobilite Plouzane  |  Convention + gratification",
        leading=9.8,
        color=MUTED,
    )
    p.space(3)
    p.text(m, 8, "Centres d'interet techniques", bold=True, color=TEXT)
    p.y -= 10
    p.multilines(
        7.5,
        "React / SPA  |  PHP & API REST  |  Modernisation d'applications  |  POC & veille tech  |  GitHub",
        leading=9.8,
        color=MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = p.build()
    OUT.write_bytes(data)
    print(f"Wrote {OUT} ({len(data)} bytes), y_end={p.y:.0f}")


if __name__ == "__main__":
    main()

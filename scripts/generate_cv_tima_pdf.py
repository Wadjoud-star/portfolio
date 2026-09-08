#!/usr/bin/env python3
"""Génère assets/cv-tima.pdf — style blanc / violet (comme le CV HTML)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-tima.pdf"

# Palette (comme css/cv.css)
ACCENT = (0.263, 0.220, 0.659)      # #4338ca
ACCENT_DARK = (0.216, 0.188, 0.639) # #3730a3
TEXT = (0.067, 0.094, 0.153)        # #111827
MUTED = (0.290, 0.333, 0.408)       # #4a5568
LIGHT = (0.420, 0.447, 0.502)       # #6b7280
CHIP_BG = (0.878, 0.910, 1.0)       # #e0e7ff
RULE = (0.827, 0.827, 0.843)        # #d3d3d7


def esc(s: str) -> str:
    return (
        s.encode("latin-1", "replace")
        .decode("latin-1")
        .replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
    )


def rgb(c):
    return f"{c[0]:.3f} {c[1]:.3f} {c[2]:.3f}"


class PDF:
    def __init__(self):
        self.y = 812
        self.page_w = 595
        self.margin = 34
        self.content = []
        self._color = TEXT

    def fill(self, c):
        self._color = c
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
        # Approx Helvetica width
        factor = 0.52 if bold else 0.48
        return factor * size * len(string)

    def text_right(self, size, string, bold=False, color=None):
        w = self.text_w(string, size, bold)
        x = self.page_w - self.margin - w
        self.text(x, size, string, bold=bold, color=color)

    def multilines(self, size, text, leading=None, bold=False, color=None, max_w=None):
        leading = leading or (size + 2.2)
        max_w = max_w or (self.page_w - 2 * self.margin)
        words = text.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if self.text_w(test, size, bold) > max_w:
                self.text(self.margin, size, line, bold=bold, color=color)
                self.y -= leading
                line = w
            else:
                line = test
        if line:
            self.text(self.margin, size, line, bold=bold, color=color)
            self.y -= leading

    def rule(self, color=ACCENT, thickness=2.0):
        self.stroke(color)
        self.content.append(
            f"{thickness} w {self.margin} {self.y:.1f} m {self.page_w - self.margin} {self.y:.1f} l S"
        )
        self.y -= 9

    def thin_rule(self):
        self.rule(color=RULE, thickness=0.5)

    def space(self, n=6):
        self.y -= n

    def section(self, title):
        self.space(5)
        self.text(self.margin, 9.5, title.upper(), bold=True, color=ACCENT)
        self.y -= 3
        self.thin_rule()
        self.space(1)

    def chip(self, label, x, y):
        pad_x, pad_y = 6, 3
        tw = self.text_w(label, 7, bold=True)
        w, h = tw + pad_x * 2, 12
        # Pastille violet plein + texte blanc
        self.content.append(f"{rgb(ACCENT)} rg")
        self.content.append(f"{x:.1f} {y:.1f} {w:.1f} {h:.1f} re f")
        self.fill((1, 1, 1))
        self.content.append(
            f"BT /F2 7 Tf {x + pad_x:.1f} {y + 3.2:.1f} Td ({esc(label)}) Tj ET"
        )
        return w + 5

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
    right = p.page_w - m

    # ── En-tête ──
    # Bandeau violet léger
    p.content.append(f"{rgb(CHIP_BG)} rg")
    p.content.append(f"0 {p.y - 52:.1f} 595 70 re f")

    p.text(m, 20, "Wadjoud PHILIPPE", bold=True, color=TEXT)
    p.y -= 15
    p.text(m, 10.5, "Élève Ingénieur — Développeur Full Stack / IA", bold=True, color=ACCENT)
    p.y -= 12
    p.text(m, 8.5, "Stage de fin d'études (fév. 2027) · Mobilité Paris · ESIGELEC Rouen", color=MUTED)
    p.y -= 11
    p.text(m, 8, "wadjoud.philippe@groupe-esigelec.org  ·  07 58 03 02 39", color=ACCENT_DARK)
    p.y -= 10
    p.text(m, 8, "wadjoud-star.github.io/portfolio  ·  linkedin.com/in/wadjoud-philippe  ·  github.com/Wadjoud-star", color=ACCENT_DARK)
    p.y -= 8
    p.rule(thickness=2.4)

    # ── Profil ──
    p.section("Profil")
    p.multilines(
        8,
        "Élève ingénieur bac+5 (ESIGELEC, développement web full stack), je conçois des applications web "
        "de bout en bout : analyse métier, développement Java / Spring & React, API REST, Docker et déploiement. "
        "Intéressé par l'IA appliquée aux processus métier (OpenAI, automatisation), les plateformes multi-rôles "
        "(droits, admin, workflows) et les produits en production. Recherche un stage de fin d'études de 6 mois "
        "à partir de février 2027 — autonome, Agile/Scrum, force de proposition.",
        leading=10,
        color=MUTED,
    )

    # ── Compétences (2 colonnes) ──
    p.section("Compétences techniques")
    skills = [
        ("Backend", "Java, Spring Boot, Kotlin (bases), Node.js, Express, PHP, C#, Python, API REST, JWT"),
        ("Frontend", "React, Next.js, Angular, TypeScript, JavaScript, HTML/CSS, Tailwind, Bootstrap"),
        ("IA & Données", "OpenAI, LangChain (notions), PostgreSQL, MySQL, Prisma, Oracle SQL, MCD/MLD"),
        ("DevOps & Méthodes", "Docker, Kubernetes (notions), Git, CI/CD, Linux, Agile/Scrum, rôles & droits"),
    ]
    col_w = (p.page_w - 2 * m - 14) / 2
    start_y = p.y
    left_x = m
    right_x = m + col_w + 14

    def skill_block(x, title, body, y0):
        p.y = y0
        p.text(x, 8.5, title, bold=True, color=TEXT)
        p.y -= 11
        # wrap within column
        words = body.split()
        line = ""
        for w in words:
            test = (line + " " + w).strip()
            if p.text_w(test, 7.5) > col_w:
                p.text(x, 7.5, line, color=MUTED)
                p.y -= 9.5
                line = w
            else:
                line = test
        if line:
            p.text(x, 7.5, line, color=MUTED)
            p.y -= 9.5
        return p.y

    y_l = skill_block(left_x, skills[0][0], skills[0][1], start_y)
    y_r = skill_block(right_x, skills[1][0], skills[1][1], start_y)
    row2 = min(y_l, y_r) - 4
    y_l = skill_block(left_x, skills[2][0], skills[2][1], row2)
    y_r = skill_block(right_x, skills[3][0], skills[3][1], row2)
    p.y = min(y_l, y_r) - 2

    # ── Projets ──
    p.section("Projets significatifs")
    projects = [
        (
            "Smart CMS IA — Génération de contenu & OpenAI",
            "2025",
            "CMS intelligent : génération IA (blog, LinkedIn, X, illustration) via OpenAI, jobs asynchrones, éditeur riche, SEO, auth et historique de projets.",
            "Next.js · React · OpenAI · Supabase · Stripe · TipTap · TypeScript",
        ),
        (
            "Beniphone — Marketplace multi-rôles",
            "2025",
            "Catalogue, KYC vendeur, messagerie/négociation, transactions tracées, modération et dashboard admin. Rôles et workflows métier.",
            "React · Node.js · Express · Prisma · MySQL · Tailwind · Agile",
        ),
        (
            "Factis — Mini-SaaS facturation",
            "2025",
            "SaaS France/Bénin : onboarding, clients, factures PDF, analytics, Stripe, rôles et conformité. Produit, API et déploiement.",
            "Next.js · TypeScript · Prisma · PostgreSQL · Stripe · Docker",
        ),
        (
            "Club Sport — Application Java multi-rôles",
            "2025",
            "Recherche, cartographie, statistiques, exports CSV, espaces élu/club. Docker et Tomcat.",
            "Java · JSP/Servlets · MySQL · Docker · Tomcat",
        ),
        (
            "Mon Déménagement — Plateforme en production",
            "2025",
            "Mise en relation clients/déménageurs : annonces, offres, messagerie, évaluations, admin. Analyse → MVC → production.",
            "PHP · MySQL · MVC · Bootstrap · JavaScript · Git",
        ),
    ]
    for title, date, desc, stack in projects:
        p.text(m, 9, title, bold=True, color=TEXT)
        p.text_right(8, date, bold=True, color=LIGHT)
        p.y -= 11
        p.multilines(7.8, desc, leading=9.8, color=MUTED)
        p.text(m, 7.5, stack, bold=True, color=ACCENT)
        p.y -= 11

    # ── Formation + Expérience ──
    p.section("Formation")
    p.text(m, 8.5, "Diplôme d'Ingénieur — Dev Web Full Stack", bold=True, color=TEXT)
    p.text_right(8, "2024 – 2027", bold=True, color=LIGHT)
    p.y -= 10
    p.text(m, 8, "ESIGELEC · Rouen", bold=True, color=ACCENT)
    p.y -= 10
    p.multilines(7.8, "Java, Spring, Angular, TypeScript, React, Docker, API REST, Agile/Scrum", leading=9.8, color=MUTED)
    p.text(m, 8.5, "Cycle préparatoire intégré", bold=True, color=TEXT)
    p.text_right(8, "2022 – 2024", bold=True, color=LIGHT)
    p.y -= 10
    p.text(m, 8, "ESIGELEC · Cotonou, Bénin", bold=True, color=ACCENT)
    p.y -= 12

    p.section("Expérience")
    p.text(m, 8.5, "Stagiaire Informatique", bold=True, color=TEXT)
    p.text_right(8, "Juil. – Août 2023", bold=True, color=LIGHT)
    p.y -= 10
    p.text(m, 8, "PROMOPHARMA · Bénin", bold=True, color=ACCENT)
    p.y -= 10
    p.multilines(
        7.8,
        "Recueil des besoins, diagnostic d'incidents, maintenance parc informatique et serveurs.",
        leading=9.8,
        color=MUTED,
    )

    # ── Footer chips ──
    p.section("Langues · Qualités · Centres d'intérêt")
    p.multilines(7.8, "Français — langue maternelle  ·  Anglais — B2 (docs techniques, specs)", leading=9.8, color=MUTED)
    p.space(2)
    chips = ["Autonome", "Force de proposition", "Esprit d'équipe", "Agile", "IA & LLM"]
    x = m
    y_chip = p.y - 2
    for label in chips:
        w = p.chip(label, x, y_chip)
        x += w
    p.y = y_chip - 14
    p.multilines(
        7.8,
        "Produits SaaS & applications métier  ·  Open source / contributions GitHub",
        leading=9.8,
        color=MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = p.build()
    OUT.write_bytes(data)
    print(f"Wrote {OUT} ({len(data)} bytes), y_end={p.y:.0f}")


if __name__ == "__main__":
    main()

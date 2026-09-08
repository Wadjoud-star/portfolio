#!/usr/bin/env python3
"""Génère assets/cv-tima.pdf — style blanc/violet sobre (sans bandeau)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "cv-tima.pdf"

# Palette
ACCENT = (0.263, 0.220, 0.659)       # #4338ca
ACCENT_DARK = (0.216, 0.188, 0.639)  # #3730a3
TEXT = (0.067, 0.094, 0.153)         # #111827
MUTED = (0.290, 0.333, 0.408)        # #4a5568
LIGHT = (0.420, 0.447, 0.502)        # #6b7280
CHIP_BG = (0.878, 0.910, 1.0)        # #e0e7ff
RULE = (0.827, 0.827, 0.843)


def esc(s: str) -> str:
    """Encode PDF string en WinAnsi / latin-1 (pas de ? pour tirets spéciaux)."""
    replacements = {
        "\u2014": "-",   # —
        "\u2013": "-",   # –
        "\u2022": "-",   # •
        "\u2192": "->",  # →
        "\u00b7": "|",   # ·
        "\u2026": "...", # …
        "\u00a0": " ",   # nbsp
        "\u0153": "oe",  # œ
        "\u0152": "OE",
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
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
        factor = 0.52 if bold else 0.48
        return factor * size * len(string)

    def text_right(self, size, string, bold=False, color=None):
        w = self.text_w(string, size, bold)
        x = self.page_w - self.margin - w
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

    def bullet(self, text, size=7.6, leading=9.6, color=None):
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

    def space(self, n=5):
        self.y -= n

    def section(self, title):
        self.space(4)
        self.text(self.margin, 9.5, title.upper(), bold=True, color=ACCENT)
        self.y -= 3
        self.thin_rule()
        self.space(1)

    def chip(self, label, x, y):
        pad_x = 6
        tw = self.text_w(label, 7, bold=True)
        w, h = tw + pad_x * 2, 12
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

    # ── En-tête (sans bandeau / sans barre) ──
    p.text(m, 19, "Wadjoud PHILIPPE", bold=True, color=TEXT)
    p.y -= 14
    p.text(m, 10, "Eleve Ingenieur - Developpeur Full Stack / IA", bold=True, color=ACCENT)
    p.y -= 11
    p.text(m, 8.2, "Stage de fin d'etudes (fev. 2027) - Mobilite Paris - ESIGELEC Rouen", color=MUTED)
    p.y -= 10
    p.text(m, 7.8, "wadjoud.philippe@groupe-esigelec.org  |  07 58 03 02 39", color=ACCENT_DARK)
    p.y -= 9
    p.text(
        m,
        7.8,
        "wadjoud-star.github.io/portfolio  |  linkedin.com/in/wadjoud-philippe  |  github.com/Wadjoud-star",
        color=ACCENT_DARK,
    )
    p.y -= 7
    p.rule(thickness=2.2)

    # ── Profil ──
    p.section("Profil")
    p.multilines(
        7.8,
        "Eleve ingenieur bac+5 (ESIGELEC, developpement web full stack), je concois des applications web "
        "de bout en bout : analyse metier, developpement Java / Spring & React, API REST, Docker et deploiement. "
        "Interesse par l'IA appliquee aux processus metier (OpenAI, automatisation), les plateformes multi-roles "
        "(droits, admin, workflows) et les produits en production. Recherche un stage de fin d'etudes de 6 mois "
        "a partir de fevrier 2027 - autonome, Agile/Scrum, force de proposition.",
        leading=9.6,
        color=MUTED,
    )

    # ── Compétences ──
    p.section("Competences techniques")
    skills = [
        ("Backend", "Java, Spring Boot, Kotlin (bases), Node.js, Express, PHP, C#, Python, API REST, JWT"),
        ("Frontend", "React, Next.js, Angular, TypeScript, JavaScript, HTML/CSS, Tailwind, Bootstrap"),
        ("IA & Donnees", "OpenAI, LangChain (notions), PostgreSQL, MySQL, Prisma, Oracle SQL, MCD/MLD"),
        ("DevOps & Methodes", "Docker, Kubernetes (notions), Git, CI/CD, Linux, Agile/Scrum, roles & droits"),
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

    # ── Projets détaillés ──
    p.section("Projets significatifs")
    projects = [
        (
            "Smart CMS IA - Generation de contenu & OpenAI",
            "2025",
            [
                "Generation IA multi-formats : article blog, posts LinkedIn/X et illustration a partir d'un theme",
                "Jobs asynchrones avec suivi de progression, editeur riche TipTap et auto-sauvegarde",
                "Score SEO, export Markdown/HTML, authentification et historique de projets (Supabase)",
                "Parcours produit complet : generation, edition, optimisation puis export pour publication",
            ],
            "Next.js | React | OpenAI | Supabase | Stripe | TipTap | TypeScript",
        ),
        (
            "Beniphone - Marketplace multi-roles",
            "2025",
            [
                "Catalogue Apple avec filtres, KYC vendeur et moderation d'annonces avant publication",
                "Messagerie de negociation de prix tracee, accords enregistres puis finalisation WhatsApp",
                "Espaces acheteur, vendeur et admin : transactions, litiges et validation des dossiers",
                "Gestion des droits par role et workflows metier de bout en bout",
            ],
            "React | Node.js | Express | Prisma | MySQL | Tailwind | Agile",
        ),
        (
            "Factis - Mini-SaaS facturation",
            "2025",
            [
                "Facturation conforme France (TVA, SIRET) et Benin (FCFA, IFU) pour freelances",
                "Clients, factures PDF, depenses, analytics, abonnement Stripe Gratuit/Pro",
                "Onboarding legal, roles utilisateur et deploiement production (PostgreSQL)",
                "Tableaux de bord de suivi financier et process de paiement",
            ],
            "Next.js | TypeScript | Prisma | PostgreSQL | Stripe | Docker",
        ),
        (
            "Club Sport - Application Java multi-roles",
            "2025",
            [
                "Recherche de clubs (federation, commune, rayon) et cartographie interactive",
                "Dashboards elu : statistiques de licences, exports CSV, cartographie choroplèthe",
                "Espace club : actualites, horaires, cotisations - conteneurisation Docker/Tomcat",
            ],
            "Java | JSP/Servlets | MySQL | Docker | Tomcat",
        ),
        (
            "Mon Demenagement - Plateforme en production",
            "2025",
            [
                "Mise en relation clients / demenageurs : annonces, photos, propositions de prix",
                "Messagerie interne, evaluations et espace admin de supervision",
                "Cycle complet analyse (MCD) -> architecture MVC -> mise en ligne",
            ],
            "PHP | MySQL | MVC | Bootstrap | JavaScript | Git",
        ),
    ]

    for title, date, bullets, stack in projects:
        p.text(m, 8.5, title, bold=True, color=TEXT)
        p.text_right(7.5, date, bold=True, color=LIGHT)
        p.y -= 10
        for b in bullets:
            p.bullet(b)
        p.text(m, 7.2, stack, bold=True, color=ACCENT)
        p.y -= 9

    # ── Formation ──
    p.section("Formation")
    p.text(m, 8.2, "Diplome d'Ingenieur - Dev Web Full Stack", bold=True, color=TEXT)
    p.text_right(7.5, "2024 - 2027", bold=True, color=LIGHT)
    p.y -= 9
    p.text(m, 7.6, "ESIGELEC - Rouen", bold=True, color=ACCENT)
    p.y -= 9
    p.multilines(
        7.4,
        "Java, Spring, Angular, TypeScript, React, Docker, API REST, Agile/Scrum",
        leading=9.2,
        color=MUTED,
    )
    p.text(m, 8.2, "Cycle preparatoire integre", bold=True, color=TEXT)
    p.text_right(7.5, "2022 - 2024", bold=True, color=LIGHT)
    p.y -= 9
    p.text(m, 7.6, "ESIGELEC - Cotonou, Benin", bold=True, color=ACCENT)
    p.y -= 10

    # ── Expérience ──
    p.section("Experience")
    p.text(m, 8.2, "Stagiaire Informatique", bold=True, color=TEXT)
    p.text_right(7.5, "Juil. - Aout 2023", bold=True, color=LIGHT)
    p.y -= 9
    p.text(m, 7.6, "PROMOPHARMA - Benin", bold=True, color=ACCENT)
    p.y -= 9
    p.bullet("Recueil des besoins utilisateurs et diagnostic d'incidents techniques")
    p.bullet("Maintenance du parc informatique et des serveurs de l'entreprise")

    # ── Footer ──
    p.section("Langues | Qualites | Centres d'interet")
    p.multilines(
        7.4,
        "Francais - langue maternelle  |  Anglais - B2 (docs techniques, specs)",
        leading=9.2,
        color=MUTED,
    )
    p.space(2)
    chips = ["Autonome", "Force de proposition", "Esprit d'equipe", "Agile", "IA & LLM"]
    x = m
    y_chip = p.y - 1
    for label in chips:
        x += p.chip(label, x, y_chip)
    p.y = y_chip - 13
    p.multilines(
        7.4,
        "Produits SaaS & applications metier  |  Open source / contributions GitHub",
        leading=9.2,
        color=MUTED,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    data = p.build()
    OUT.write_bytes(data)
    print(f"Wrote {OUT} ({len(data)} bytes), y_end={p.y:.0f}")
    if p.y < 40:
        print("WARNING: content may overflow page")
    elif p.y > 120:
        print("NOTE: still some empty space at bottom")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Génère content/etagere.md (la page « Mon étagère ») à partir de data/bookshelf.csv.

Usage : python scripts/gen_etagere.py
À relancer après chaque réexport de la bibliothèque (data/bookshelf.csv).
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "data", "bookshelf.csv")
OUT = os.path.join(ROOT, "content", "etagere.md")

# Ordre d'affichage des rayons.
ORDER = [
    "Canada français et Ontario français",
    "Politique, économie et idées",
    "Littérature et nouvelles",
    "Bandes dessinées",
    "Sciences, génie et informatique",
    "Cuisine, musique et divers",
]


def bucket(tags):
    t = set(x.strip() for x in tags.split(",") if x.strip())
    if t & {"Franco-Ontarien", "Canadien-Français"}:
        return ORDER[0]
    if "Bande dessinée" in t:
        return ORDER[3]
    if "Académique" in t:
        return ORDER[4]
    if t & {"Cuisine", "Musique"}:
        return ORDER[5]
    if "Économie" in t:
        return ORDER[1]
    if t & {"Littérature étrangère", "Fiction", "Nouvelles"}:
        return ORDER[2]
    if t & {"Politique", "Essai", "Philosophie", "Histoire", "Culture", "Identité"}:
        return ORDER[1]
    return ORDER[5]


def main():
    rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
    seen = set()
    shelves = {k: [] for k in ORDER}
    for r in rows:
        title = (r.get("Title") or "").strip()
        author = (r.get("Authors") or "").strip()
        if not title:
            continue
        key = title.lower()
        if key in seen:
            continue
        seen.add(key)
        shelves[bucket((r.get("Tags") or ""))].append((title, author))

    total = sum(len(v) for v in shelves.values())
    lines = [
        "---",
        'title: "Mon étagère"',
        "date: 2026-06-21",
        "draft: false",
        'description: "Tout ce que je lis. Une bibliothèque est un autoportrait fait sans poser : on n\'y range pas ce qu\'on veut montrer, mais ce qui nous a formé."',
        "---",
        "",
        "Une bibliothèque est un autoportrait fait sans poser. On n'achète pas un livre pour qu'on nous voie le lire, mais parce que quelque chose a tiré. Année après année, ça finit par dessiner la forme de ce qu'on a laissé entrer en soi.",
        "",
        f"Voici la mienne, à ce jour : {total} titres.",
        "",
    ]
    for shelf in ORDER:
        books = sorted(shelves[shelf], key=lambda x: x[0].lower())
        if not books:
            continue
        lines.append(f"## {shelf}")
        lines.append("")
        for title, author in books:
            lines.append(f"- *{title}*" + (f" — {author}" if author else ""))
        lines.append("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    print(f"Écrit {OUT} : {total} titres répartis en {sum(1 for s in ORDER if shelves[s])} rayons.")


if __name__ == "__main__":
    main()

"""Build the English academic homepage using only the Python standard library."""

import html
import json
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]


def escape(value):
    return html.escape(str(value), quote=True)


def publication(paper):
    authors = escape(paper["authors"]).replace("Yu Jiang", '<strong class="self-author">Yu Jiang</strong>')
    title = escape(paper["title"])
    links = paper.get("links", {})
    primary = links.get("Paper") or links.get("Project") or links.get("PDF")
    if primary:
        title = f'<a href="{escape(primary)}">{title}</a>'
    resources = "".join(f'<a href="{escape(url)}">{escape(label)}<span aria-hidden="true"> ↗</span></a>'
                        for label, url in links.items())
    note = f'<span class="publication-note">{escape(paper["note"])}</span>' if paper.get("note") else ""
    return (f'<article class="publication" id="{escape(paper["id"])}">'
            f'<div class="pub-marker" aria-hidden="true">{escape(paper["short"])}</div>'
            f'<div class="pub-content"><h4>{title}</h4><p class="authors">{authors}</p>'
            f'<p class="venue">{escape(paper["venue"])}{note}</p>'
            + (f'<div class="paper-links" aria-label="Resources for {escape(paper["title"])}">{resources}</div>' if resources else "")
            + '</div></article>')


def group_publications(papers):
    groups = []
    for year in sorted({p["year"] for p in papers}, reverse=True):
        rows = "\n".join(publication(p) for p in papers if p["year"] == year)
        groups.append(f'<div class="publication-year"><h3>{year}</h3><div>{rows}</div></div>')
    return "\n".join(groups)


def main():
    papers = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
    assert len({p["id"] for p in papers}) == len(papers), "Publication IDs must be unique"
    assert all("Yu Jiang" in p["authors"] for p in papers), "Check author lists"
    for p in papers:
        assert not any("\u4e00" <= c <= "\u9fff" for c in p["title"]), "English titles required"
    core = [p for p in papers if p["category"] == "computer-science"]
    template = Template((ROOT / "templates/home.html").read_text(encoding="utf-8"))
    result = template.substitute(publications=group_publications(core))
    (ROOT / "index.html").write_text(result, encoding="utf-8", newline="\n")
    print(f"Built index.html: {len(core)} computer science papers.")


if __name__ == "__main__":
    main()

# Yu Jiang's academic homepage

Live site: <https://jiangyu1181.github.io/>

An English academic homepage for Yu Jiang, a Ph.D. student at Wuhan University.
The visual direction adapts the [Minimal Light](https://github.com/yaoyao-liu/minimal-light)
academic template, with a custom responsive layout and no client-side framework.

## Editing

- `data/publications.json` contains publication titles, authors, venues, years, and verified resource links.
  Only entries categorized as `computer-science` are displayed on the homepage.
- `templates/home.html` contains the profile, biography, and research spotlight.
- `assets/style.css` controls the layout and typography.
- `assets/yu-jiang.jpg` is the portrait supplied in the academic CV.
- `S2R/` is the existing project page. Its files were preserved during the homepage redesign.

After editing the publication data or template, regenerate the committed homepage:

```text
python scripts/build.py
```

Preview locally:

```text
python -m http.server 8765 --bind 127.0.0.1
```

GitHub Pages publishes `main` from the repository root. `.nojekyll` selects direct
static serving. No package installation, external font service, analytics, or
JavaScript is required to read the homepage.

## Content sources

The biography, education, project roles, honors, portrait, and initial publication
list came from the owner's academic CV on September 4, 2026. Publication metadata
was checked against publisher and conference records linked in the data file.

- JumpingGS uses the official title spelling, “Level-jump”.
- The Fudan journal paper is listed under its 2025 issue year, with its 2024 online date noted.
- The Journal of Chinese Governance paper is listed under its 2026 issue year, with its 2025 online date noted.
- The Current Opinion in Psychiatry item retains the e-Supplement 2 designation and entry number.
- S2R links to the existing project page. Its supplied DOI had not resolved on the verification date.
- The 2020 change-detection paper retains the owner's English bibliographic record without an unverified URL.
- The Cancer Nursing entry retains the owner's author list. Its title and journal were corroborated by an [institutional announcement](https://law.ahnu.edu.cn/info/1073/42216.htm). No unverified DOI is shown.

Award and project descriptions were translated from the owner's Chinese CV.
The academic homepage does not publish the CV's mobile number or project agreement identifiers.

## Design credit

The [Minimal Light](https://github.com/yaoyao-liu/minimal-light) template is released
under [CC0 1.0](https://github.com/yaoyao-liu/minimal-light/blob/main/LICENSE).
This site adapts its profile sidebar and academic publication layout with custom
HTML and CSS. Research images, papers, and the portrait remain with their respective owners.

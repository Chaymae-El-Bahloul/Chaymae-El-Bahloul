#!/usr/bin/env python3
"""
README-as-a-pipeline.

EXTRACT   GitHub REST API (public repositories, languages, recent commits)
TRANSFORM aggregate and rank the numbers (Python standard library only)
LOAD      assets/pipeline-en.svg + assets/pipeline-fr.svg + data/history.csv
          + status block in README.md (English) and README.fr.md (French)

Run daily by .github/workflows/pipeline.yml. No third-party dependency.
"""
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
USER = os.environ.get("GH_USER", "Chaymae-El-Bahloul")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
HISTORY = ROOT / "data" / "history.csv"
LANGS = ("en", "fr")


def svg_path(lang):
    return ROOT / "assets" / f"pipeline-{lang}.svg"


def readme_path(lang):
    name = "README.md" if lang == "en" else "README.fr.md"
    p = ROOT / name
    if not p.exists() and lang == "en" and (ROOT / "Readme.md").exists():
        p = ROOT / "Readme.md"
    return p


# All visible text, per language.
I18N = {
    "en": {
        "aria": "Live data pipeline that rebuilds this profile every day: extract from the GitHub API, transform with Python, load into this README",
        "title": "pipeline.py  --  this profile is the output of a data pipeline",
        "runs": "runs daily 00:00 UTC",
        "extract": "EXTRACT", "transform": "TRANSFORM", "load": "LOAD",
        "api": "GitHub REST API", "repos": "repositories", "calls": "API calls",
        "stdlib": "Python, standard library only", "ranked": "languages ranked",
        "commits_days": "commits, {d} days", "loadsub": "README + SVG + CSV",
        "langs_title": "Languages, share of code bytes", "last30": "Last 30 days",
        "commits": "commits", "projects": "public projects",
        "trend": "Commit trend, one point per run",
        "collecting": "collecting history", "points": "data point(s) so far",
        "await": "Awaiting the first run", "await2": "Actions tab > Update pipeline > Run workflow",
        "foot": "last run {time}  |  run #{n}  |  most recent push: {repo}",
        "foot_wait": "status: waiting for the first scheduled run",
        "log_extract": "extract", "log_transform": "transform", "log_load": "load", "log_last": "last run",
        "log_repos": "{n} repositories, {c} API calls",
        "log_langs": "{l} languages, {k} commits in {d} days",
    },
    "fr": {
        "aria": "Pipeline de données en direct qui reconstruit ce profil chaque jour : extraction depuis l'API GitHub, transformation avec Python, chargement dans ce README",
        "title": "pipeline.py  --  ce profil est le résultat d'un pipeline de données",
        "runs": "exécuté chaque jour à 00:00 UTC",
        "extract": "EXTRACTION", "transform": "TRANSFORMATION", "load": "CHARGEMENT",
        "api": "API REST GitHub", "repos": "dépôts", "calls": "appels API",
        "stdlib": "Python, bibliothèque standard", "ranked": "langages classés",
        "commits_days": "commits, {d} jours", "loadsub": "README + SVG + CSV",
        "langs_title": "Langages, part des octets de code", "last30": "30 derniers jours",
        "commits": "commits", "projects": "projets publics",
        "trend": "Tendance, un point par exécution",
        "collecting": "historique en cours de collecte", "points": "point(s) pour l'instant",
        "await": "En attente de la première exécution", "await2": "Onglet Actions > Update pipeline > Run workflow",
        "foot": "dernière exécution {time}  |  n°{n}  |  dernier push : {repo}",
        "foot_wait": "statut : en attente de la première exécution planifiée",
        "log_extract": "extraction", "log_transform": "transformation", "log_load": "chargement", "log_last": "dernière exécution",
        "log_repos": "{n} dépôts, {c} appels API",
        "log_langs": "{l} langages, {k} commits sur {d} jours",
    },
}
WINDOW_DAYS = 30
MAX_REPOS = 40

C_BG, C_EDGE = "#0B1020", "#1F2A44"
C_ORANGE, C_TEAL, C_PURPLE = "#FF6B35", "#14B8A6", "#8B5CF6"
C_TEXT, C_MUTED = "#E2E8F0", "#94A3B8"


# ----------------------------------------------------------------- EXTRACT
def api(path):
    url = f"https://api.github.com{path}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "readme-pipeline"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 409:  # empty repository
                return []
            if attempt == 2:
                raise
        except urllib.error.URLError:
            if attempt == 2:
                raise
        time.sleep(2 * (attempt + 1))


def extract():
    repos = api(f"/users/{USER}/repos?per_page=100&type=owner&sort=pushed")
    repos = [r for r in repos if not r["fork"] and r["name"].lower() != USER.lower()][:MAX_REPOS]
    since = (datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    raw = []
    for r in repos:
        langs = api(f"/repos/{USER}/{r['name']}/languages") or {}
        commits = api(f"/repos/{USER}/{r['name']}/commits?author={USER}&since={since}&per_page=100") or []
        raw.append({"name": r["name"], "pushed_at": r["pushed_at"], "languages": langs, "commits": len(commits)})
    return raw


# --------------------------------------------------------------- TRANSFORM
def transform(raw):
    bytes_by_lang = {}
    for r in raw:
        for lang, n in r["languages"].items():
            bytes_by_lang[lang] = bytes_by_lang.get(lang, 0) + n
    total = sum(bytes_by_lang.values()) or 1
    ranked = sorted(bytes_by_lang.items(), key=lambda kv: kv[1], reverse=True)
    top = [(lang, round(100 * n / total, 1)) for lang, n in ranked[:5]]
    latest = max(raw, key=lambda r: r["pushed_at"]) if raw else None
    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "time": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "repos": len(raw),
        "languages": len(bytes_by_lang),
        "commits_30d": sum(r["commits"] for r in raw),
        "bytes": total if bytes_by_lang else 0,
        "top": top,
        "latest_repo": latest["name"] if latest else "-",
        "api_calls": 1 + 2 * len(raw),
    }


# -------------------------------------------------------------------- LOAD
def load_history(snapshot):
    rows = []
    if HISTORY.exists():
        with HISTORY.open(newline="") as f:
            rows = list(csv.DictReader(f))
    rows = [r for r in rows if r["date"] != snapshot["date"]]
    rows.append({
        "date": snapshot["date"],
        "repos": snapshot["repos"],
        "commits_30d": snapshot["commits_30d"],
        "bytes": snapshot["bytes"],
        "top_language": snapshot["top"][0][0] if snapshot["top"] else "-",
    })
    rows = rows[-120:]
    HISTORY.parent.mkdir(exist_ok=True)
    with HISTORY.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "repos", "commits_30d", "bytes", "top_language"])
        w.writeheader()
        w.writerows(rows)
    return rows


def t(x, y, text, size=13, fill=C_TEXT, weight="400", mono=True, anchor="start", extra=""):
    fam = "SFMono-Regular,Consolas,'Liberation Mono',monospace" if mono else "Segoe UI,Helvetica,Arial,sans-serif"
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}" {extra}>{escape(str(text))}</text>')


def stage(x, color, num, title, sub, l1, l2):
    return (
        f'<rect x="{x}" y="70" width="250" height="110" rx="12" fill="#111A33" stroke="{color}" stroke-width="1.5"/>'
        f'<rect x="{x}" y="70" width="6" height="110" rx="3" fill="{color}"/>'
        + t(x + 22, 98, f"{num}  {title}", 15, color, "700")
        + t(x + 22, 121, sub, 12, C_TEXT, mono=False)
        + t(x + 22, 147, l1, 12, C_MUTED)
        + t(x + 22, 166, l2, 12, C_MUTED)
    )


def flow(x1, x2, color, uid):
    out = f'<path id="{uid}" d="M{x1} 125 L{x2} 125" stroke="{C_EDGE}" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
    for i in range(3):
        out += (f'<circle r="4.5" fill="{color}"><animateMotion dur="1.8s" begin="{i * 0.6}s" '
                f'repeatCount="indefinite"><mpath href="#{uid}"/></animateMotion>'
                f'<animate attributeName="opacity" values="0;1;1;0" dur="1.8s" begin="{i * 0.6}s" repeatCount="indefinite"/></circle>')
    return out


def sparkline(rows, x, y, w, h, L):
    vals = [int(r["commits_30d"]) for r in rows][-30:]
    if len(vals) < 2:
        return (t(x + w / 2, y + h / 2 - 4, L["collecting"], 12, C_MUTED, anchor="middle")
                + t(x + w / 2, y + h / 2 + 14, f"{len(vals)} {L['points']}", 11, C_MUTED, anchor="middle"))
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1
    pts = [(x + i * w / (len(vals) - 1), y + h - (v - lo) / span * h) for i, v in enumerate(vals)]
    poly = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    area = f"{x},{y + h} " + poly + f" {x + w},{y + h}"
    return (
        f'<polygon points="{area}" fill="{C_PURPLE}" opacity="0.15"/>'
        f'<polyline points="{poly}" fill="none" stroke="{C_PURPLE}" stroke-width="2.5" stroke-linejoin="round" '
        f'stroke-dasharray="1200" stroke-dashoffset="0"><animate attributeName="stroke-dashoffset" '
        f'from="1200" to="0" dur="2.4s" fill="freeze"/></polyline>'
        f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="4" fill="{C_ORANGE}"/>'
        + t(x, y + h + 18, f"min {lo}", 11, C_MUTED) + t(x + w, y + h + 18, f"max {hi}", 11, C_MUTED, anchor="end")
    )


def render_svg(s, rows, lang="en"):
    L = I18N[lang]
    ready = s is not None
    top = s["top"] if ready else []
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 450" width="1000" height="450" role="img" '
        f'aria-label="{escape(L["aria"], {chr(34): "&quot;"})}">',
        f'<rect width="1000" height="450" rx="18" fill="{C_BG}" stroke="{C_EDGE}"/>',
        '<circle cx="30" cy="30" r="6" fill="#FF5F57"/><circle cx="50" cy="30" r="6" fill="#FEBC2E"/><circle cx="70" cy="30" r="6" fill="#28C840"/>',
        t(95, 35, L["title"], 13, C_MUTED),
        t(960, 35, L["runs"], 12, C_MUTED, anchor="end"),
        stage(40, C_ORANGE, "01", L["extract"], L["api"],
              f"{s['repos']} {L['repos']}" if ready else f"-- {L['repos']}",
              f"{s['api_calls']} {L['calls']}" if ready else f"-- {L['calls']}"),
        stage(375, C_TEAL, "02", L["transform"], L["stdlib"],
              f"{s['languages']} {L['ranked']}" if ready else f"-- {L['ranked']}",
              f"{s['commits_30d']} " + L["commits_days"].format(d=WINDOW_DAYS) if ready else "-- " + L["commits_days"].format(d=WINDOW_DAYS)),
        stage(710, C_PURPLE, "03", L["load"], L["loadsub"],
              f"assets/pipeline-{lang}.svg", "data/history.csv"),
        flow(290, 375, C_ORANGE, "f1"),
        flow(625, 710, C_TEAL, "f2"),
        # panels
        f'<rect x="40" y="205" width="440" height="190" rx="12" fill="#111A33" stroke="{C_EDGE}"/>',
        t(60, 232, L["langs_title"], 13, C_TEXT, "700", mono=False),
    ]
    palette = [C_ORANGE, C_TEAL, C_PURPLE, "#38BDF8", "#F59E0B"]
    if ready and top:
        for i, (lang, pct) in enumerate(top):
            y = 262 + i * 27
            width = max(4, pct / max(p for _, p in top) * 220)
            parts.append(t(60, y + 4, lang, 12, C_TEXT))
            parts.append(f'<rect x="165" y="{y - 8}" width="220" height="12" rx="6" fill="{C_EDGE}"/>')
            parts.append(f'<rect x="165" y="{y - 8}" width="{width:.0f}" height="12" rx="6" fill="{palette[i]}">'
                         f'<animate attributeName="width" from="0" to="{width:.0f}" dur="1.2s" begin="{i * 0.15}s" fill="freeze"/></rect>')
            parts.append(t(400, y + 4, f"{pct}%", 12, C_MUTED))
    else:
        parts.append(t(260, 315, L["await"], 14, C_MUTED, mono=False, anchor="middle"))
        parts.append(t(260, 337, L["await2"], 11, C_MUTED, anchor="middle"))

    parts += [
        f'<rect x="500" y="205" width="200" height="190" rx="12" fill="#111A33" stroke="{C_EDGE}"/>',
        t(520, 232, L["last30"], 13, C_TEXT, "700", mono=False),
        t(520, 285, str(s["commits_30d"]) if ready else "--", 38, C_ORANGE, "700", mono=False),
        t(520, 305, L["commits"], 12, C_MUTED, mono=False),
        t(520, 352, str(s["repos"]) if ready else "--", 38, C_TEAL, "700", mono=False),
        t(520, 372, L["projects"], 12, C_MUTED, mono=False),
        f'<rect x="720" y="205" width="240" height="190" rx="12" fill="#111A33" stroke="{C_EDGE}"/>',
        t(740, 232, L["trend"], 13, C_TEXT, "700", mono=False),
        sparkline(rows, 745, 262, 190, 90, L) if rows else "",
        # footer
        '<circle cx="48" cy="423" r="5" fill="#28C840"><animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/></circle>',
        t(62, 427, (L["foot"].format(time=s["time"], n=len(rows), repo=s["latest_repo"])
                    if ready else L["foot_wait"]), 12, C_MUTED),
        '</svg>',
    ]
    return "\n".join(parts)


def update_readme(s, rows, lang):
    path = readme_path(lang)
    if not path.exists():
        return
    L = I18N[lang]
    pad = max(len(L["log_extract"]), len(L["log_transform"]), len(L["log_load"]), len(L["log_last"]))

    def line(tag, key, text):
        return f"[{tag}] {L[key]} " + "." * (pad - len(L[key]) + 4) + f" {text}"

    block = "\n".join([
        "<!--PIPELINE:START-->",
        "```text",
        "$ ./pipeline --status",
        "",
        line("  OK  ", "log_extract", L["log_repos"].format(n=s["repos"], c=s["api_calls"])),
        line("  OK  ", "log_transform", L["log_langs"].format(l=s["languages"], k=s["commits_30d"], d=WINDOW_DAYS)),
        line("  OK  ", "log_load", f"assets/pipeline-{lang}.svg, data/history.csv"),
        line(" INFO ", "log_last", f"{s['time']} (run #{len(rows)})"),
        "```",
        "<!--PIPELINE:END-->",
    ])
    text = path.read_text(encoding="utf-8")
    new = re.sub(r"<!--PIPELINE:START-->.*?<!--PIPELINE:END-->", lambda _: block, text, flags=re.S)
    if new != text:
        path.write_text(new, encoding="utf-8")


def main():
    if "--placeholder" in sys.argv:  # initial asset, before any real run
        for lang in LANGS:
            svg_path(lang).write_text(render_svg(None, [], lang), encoding="utf-8")
        return
    snapshot = transform(extract())
    rows = load_history(snapshot)
    for lang in LANGS:
        svg_path(lang).write_text(render_svg(snapshot, rows, lang), encoding="utf-8")
        update_readme(snapshot, rows, lang)
    print(json.dumps(snapshot, indent=2))


if __name__ == "__main__":
    main()
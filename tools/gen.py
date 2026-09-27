#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""index.html と assets/i18n.js を tools/content.py から書き出す（#513）。

    python3 tools/gen.py

**index.html を手で直さない** —— 次に走らせると消える。文言は content.py、
形はこのファイル、見た目は assets/styles.css。releases.html は手書き（文言の鍵だけ i18n.js）。
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import UI, HEADS, SHOTS, THEME_SHOTS, FEATURES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape

en, ja = {}, {}
for k, a, b in UI:
    en[k], ja[k] = a, b
for f, a, b, _ in SHOTS:
    en["shot." + f], ja["shot." + f] = a, b
for i, (area_en, area_ja, items) in enumerate(FEATURES, 1):
    en[f"fa.{i}"], ja[f"fa.{i}"] = area_en, area_ja
    for j, (a, b) in enumerate(items, 1):
        en[f"f.{i}.{j}"], ja[f"f.{i}.{j}"] = a, b
en["doc.title"] = "dopamine — a macOS browser with panes, a terminal, files and an editor"
ja["doc.title"] = "dopamine — ペインで割れる macOS のブラウザ（ターミナル・Files・エディタ入り）"

total = sum(len(items) for _, _, items in FEATURES)


def t(key, tag="span", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i18n="{key}">{e(en[key])}</{tag}>'


def head(key):
    for k, j, g in HEADS:
        if k == key:
            return f'<h2 class="bi"><span lang="ja">{e(j)}</span><span class="bi__sep">—</span><span lang="en">{e(g.upper())}</span></h2>'
    raise KeyError(key)


def shot(f, big=False, eager=False):
    cls = "shot shot--big" if big else "shot"
    load = "eager" if eager else "lazy"
    w, h = (2400, 1577) if f not in ("settings-themes", "settings-editor", "settings-filter") else (1640, 1200)
    return (
        f'<figure class="{cls}">'
        f'<button type="button" class="shot__zoom" data-full="./assets/shots/{f}.webp" aria-label="Enlarge">'
        f'<img src="./assets/shots/{f}.webp" width="{w}" height="{h}" loading="{load}" decoding="async" alt="{e(en["shot." + f])}" data-i18n-alt="shot.{f}">'
        f"</button>"
        f'<figcaption>{t("shot." + f)}</figcaption></figure>'
    )


rows = []
for i, (_, _, items) in enumerate(FEATURES, 1):
    lis = "".join(f'<li>{t(f"f.{i}.{j}")}</li>' for j in range(1, len(items) + 1))
    rows.append(
        f'<tr><td class="no">{i:02d}</td><td class="area">{t(f"fa.{i}")}</td><td class="what"><ul>{lis}</ul></td></tr>'
    )

big = [s for s in SHOTS if s[3]]
small = [s for s in SHOTS if not s[3]]
themes = "".join(
    f'<figure class="theme"><button type="button" class="shot__zoom" data-full="./assets/shots/{f}.webp" aria-label="Enlarge">'
    f'<img src="./assets/shots/{f}.webp" width="1600" height="1051" loading="lazy" decoding="async" alt="{e(name)}"></button>'
    f"<figcaption>{e(name)}</figcaption></figure>"
    for f, name in THEME_SHOTS
)

page = f"""<!DOCTYPE html>
<!-- 生成物（tools/gen.py）。手で直さない。文言は tools/content.py。 -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{e(en["doc.title"])}</title>
<meta name="description" content="{e(en["tagline"])}">
<link rel="icon" href="./assets/favicon.png" sizes="64x64">
<link rel="apple-touch-icon" href="./assets/apple-touch-icon.png">
<meta property="og:title" content="dopamine">
<meta property="og:description" content="{e(en["tagline"])}">
<meta property="og:image" content="https://route23.github.io/dopamine-releases/assets/shots/workspace.webp">
<meta property="og:url" content="https://route23.github.io/dopamine-releases/">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@500;600;700;800&display=swap">
<link rel="stylesheet" href="./assets/styles.css">
<script src="./assets/i18n.js" defer></script>
<script src="./assets/site.js" defer></script>
<script src="./assets/app.js" defer></script>
</head>
<body>

<nav class="lang" aria-label="Language">
  <button type="button" data-lang="en" aria-pressed="true">EN</button><button type="button" data-lang="ja" aria-pressed="false">JA</button>
</nav>

<main class="sheet">

  <header class="mast">
    <span class="stamp" aria-hidden="true"><span>BETA</span><span>v0.1</span></span>
    <img class="mast__icon" src="./assets/dopamine.png" width="512" height="512" alt="">
    <h1 class="wordmark">dopamine</h1>
    <p class="mast__url">route23.github.io/dopamine-releases</p>
    {t("tagline", "p", "mast__tagline")}
    {t("spec", "p", "mast__spec")}
    <!--
      ダウンロードリンクは **ここに書いてある状態で既に動く**。
      assets/app.js は href とラベルを上書きするだけで、失敗しても
      このリンクはそのまま残る（JS 無効・レート制限・オフラインでも押せる）。
    -->
    <div class="download">
      <a id="download-primary" class="btn" href="https://github.com/Route23/dopamine-releases/releases/latest" data-i18n="download">{e(en["download"])}</a>
      <p id="download-meta" class="download__meta"></p>
      <p class="status" data-degraded-note hidden>{t("degraded")}</p>
    </div>
  </header>

  <section id="screens" class="block">
    {head("h.screens")}
    {t("screens.lead", "p", "lead")}
    {"".join(shot(f, True, True) for f, *_ in big)}
    <div class="shots">{"".join(shot(f) for f, *_ in small)}</div>
    <h3 class="bi bi--sub"><span lang="ja">テーマ</span><span class="bi__sep">—</span><span lang="en">THEMES</span></h3>
    <div class="themes">{themes}</div>
  </section>

  <section id="features" class="block">
    {head("h.features")}
    <p class="lead"><span data-i18n="features.lead">{e(en["features.lead"])}</span> <span class="count">{total}</span></p>
    <div class="table-wrap">
    <table class="spec">
      <thead><tr><th class="no">{t("th.no")}</th><th class="area">{t("th.area")}</th><th>{t("th.what")}</th></tr></thead>
      <tbody>{"".join(rows)}</tbody>
    </table>
    </div>
    {t("legend", "p", "legend")}
  </section>

  <section id="install" class="block">
    {head("h.install")}
    <div class="grid2">
      <div class="box">
        {t("install.brew", "h3")}
        <div class="cmd"><pre><code>brew install --cask Route23/tap/dopamine</code></pre><button type="button" class="cmd__copy" data-i18n="copy">Copy</button></div>
        {t("install.brew.note", "p", "small")}
      </div>
      <div class="box">
        {t("install.dmg", "h3")}
        {t("install.dmg.body", "p")}
        <div class="cmd"><pre><code>xattr -dr com.apple.quarantine /Applications/dopamine.app</code></pre><button type="button" class="cmd__copy" data-i18n="copy">Copy</button></div>
      </div>
    </div>
    <table class="req">
      <tr><td class="no">I</td><td>{t("req.os")}</td></tr>
      <tr><td class="no">II</td><td>{t("req.cpu")}</td></tr>
      <tr><td class="no">III</td><td>{t("updates")}</td></tr>
    </table>
  </section>

  <footer class="colophon">
    <p class="colophon__mark">dopamine <span>N°</span> 0.1</p>
    <div class="colophon__row">
      <div class="barcode" aria-hidden="true"><span></span><code>3 0 1 2 3 0 0 0 5 1 3</code></div>
      <nav class="colophon__links">
        <a href="./releases.html" data-i18n="footer.releases">{e(en["footer.releases"])}</a>
        <a href="https://github.com/Route23/dopamine-issues/issues" data-i18n="footer.bug">{e(en["footer.bug"])}</a>
        <a href="https://github.com/Route23/dopamine-releases" data-i18n="footer.github">GitHub</a>
      </nav>
    </div>
    {t("made", "p", "colophon__made")}
  </footer>

</main>

<dialog class="lightbox" aria-label="Screenshot"><img alt=""><button type="button" class="lightbox__close" aria-label="Close">×</button></dialog>

</body>
</html>
"""

with open(os.path.join(ROOT, "index.html"), "w") as f:
    f.write(page)
with open(os.path.join(ROOT, "assets", "i18n.js"), "w") as f:
    f.write("/* 生成物（tools/gen.py）。手で直さない。文言は tools/content.py。 */\n")
    f.write("window.DOPAMINE_I18N = " + json.dumps({"en": en, "ja": ja}, ensure_ascii=False, indent=1) + ";\n")
print(f"index.html + assets/i18n.js ({len(en)} keys, {total} features)")

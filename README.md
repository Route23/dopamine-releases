<div align="center">
  <img src="assets/dopamine.png" width="128" alt="dopamine">
  <h1>dopamine</h1>
  <p>A browser, a terminal, an editor and your files — side by side in one window.<br>
     For macOS (Apple Silicon) and Windows (x64 &amp; ARM64).</p>
  <p><b><a href="https://route23.github.io/dopamine-releases/">route23.github.io/dopamine-releases</a></b></p>
</div>

---

**This repository holds the downloads and the website, not the source.**
Builds are published here as Releases; the site under `/` is served by GitHub Pages.

### Editing the website

Every file is hand-written and English only: `index.html`, `releases.html`, `404.html`,
`assets/styles.css`, `assets/site.js` (screenshot lightbox) and `assets/app.js` (release data from
the GitHub API, and which download fits the visitor's OS). The three screenshots live in
`assets/shots/` as WebP. The look follows the app's launch screen: Instrument Serif and its four
colours — black `#000000`, blue `#3E43FF`, rust `#AF3816` — with text in `#DCD6BD`.

## Install

### macOS (Apple Silicon, macOS 14+)

```sh
brew install --cask Route23/tap/dopamine
```

Or grab the `.dmg` from [the latest release](https://github.com/Route23/dopamine-releases/releases/latest).

### First launch from the `.dmg`

dopamine is signed ad-hoc and **not notarized by Apple**, so macOS refuses to open
it the first time. Run this once, then open the app:

```sh
xattr -dr com.apple.quarantine /Applications/dopamine.app
```

Installing with Homebrew does this for you.

### Windows (10 or 11, x64 or ARM64)

Download `dopamine_<version>_x64-setup.exe` (most PCs) or `dopamine_<version>_arm64-setup.exe`
(Windows on ARM) from [the latest release](https://github.com/Route23/dopamine-releases/releases/latest)
and run it. It installs for your user only and needs no administrator rights.

The installer is not code-signed yet, so SmartScreen may say "Windows protected your PC" —
choose **More info**, then **Run anyway**.

## Requirements

- macOS 14 (Sonoma) or later on Apple Silicon — there is no Intel Mac build
- Windows 10 or 11 on x64 or ARM64 (Microsoft Edge WebView2, which Windows already includes)

## Bugs and requests

→ [Route23/dopamine-issues](https://github.com/Route23/dopamine-issues/issues)

## Working on the site

The site is plain HTML, CSS, and two small scripts — **no build step, no dependencies**.
The only outside request besides the GitHub API is the Instrument Serif font from Google Fonts. Edit the files and push; GitHub Pages serves `main` at the repo root.

Preview it the way it is actually served (from the *parent* directory, so the
`/dopamine-releases/` subpath is reproduced — a root-absolute `/assets/…` path
breaks in production but works if you serve from inside the repo):

```sh
cd .. && python3 -m http.server 8000
open http://localhost:8000/dopamine-releases/
```

Release data is fetched from the GitHub API at page load, so **a new release
shows up without touching this repo**.

> **Branching**: the source repo (`Route23/dopamine`) requires every branch to
> come off `main` and enforces it with a workflow. That workflow is deliberately
> **not** copied here — it targets a self-hosted runner registered to the other
> repository, so it would sit `pending` forever. The convention still applies by
> hand: branch from `main`, base every PR on `main`.

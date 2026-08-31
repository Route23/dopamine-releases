<div align="center">
  <img src="assets/dopamine.png" width="128" alt="dopamine">
  <h1>dopamine</h1>
  <p>A macOS desktop browser built on gpui — split a space into web pages,<br>
     a terminal, a file browser, and RSS.</p>
  <p><b><a href="https://route23.github.io/dopamine-releases/">route23.github.io/dopamine-releases</a></b></p>
</div>

---

**This repository holds the downloads and the website, not the source.**
Builds are published here as Releases; the site under `/` is served by GitHub Pages.

## Install

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

## Requirements

- macOS 14 (Sonoma) or later
- Apple Silicon (arm64) only — there is no Intel build

## Bugs and requests

→ [Route23/dopamine-issues](https://github.com/Route23/dopamine-issues/issues)

## Working on the site

The site is plain HTML, CSS, and one script — **no build step, no dependencies,
no CDN**. Edit the files and push; GitHub Pages serves `main` at the repo root.

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

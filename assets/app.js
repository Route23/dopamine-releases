/* dopamine — distribution site
 *
 * 設計の要点 3 つ:
 *
 * 1. **HTML だけで完結している。** ダウンロードリンクは authored HTML に
 *    `.../releases/latest` として最初から書いてあり、このスクリプトは
 *    **上書きするだけ**。JS 無効でも、API がレート制限でも、オフラインでも
 *    ダウンロードできる。**空のボタンを JS で組み立てない。**
 * 2. **`innerHTML` への代入はこのファイルで 1 箇所だけ。** リリースノートに
 *    `scrub(body_html)` を入れる行。検査点は
 *    `grep -cE 'innerHTML[[:space:]]*=' assets/app.js` が **1** を返すこと
 *    （`doc.body.innerHTML` の読み出しは scrub の出口なので別勘定）。
 *    ほかの値は全部 textContent と el.href で入れる。
 * 3. **劣化した経路が最も安全な経路。** `body_html` が取れなければ
 *    マークダウンを解釈せず `textContent` で出す（構造上インジェクション不能）。
 *
 * 外部依存ゼロ。origin の外へ出るリクエストは GitHub REST への 1 本だけ。
 */
(function () {
  "use strict";

  var REPO = "Route23/dopamine-releases";
  var API = "https://api.github.com/repos/" + REPO + "/releases?per_page=100";
  var RELEASES_URL = "https://github.com/" + REPO + "/releases";
  var CACHE_KEY = "dopamine.releases.v1";
  var TTL_MS = 10 * 60 * 1000;
  // 資産の特定は **後方一致**。真ん中のバージョンに依存しない。
  var DMG_SUFFIX = "_aarch64.dmg";

  // ── utils ────────────────────────────────────────────────────────────

  /** 文言（#513）。辞書は assets/i18n.js、引くのは assets/site.js。無ければ英語の `fb`。 */
  function T(key, fb, vars) {
    if (typeof window.dopamineT === "function") return window.dopamineT(key, vars);
    var s = fb;
    if (vars) for (var k in vars) s = s.split("{" + k + "}").join(vars[k]);
    return s;
  }

  function fmtDate(iso) {
    if (!iso) return "";
    try {
      return new Intl.DateTimeFormat(window.dopamineLang === "ja" ? "ja" : "en", {
        year: "numeric", month: "short", day: "numeric",
      }).format(new Date(iso));
    } catch (e) { return ""; }
  }

  function fmtSize(bytes) {
    if (!bytes) return "";
    var mb = bytes / (1024 * 1024);
    return (mb >= 100 ? mb.toFixed(0) : mb.toFixed(1)) + " MB";
  }

  function dmgAsset(release) {
    var assets = (release && release.assets) || [];
    for (var i = 0; i < assets.length; i++) {
      if (typeof assets[i].name === "string" && assets[i].name.slice(-DMG_SUFFIX.length) === DMG_SUFFIX) {
        return assets[i];
      }
    }
    return null;
  }

  /** github.com / その CDN 以外の URL は張らない。 */
  function safeUrl(u) {
    if (typeof u !== "string") return null;
    if (u.indexOf("https://github.com/") === 0) return u;
    if (u.indexOf("https://objects.githubusercontent.com/") === 0) return u;
    return null;
  }

  /**
   * GitHub が返した `body_html` を、こちら側でももう一度ふるいにかける。
   *
   * `DOMParser` は**不活性な**文書を作る —— パース中にスクリプトは走らず、
   * 画像も読み込まれない。属性の削除は live な NamedNodeMap ではなく
   * 名前のスナップショットを回す。
   */
  function scrub(html) {
    var doc = new DOMParser().parseFromString(html, "text/html");
    var drop = { SCRIPT: 1, STYLE: 1, IFRAME: 1, OBJECT: 1, EMBED: 1, FORM: 1,
                 INPUT: 1, BUTTON: 1, LINK: 1, META: 1, BASE: 1 };
    var all = doc.body.querySelectorAll("*");
    for (var i = 0; i < all.length; i++) {
      var el = all[i];
      if (drop[el.tagName]) { el.remove(); continue; }
      var names = [];
      for (var j = 0; j < el.attributes.length; j++) names.push(el.attributes[j].name);
      for (var k = 0; k < names.length; k++) {
        var n = names[k];
        var v = (el.getAttribute(n) || "").trim().toLowerCase();
        if (n.slice(0, 2) === "on") { el.removeAttribute(n); continue; }
        if ((n === "href" || n === "src" || n === "xlink:href") &&
            (v.indexOf("javascript:") === 0 || v.indexOf("data:") === 0 || v.indexOf("vbscript:") === 0)) {
          el.removeAttribute(n);
        }
      }
    }
    var links = doc.body.querySelectorAll("a[href]");
    for (var m = 0; m < links.length; m++) {
      links[m].setAttribute("target", "_blank");
      links[m].setAttribute("rel", "noopener noreferrer");
    }
    return doc.body.innerHTML;
  }

  /**
   * release.yml の notes.md は先頭に `dopamine vX.Y.Z` の 1 行を持つ。
   * ページ側でも <h2> に同じものを出すので、重複を落とす。
   */
  function stripDupTitle(node, tag) {
    var first = node.firstElementChild;
    if (first && first.tagName === "P" &&
        /^dopamine\s+v?\d+\.\d+\.\d+\s*$/i.test(first.textContent.trim())) {
      first.remove();
    }
    return node;
  }

  // ── cache ────────────────────────────────────────────────────────────
  // localStorage は private window や site data を切っている環境で **throw する**。
  // 読み書きとも try/catch で包み、無いときは普通に描く。

  function readCache() {
    try {
      var raw = localStorage.getItem(CACHE_KEY);
      if (!raw) return null;
      var v = JSON.parse(raw);
      if (!v || !Array.isArray(v.data)) return null;
      return v;
    } catch (e) { return null; }
  }

  function writeCache(data) {
    try {
      localStorage.setItem(CACHE_KEY, JSON.stringify({ at: Date.now(), data: data }));
    } catch (e) { /* 保存できなくても表示には困らない */ }
  }

  // ── net ──────────────────────────────────────────────────────────────

  function loadReleases() {
    var cached = readCache();
    if (cached && Date.now() - cached.at < TTL_MS) {
      return Promise.resolve(cached.data);
    }
    return fetch(API, {
      headers: {
        // `full` は body / body_text / body_html を全部返す。
        Accept: "application/vnd.github.full+json",
        "X-GitHub-Api-Version": "2022-11-28",
      },
    }).then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    }).then(function (data) {
      if (!Array.isArray(data)) throw new Error("unexpected payload");
      var live = data.filter(function (r) { return !r.draft; });
      writeCache(live);
      return live;
    }).catch(function (err) {
      // **失敗したら TTL を無視してキャッシュを出す。** 古い情報でも
      // 「何も出ない」より役に立つ。
      if (cached) return cached.data;
      throw err;
    });
  }

  // ── index.html ───────────────────────────────────────────────────────

  function enhanceDownload(releases) {
    var btn = document.getElementById("download-primary");
    var meta = document.getElementById("download-meta");
    if (!btn) return;

    if (!releases.length) {
      // **今日の状態。** エラーではなく、別の状態として扱う。
      btn.textContent = T("dl.none", "No public build yet");
      if (meta) meta.textContent = T("dl.first", "The first release will be v0.1.0.");
      return;
    }
    var latest = releases[0];
    var asset = dmgAsset(latest);
    var url = asset && safeUrl(asset.browser_download_url);
    if (!url) {
      if (meta) meta.textContent = T("dl.latestOnly", "Latest release: {tag}", { tag: latest.tag_name });
      return;
    }
    btn.href = url;
    btn.textContent = T("dl.latest", "Download dopamine {tag}", { tag: latest.tag_name });
    if (meta) {
      meta.textContent = [asset.name, fmtSize(asset.size), fmtDate(latest.published_at)]
        .filter(Boolean).join(" · ");
    }
  }

  // ── releases.html ────────────────────────────────────────────────────

  function renderReleaseList(releases) {
    var list = document.getElementById("releases-list");
    var fallback = document.getElementById("releases-fallback");
    if (!list) return;

    if (!releases.length) {
      if (fallback) {
        fallback.textContent = T("rel.none", "No releases yet. The first public build will be v0.1.0.");
        fallback.hidden = false;
      }
      return;
    }
    if (fallback) fallback.hidden = true;
    list.textContent = "";

    releases.forEach(function (r) {
      var li = document.createElement("li");
      var art = document.createElement("article");
      art.className = "card";

      var head = document.createElement("div");
      head.className = "release__head";
      var h2 = document.createElement("h2");
      h2.textContent = r.tag_name || r.name || "";
      head.appendChild(h2);
      if (r.prerelease) {
        var chip = document.createElement("span");
        chip.className = "chip";
        chip.textContent = T("rel.pre", "pre-release");
        head.appendChild(chip);
      }
      if (r.published_at) {
        var time = document.createElement("time");
        time.setAttribute("datetime", r.published_at);
        time.className = "muted small";
        time.textContent = fmtDate(r.published_at);
        head.appendChild(time);
      }
      art.appendChild(head);

      var notes = document.createElement("div");
      notes.className = "release__notes";
      if (typeof r.body_html === "string" && r.body_html) {
        notes.innerHTML = scrub(r.body_html); // ← このファイル唯一の innerHTML
        stripDupTitle(notes);
      } else if (typeof r.body === "string" && r.body) {
        // **マークダウンを解釈しない。** textContent は構造上注入できない。
        var pre = document.createElement("pre");
        pre.className = "notes-raw";
        pre.textContent = r.body.replace(/^dopamine\s+v?\d+\.\d+\.\d+\s*\n+/i, "");
        notes.appendChild(pre);
      }
      art.appendChild(notes);

      var asset = dmgAsset(r);
      var url = asset && safeUrl(asset.browser_download_url);
      if (url) {
        var a = document.createElement("a");
        a.className = "release__dl";
        a.href = url;
        a.textContent = "↓ " + asset.name + " (" + fmtSize(asset.size) + ")";
        art.appendChild(a);
      }
      li.appendChild(art);
      list.appendChild(li);
    });
  }

  // ── degrade ──────────────────────────────────────────────────────────
  // **authored HTML には指一本触れない。** 注記を出すだけ。

  function degrade() {
    var notes = document.querySelectorAll("[data-degraded-note]");
    for (var i = 0; i < notes.length; i++) notes[i].hidden = false;
    var fallback = document.getElementById("releases-fallback");
    if (fallback) fallback.hidden = false;
  }

  // ── copy buttons ─────────────────────────────────────────────────────

  function wireCopyButtons() {
    var btns = document.querySelectorAll(".cmd__copy");
    for (var i = 0; i < btns.length; i++) {
      (function (btn) {
        // file:// では clipboard API が無い。死んだボタンを見せるより隠す
        // （コマンド自体は選択してコピーできる）。
        if (!navigator.clipboard) { btn.hidden = true; return; }
        btn.addEventListener("click", function () {
          var pre = btn.parentNode.querySelector("pre");
          if (!pre) return;
          navigator.clipboard.writeText(pre.textContent.trim()).then(function () {
            var old = btn.textContent;
            btn.textContent = T("copied", "Copied");
            setTimeout(function () { btn.textContent = old; }, 1500);
          });
        });
      })(btns[i]);
    }
  }

  // ── boot ─────────────────────────────────────────────────────────────

  document.addEventListener("DOMContentLoaded", function () {
    wireCopyButtons();
    loadReleases().then(function (releases) {
      enhanceDownload(releases);
      renderReleaseList(releases);
    }).catch(function (err) {
      if (window.console) console.warn("[dopamine] release info unavailable:", err);
      degrade();
    });
  });
})();

/* dopamine — distribution site: 言語の切り替えと、スクショの拡大（#513）。
 *
 * - **HTML は英語で完結している。** ここは ja のときに `data-i18n` の字を
 *   `textContent` で差し替えるだけ（innerHTML は使わない —— app.js の約束と同じ）。
 * - 言語はブラウザの言語で決め、EN / JA を押したら localStorage に覚えて読み直す
 *   （app.js が書いた文言も含めて、読み直すのがいちばん確か）。
 * - 辞書は assets/i18n.js（tools/gen.py の生成物）。
 */
(function () {
  "use strict";

  var DICT = window.DOPAMINE_I18N || { en: {}, ja: {} };
  var KEY = "dopamine.lang";

  function stored() {
    try {
      var v = localStorage.getItem(KEY);
      return v === "en" || v === "ja" ? v : null;
    } catch (e) { return null; }
  }

  function detect() {
    var n = (navigator.languages && navigator.languages[0]) || navigator.language || "en";
    return /^ja\b/i.test(n) ? "ja" : "en";
  }

  /** `?lang=en` / `?lang=ja` はその場だけ効く（覚えない）。言語を決めたリンクを配るため。 */
  function fromUrl() {
    var m = /[?&]lang=(en|ja)\b/.exec(location.search);
    return m ? m[1] : null;
  }

  var lang = fromUrl() || stored() || detect();
  window.dopamineLang = lang;

  /** 鍵から文言。`{name}` を `vars` で埋める。無い鍵は英語、それも無ければ鍵そのもの。 */
  window.dopamineT = function (key, vars) {
    var s = (DICT[lang] && DICT[lang][key]) || (DICT.en && DICT.en[key]) || key;
    if (vars) {
      for (var k in vars) {
        if (Object.prototype.hasOwnProperty.call(vars, k)) s = s.split("{" + k + "}").join(vars[k]);
      }
    }
    return s;
  };

  function apply() {
    document.documentElement.lang = lang;
    if (lang !== "en") {
      var nodes = document.querySelectorAll("[data-i18n]");
      for (var i = 0; i < nodes.length; i++) {
        var t = DICT[lang] && DICT[lang][nodes[i].getAttribute("data-i18n")];
        if (t) nodes[i].textContent = t;
      }
      var alts = document.querySelectorAll("[data-i18n-alt]");
      for (var j = 0; j < alts.length; j++) {
        var a = DICT[lang] && DICT[lang][alts[j].getAttribute("data-i18n-alt")];
        if (a) alts[j].setAttribute("alt", a);
      }
      var title = DICT[lang] && DICT[lang][document.body.getAttribute("data-title") || "doc.title"];
      if (title) document.title = title;
    }
    var btns = document.querySelectorAll("[data-lang]");
    for (var b = 0; b < btns.length; b++) {
      var mine = btns[b].getAttribute("data-lang");
      btns[b].setAttribute("aria-pressed", mine === lang ? "true" : "false");
      btns[b].addEventListener("click", function (ev) {
        var to = ev.currentTarget.getAttribute("data-lang");
        if (to === lang) return;
        try { localStorage.setItem(KEY, to); } catch (e) { /* 覚えられなくても切り替えはする */ }
        location.reload();
      });
    }
  }

  function lightbox() {
    var dlg = document.querySelector(".lightbox");
    if (!dlg || typeof dlg.showModal !== "function") return;
    var img = dlg.querySelector("img");
    var zooms = document.querySelectorAll(".shot__zoom");
    for (var i = 0; i < zooms.length; i++) {
      zooms[i].addEventListener("click", function (ev) {
        var btn = ev.currentTarget;
        var inner = btn.querySelector("img");
        img.src = btn.getAttribute("data-full");
        img.alt = inner ? inner.alt : "";
        dlg.showModal();
      });
    }
    dlg.addEventListener("click", function () { dlg.close(); });
  }

  apply();
  lightbox();
})();

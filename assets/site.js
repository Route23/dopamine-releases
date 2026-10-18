/* Dopamine — distribution site: スクリーンショットの拡大だけ（#1110 で日本語と言語の切り替えを外した）。 */
(function () {
  "use strict";

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

  lightbox();
})();

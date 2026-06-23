/* Steuerberatung Muyres - Demonstrator: Nav, Parallax, Menue, Cookie, Demo, Reveal */
(function () {
  "use strict";

  var nav = document.getElementById("nav");
  var heroBg = document.getElementById("heroBg");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isMobile = window.matchMedia("(max-width: 760px)");

  /* ---- Scroll: Nav-Solid + Parallax 50% (rAF-gedrosselt) ---- */
  var ticking = false;
  function onFrame() {
    var y = window.scrollY;
    if (nav) nav.classList.toggle("scrolled", y > 20);
    if (heroBg && !reduce && y < 1100) {
      heroBg.style.transform = "translateY(" + (y * 0.5) + "px)";
    }
    ticking = false;
  }
  function onScroll() {
    if (!ticking) { window.requestAnimationFrame(onFrame); ticking = true; }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onFrame();

  /* ---- Mobile-Menue (Burger toggelt + morpht, Backdrop + Swipe-up schliessen) ---- */
  var burger = document.getElementById("burger");
  var mmenu = document.getElementById("mmenu");
  var backdrop = document.getElementById("mbackdrop");
  function setMenu(open) {
    if (!mmenu) return;
    mmenu.classList.toggle("open", open);
    if (nav) nav.classList.toggle("menu-open", open);
    if (open) mmenu.removeAttribute("inert"); else mmenu.setAttribute("inert", "");
    if (burger) { burger.classList.toggle("open", open); burger.setAttribute("aria-expanded", open ? "true" : "false"); }
    if (backdrop) backdrop.hidden = !open;
    document.body.style.overflow = open ? "hidden" : "";
  }
  function closeMenu() { setMenu(false); }
  if (burger) burger.addEventListener("click", function () { setMenu(!mmenu.classList.contains("open")); });
  if (backdrop) backdrop.addEventListener("click", closeMenu);
  if (mmenu) mmenu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });
  /* Swipe nach oben schliesst */
  if (mmenu) {
    var swY = 0, swActive = false;
    mmenu.addEventListener("touchstart", function (e) { swY = e.touches[0].clientY; swActive = true; }, { passive: true });
    mmenu.addEventListener("touchmove", function (e) { if (swActive && swY - e.touches[0].clientY > 50) { closeMenu(); swActive = false; } }, { passive: true });
    mmenu.addEventListener("touchend", function () { swActive = false; });
  }

  /* ---- Cookie-Banner + Demo-Hinweis (sequenziell) ---- */
  var cookie = document.getElementById("cookie");
  var cookieAccept = document.getElementById("cookieAccept");
  var cookieDecline = document.getElementById("cookieDecline");
  var cookieReopen = document.getElementById("cookieReopen");
  var demobar = document.getElementById("demobar");
  var democlose = document.getElementById("democlose");

  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function sread(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } }
  function sstore(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }

  function showDemo() {
    if (demobar && sread("muyres_demo_hidden") !== "1") demobar.classList.remove("hidden");
  }
  function showCookie() { if (cookie) cookie.classList.remove("hidden"); }
  function hideCookie() { if (cookie) cookie.classList.add("hidden"); }
  function decideCookie(val) { store("muyres_cookie", val); hideCookie(); setTimeout(showDemo, 280); }

  if (read("muyres_cookie")) {
    showDemo();
  } else {
    setTimeout(showCookie, 700);
  }
  if (cookieAccept) cookieAccept.addEventListener("click", function () { decideCookie("all"); });
  if (cookieDecline) cookieDecline.addEventListener("click", function () { decideCookie("essential"); });
  if (cookieReopen) cookieReopen.addEventListener("click", function (e) { e.preventDefault(); showCookie(); });
  if (democlose && demobar) democlose.addEventListener("click", function () {
    demobar.classList.add("hidden"); sstore("muyres_demo_hidden", "1");
  });

  /* ---- Kontakt-Ribbon: immer schiebbar, Auto-Lauf NUR mobil ---- */
  var track = document.getElementById("cstripTrack");
  var marqMq = window.matchMedia("(max-width: 760px)");
  if (track) {
    var group = track.querySelector(".cstrip__group");
    if (group) {
      var clone = group.cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      track.appendChild(clone);
      var groupW = group.getBoundingClientRect().width || 1;
      var offset = 0, dragging = false, moved = false, startX = 0, startOff = 0;
      function norm() { offset = ((offset % groupW) + groupW) % groupW; }
      function apply() { track.style.transform = "translateX(" + (-offset) + "px)"; }
      function px(e) { return e.touches ? e.touches[0].clientX : e.clientX; }
      function frame() {
        if (!dragging) {
          var sp = (marqMq.matches && !reduce) ? 0.4 : 0; /* nur mobil animieren */
          if (sp) { offset += sp; norm(); apply(); }
        }
        window.requestAnimationFrame(frame);
      }
      track.addEventListener("pointerdown", function (e) { dragging = true; moved = false; startX = px(e); startOff = offset; });
      window.addEventListener("pointermove", function (e) { if (!dragging) return; moved = true; offset = startOff - (px(e) - startX); norm(); apply(); });
      window.addEventListener("pointerup", function () { dragging = false; });
      /* versehentliches Klicken auf Links nach Drag verhindern */
      track.addEventListener("click", function (e) { if (moved) { e.preventDefault(); } }, true);
      window.addEventListener("resize", function () { groupW = group.getBoundingClientRect().width || groupW; });
      window.requestAnimationFrame(frame);
    }
  }

  /* ---- Reveal / Stagger ---- */
  var targets = document.querySelectorAll(".reveal, .stagger");
  if (reduce || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
  targets.forEach(function (el) { io.observe(el); });
})();

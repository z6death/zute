// ==UserScript==
// @name YouTube to Invidious Redirect
// @match *://www.youtube.com/*
// @match *://youtube.com/*
// @run-at document_start
// ==/UserScript==

window.location.href = window.location.href
  .replace('www.youtube.com', 'yewtu.be')
  .replace('youtube.com', 'yewtu.be');

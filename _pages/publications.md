---
layout: page
permalink: /publications/
title: Publications
description: 
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<div class="publications-header">
  <div class="description-text">Papers by categories in reversed chronological order.</div>
  <div class="search-container">
    {% include bib_search.liquid %}
  </div>
</div>

<div class="publications">
  <!-- Published Papers Section -->
  <h2 class="category-heading">Published Papers</h2>
  {% bibliography --query @article,@book,@booklet,@conference,@inbook,@incollection,@manual,@mastersthesis,@phdthesis,@proceedings,@inproceedings %}

  <!-- Working Papers Section -->
  <h2 class="category-heading">Working Papers</h2>
  {% bibliography --query @unpublished,@techreport,@misc %}
</div>
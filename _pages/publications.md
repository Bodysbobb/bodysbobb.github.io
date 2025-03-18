---
layout: page
permalink: /publications/
title: Publications
description: Publications by categories in reversed chronological order.
nav: true
nav_order: 2
display_categories: [published, working]
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->
{% include bib_search.liquid %}

<div class="publications">
{% if page.display_categories %}
  <!-- Display categorized publications -->
  {% for category in page.display_categories %}
    <h2 class="category-heading">{% if category == "published" %}Published Papers{% elsif category == "working" %}Working Papers{% else %}{{ category | capitalize }}{% endif %}</h2>
    
    {% bibliography -q @*[type={{category}}]* %}
  {% endfor %}
{% else %}
  <!-- Display all publications without categories -->
  {% bibliography %}
{% endif %}
</div>
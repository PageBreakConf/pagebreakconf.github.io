---
layout: page
title: PageBreak 2022 Speakers
permalink: /speakers2022/
---

<h1>Meet Our 2022 Speakers</h1>

<ul class="speakers">
{% assign sortedPeople = site.data.2022people | sort: "Sortindex" %}
{% for speaker in  sortedPeople %}
  {% include speaker_item.html %}
{% endfor %}
</ul>
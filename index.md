---
title: Edward FitzGerald's translation of the Rubayat of Omar Khayam
layout: default
---

<h1>Edward FitzGerald's <i>Rubayat of Omar Khayam</i></h1>

{% for stanza in site.stanzas %}
  <p>{{ stanza.edition }} <a href = "{{ stanza.url }}">{{ stanza.stanza }}</a></p>
{% endfor %}

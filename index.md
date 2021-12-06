---
title: Edward FitzGerald's translation of the Rubayat of Omar Khayam
layout: index_layout
---

<h1>Edward FitzGerald's <i>Rubaiyat of Omar Khayyam</i></h1>
<p>All versions of the stanzas from the first five editions</p>
{% assign editions = '1859,1868,1872,1879,1889' | split: ',' %}
<table>
<tr>
{% for edition in editions %}
  <th>
  {{ edition }}
  </th>
{% endfor %}
</tr>
<tr>
{% for edition in editions %}
  <td>
  {% assign stanzas = site.stanzas | where: 'edition', edition | sort: 'stanza' %}
  {% for stanza in stanzas %}
    <a href = "{{ stanza.url }}">{{ stanza.stanza }}</a><br>
  {% endfor %}
  </td>
{% endfor %}
</tr>
</table>


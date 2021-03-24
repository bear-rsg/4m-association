---
layout: "year_bulletin"
---
{% for bulletin in site.short_bulletins %}

    <h2><a href="{{ bulletin.url }}">{{ bulletin.title }}</a></h2>
    {{ bulletin.content | markdownify }}
    
    <hr />
    
{% endfor %}






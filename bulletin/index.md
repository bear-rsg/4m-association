---
layout: sidebar_page
---

<script>
  (async () => {
    const response = await fetch('https://api.github.com/repositories/304575824/contents/bulletin/');
    const data = await response.json();
    let htmlString = '<ul class="bulletin-list">';
    for (let file of data) {
      let filepath = ${file.path}.slice(0, -3) + '.html'
      let filename = ${file.name}
      htmlString += `<li><a href="/4m-association/${filepath}">${filename}</a></li>`;
    }
    htmlString += '</ul>';
    document.getElementsByClassName('bulletin-list')[0].innerHTML = htmlString;
  })()
</script>
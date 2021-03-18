---
layout: sidebar_page
---

<script>
  (async () => {
    const indexResponse = await fetch('https://api.github.com/repositories/304575824/contents/bulletin/?ref=dev-v1');
    const indexData = await indexResponse.json();
    let indexHtmlString = '<ul>';
    for (let indexFile of indexData) {
      let indexFilepath = indexFile.path.slice(0, -3) + '.html'
      indexHtmlString += `<li><a href="/4m-association/${indexFilepath}">${indexFile.name}</a></li>`;
    }
    indexHtmlString += '</ul>';
    document.getElementsByClassName('left-area')[0].innerHTML = indexHtmlString;
  })()
</script>
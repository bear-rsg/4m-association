---
layout: sidebar_page
---

<script>
  (async () => {
    const indexResponse = await fetch('https://api.github.com/repos/bear-rsg/4m-association/contents/bulletin?ref=dev-v1');
    const indexData = await indexResponse.json();
    let indexHtmlString = '<ul>';
    for (let indexFile of indexData) {
      let indexFileName = indexFile.name;
      if (indexFile.name.endsWith('.md')) {
        indexFileName = indexFile.name.slice(0, -3);
      }
      indexFileName = indexFileName.replace(/([a-z0-9])([A-Z])/g, '$1 $2');
      let indexCapFileName = indexFileName.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
      let indexFilepath = indexFile.path.slice(0, -3) + '.html';
      indexHtmlString += `<li><a href="/4m-association/${indexFilepath}">${indexCapFileName}</a></li>`;
    }
    indexHtmlString += '</ul>';
    document.getElementsByClassName('left-area')[0].innerHTML = indexHtmlString;
  })()
</script>
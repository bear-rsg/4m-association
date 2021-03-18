---
layout: sidebar_page
---

<script>
  (async () => {
    const indexResponse = await fetch('https://api.github.com/repos/bear-rsg/4m-association/contents/bulletin?ref=dev-v1');
    const indexData = await indexResponse.json();
    let indexHtmlString = '<ul>';
    for (let indexFile of indexData) {
      if (indexFile.name.endsWith('.md')) {
        let indexFileName = indexFile.name.slice(0, -3);
      } else {
        let indexFileName = indexFile.name;
      }
      let indexCapFileName = indexFileName.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
      let indexFilepath = indexFile.path.slice(0, -3) + '.html';
      let indexHtmlString += `<li><a href="/4m-association/${indexFilepath}">${indexCapFileName}</a></li>`;
    }
    indexHtmlString += '</ul>';
    document.getElementsByClassName('left-area')[0].innerHTML = indexHtmlString;
  })()
</script>
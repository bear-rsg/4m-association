---
layout: sidebar_page
---

<script>
  (async () => {
    const indexResponse = await fetch('https://api..com/repos/bear-rsg/4m-association/contents/bulletin?ref=dev-v1');
    const indexData = await indexResponse.json();
    let indexHtmlString = '<ul>';
    for (let indexFile of indexData) {
        let indexFileName = indexFile.name;
        let indexFilepath = indexFile.path.slice(0, -3) + '.html';
        if (indexFileName.endsWith('.md')) {
            indexFileName = indexFileName.slice(0, -3);
            indexFilepath = indexFile.path.slice(0, -3) + '.html';
        }
        indexFileName = indexFile.name.replace(/([a-z0-9])([A-Z])/g, '$1 $2');
        indexFileName = indexFileName.replace(/([a-z])([0-9])/g, '$1 $2');
        indexFileName= indexFileName.replace(/([a-z0-9])([-])([a-z0-9])/g, '$1 $3');
            
        let indexCapFileName = indexFileName.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
        
        indexHtmlString += `<li><a href="/4m-association/${indexFilepath}">${indexCapFileName}</a></li>`;
    }
    indexHtmlString += '</ul>';
    document.getElementsByClassName('left-area')[0].innerHTML = indexHtmlString;
  })()
</script>
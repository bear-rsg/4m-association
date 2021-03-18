---
layout: sidebar_page
---

<script>
  (async () => {
    const indexResponse = await fetch('https://api.github.com/repos/bear-rsg/4m-association/contents/bulletin?ref=dev-v1');
    const indexData = await indexResponse.json();
    document.getElementsByClassName('left-area')[0].innerHTML = indexData;
  })()
</script>
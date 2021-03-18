---
layout: sidebar_page
---

<script>
  (async () => {
    const indexResponse = await fetch('https://api.github.com/repositories/304575824/contents/bulletin/?ref=dev-v1');
    const indexData = await indexResponse.json()[0];
    document.getElementsByClassName('left-area')[0].innerHTML = indexData;
  })()
</script>
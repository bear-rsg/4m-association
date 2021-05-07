title: 4M Association
date: 2021-03-31
slug: news
<!-- loop through bulletin / conference etc by month (using teasers) -->

SELECT nr.nid, nr.vid, nr.title, nr.teaser, nr.timestamp, n.*
FROM node_revisions AS nr 
JOIN node n ON nr.vid = n.vid 
WHERE n.promote = 1
ORDER BY n.changed DESC

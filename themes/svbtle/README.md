# SVBTLE

Svbtle theme is a close copy of [Svbtle.com](http://www.svbtle.com) with
a few minor changes for use with [Pelican](http://pelican.notmyidea.org).

You can see the [theme in
action](http://williamting.com/drafts/this-is-a-theme-testing-post.html), or
the site code [here](https://github.com/wting/williamting.com).

![theme screenshot](https://raw.github.com/wting/pelican-svbtle/master/screenshot.png)

- syntax highlighting for code blocks
- Google Analytics
- Disqus commenting
- custom list of links
- support for this LaTeX [plugin][latex]

- no IE testing
- no custom menu
- header date format is hardcoded in `./templates/header.html` with the
  exception of articles.
- Svbtle uses Freight-Sans-Pro for article titles and Proxima Nova for body.
  While they are great fonts, neither are free. I've linked to them in case
  the client has them installed, but most users will browse the site with Open
  Sans.

### FROM SOURCE

Download the [repository](https://github.com/wting/pelican-svbtle) and save
it somewhere accessible. Edit `settings.py` and modify the `THEME` variable
to point to the downloaded theme location.

### FROM OFFICIAL REPO

Please refer to Pelican theme [install
instructions](http://pelican.notmyidea.org/en/latest/pelican-themes.html).

These are the Pelican global variables currently supported by the theme:

- `GOOGLE_ANALYTICS`
- `GAUGES_ANALYTICS`
- `DISQUS_SITENAME`
- `LINKS(('name1', 'url1'), ('name2', 'url2'))`
- `DEFAULT_DATE_FORMAT = ('%b %d, %Y')`: suggested date format
- `FEED_DOMAIN = SITEURL`
- `AUTHOR_BIO`, providing a short bio that appears on the side bar.

When developing locally, set the following variable:

`SITEURL = http://localhost:8000`

If you want to enable LaTeX support, additional settings must be
[configured][latex].

- Accent color can be changed by editing `@accent` in `./static/css/style.less`.

- A different Pygmentize theme can be used by editing `./Makefile` and
  running `make pygments`.

William Ting

Released under MIT License, full details in `LICENSE` file.

[latex]: https://github.com/barrysteyn/pelican_plugin-latex

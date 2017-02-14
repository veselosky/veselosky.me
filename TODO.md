
Category metadata determines output directory. If explicitly supplied in
metadata, overrides the input path.

How do you want to structure the blog going forward?

Tasks
====================
* Fix broken links (missing ".html")
* Combine and minify CSS, JS
* fontawesome for follow me section

Issues
=============================================================================
Often templates need to generate self-referencing URLs. These will differ
between test and production systems, yet we need static files to be the same
in both cases.

Option:
Store canonical base in site.yml. Have local test server translate canonical
base to local base in text when serving.

Downside: requires writing a dev server.
Solution: Depend on static3 webserver library, add a "magic" for the URL
translation.

Bug Fixes
====================
* Find and Fix broken internal links (missing ".html", directory moves)
* Fix image styles (/life/martin-luther-king-jr-day image encroaches on sidebar)
* Automate redirects from old date-based URLs to new category-based ones.

Features
====================
* Category page (or pages)
* fontawesome for follow me section?

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

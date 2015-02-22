:Title: Django Settings: Three Things Conflated
:Date: 2012-02-18
:Author: Vince Veselosky
:Slug: django-settings-three-things-conflated
:Category: Technology

.. post:: 2012-02-18
    :category: Technology

Django Settings: Three Things Conflated
========================================

If you work on a large Django project, there's a good chance that you
would describe your settings file as "a mess" (or perhaps you use
harsher language). You may even have broken your settings out into a
whole package with multiple files to try and keep things organized.
We're highly skilled and organized developers, how does this happen to
us?

I believe part of the problem is that the "settings" bucket holds three
different kinds of things without differentiating between them. If you
make a clear distinction between these things in your own mind (and in
your code), dealing with settings will become easier, if not *easy*.

Project composition
-------------------

The first class of settings comprises those used for *project
composition*. One of the killer features of Django is that projects are
*composed* of independent modules (apps). The most important settings in
your project's settings file define what apps make up the project and
how they interact with each other. In other frameworks this would be
done with code (well, technically settings *are* Python code), but in
Django this is treated as configuration. Things like INSTALLED\_APPS,
MIDDLEWARE\_CLASSES, and TEMPLATE\_CONTEXT\_PROCESSORS define how the
components of your project are combined to achieve the desired
functionality.

Settings whose values are (possibly a list of) Python modules normally
fall into this category.

External resources
------------------

The second class of settings comprises those used for connecting to
external resources. This is the area most broadly recognized as
*configuration*. Settings like DATABASES and CACHES fall into this
category. These are the things that `The Twelve Factor
App <http://vince.veselosky.me/2012/02/heroku-and-twelve-factor-app.html>`__
says should be provided by environment variables, and in fact it's not
that difficult to pull these values into your settings from the
environment.

In addition to the obvious dictionaries defining pluggable back-ends,
any setting whose value is a file system path or a URL likely falls into
this category.

Tunable parameters
------------------

The final class of settings comprises *tunable parameters*, things that
are mostly constants or variables that are abstracted out because 1)
hard-coded values are bad, and 2) you (or users of the code) might want
to change the values from the defaults. Things like
CACHE\_MIDDLEWARE\_SECONDS, DEBUG flags,  DATE\_FORMAT, and so on are
examples of tunable parameters.

This is the area of greatest multiplication. Virtually every app you
pull into your project is going to have some tunable parameters.

Conclusion
----------

Armed with the understanding of the three kinds of values in your
settings, you may now be able to devise a superior method of organizing
them. You might start by sorting your settings.py file into three
sections. Or you might decide to break them out into separate files in a
package. Maybe you'll start using different tools to manage the three
types of settings differently. I don't know, I don't have the solution
to this problem right now, just this one nugget of insight.

What successful methods have you used to organize settings in large
projects?

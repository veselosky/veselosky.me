:Title: Web Developers: Infrastructure is part of your Application!
:Date: 2011-07-09
:Author: Vince Veselosky
:Slug: web-developers-infrastructure-is-part
:Category: Technology

.. post:: 2011-07-09
    :category: Technology

Web Developers: Infrastructure is part of your Application!
============================================================

One of the most difficult realities for web developers to face is that
their application code, elegant and beautiful as it may (or may not) be,
does not run in the ivory tower of Code Perfection. It runs on a real
machine (or several) in a real data center, competing for resources to
serve real clients, and tripping over all-too-real limitations of the
environment.

Operations people, those shadowy, pager-carrying folks that developers
call "sysadmins", know that there is so much more to delivering a web
application to its clients than simply deploying code. Web applications
are not delivered the way packaged software was in the 90's, on a
shrink-wrapped CD-ROM like a book. Web applications are not products at
all, they are services, and services don't get to say "bring your own
computer." Services must be delivered complete, with an entire stack of
running programs and systems underneath them.

A web application, whether Java, Ruby, Python, PHP, or LOLcode, is
incomplete until it is paired with a stack of servers and services on
which to run it. Which language runtime must be installed? Which version
of which web server(s)? How should the database server be tuned? How
much RAM allocated to memcached? When should the logs be rotated?
Developers often do not even think about these questions. When they do,
the answers are usually provided as a narrative requirements list which
some dedicated systems engineers must translate into a working system
somehow.

Systems automation has now reached the point where this infrastructure
can be delivered *as code* right along with the application code. Every
web application should be delivered with Puppet configurations or Chef
cookbooks to bring up a precisely tuned deployment stack designed for
the application. Cloud-based infrastructure means you can even deliver
the (virtual) hardware itself with the application. A good web
application should come with a "deploy\_to\_ec2" script for instant
production deployment.

Of course, there are `other
opinions <http://blog.heroku.com/archives/2011/6/28/the_new_heroku_4_erosion_resistance_explicit_contracts/>`__.
You may choose to outsource your operations work to a
platform-as-service like `Heroku <http://www.heroku.com/>`__ or `App
Engine <http://code.google.com/appengine/>`__. If you want to live in a
code-only world where infrastructure never crosses your mind, write your
code to target deployment environments like these, and get used to the
constraints they impose.

In my opinion, every web development team needs a systems engineer
embedded as part of the team, developing and codifying the
infrastructure alongside the application code. A web application
delivered without infrastructure automation is incomplete.

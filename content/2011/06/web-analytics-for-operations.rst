:Title: Web Analytics for Operations
:Date: 2011-06-19
:Author: Vince Veselosky
:Slug: web-analytics-for-operations
:Category: Technology

.. post:: 2011-06-19
    :author: Vince Veselosky
    :category: Technology

Web Analytics for Operations
=============================

Web analytics packages, from free to exorbitant, have grown in
complexity over the life of the web. That's great news for marketers
using the web as a tool to deliver a message to an audience. These tools
allow them to measure audience reach, time spent viewing a page, return
visits, session length, and other useful customer engagement factors
that helps shape the business strategy.

Unfortunately, while the marketers have won some great tools, where does
that leave the techies who need to operate the infrastructure? We don't
need to know how long a visitors spent on the site, nor to measure the
difference between a "page view" and an "interaction", we need to know
how many requests per second the application will generate. Where
marketing-oriented analytics goes to great pains to filter out automated
crawlers, we *desperately* need to know when a rampant robot is eating
up server resources.

There isn't much in the way of off-the-shelf software to fit our needs.
Mostly, we grow our own solutions, cobbled together with a tool here and
a tool there.

Lately I've had a need to do some log analysis over a large farm of
Apache web servers. I looked at a few open source packages that I knew
about: `AWStats <http://awstats.sourceforge.net/>`__ and
`Webalizer <http://www.mrunix.net/webalizer/>`__ being the perhaps the
best known. But I wasn't happy with either of these solutions. I wanted
a tool that would allow me to aggregate not just hits, but time spent
generating each page (in milliseconds), and I wanted to break down
traffic by five minute increments for a detailed shape in my graphs. So
finally, and somewhat reluctantly, I settled on
`analog <http://www.analog.cx/>`__.

Analog is not pretty nor user-friendly by any means. The configuration
file is touchy and somewhat arcane, and its convention for command line
parameters is non-standard. However, analog generates 44 different
reports, including time breakdowns from annual down to my desired five
minute interval, reports for successes, failures, redirects, and other
interesting outcomes, and a processing time report with fine resolution.
It can read compressed log files, and it has no problem processing files
out of chronological order.

Most importantly, analog is blazingly fast. It chewed through my 20
million lines of compressed Apache logs in six minutes. The speed at
which it consumes log files seems to be limited more by I/O rate than
CPU, though as a single-process, single threaded application, analog
will only tax one of your CPU cores. If you find CPU a limiting factor
on a multi-core system, you might try decompressing the files using gzip
and piping the output to analog. This allows the decompression to happen
in a separate process, and therefore on a separate CPU core, but I don't
know if that would speed things up much.

I'm still not entirely pleased with this solution. I would prefer a
solution that was a little more intuitive, and a little easier to
customize. Analog has plenty of knobs to turn, but there is no built-in
extension mechanism, so it makes me work pretty hard to pull out custom
metrics.

I would love to hear what other folks are using to analyze your Apache
logs. How do you get operational intelligence? Are you using remote
logging? Shoot me an email or leave a comment.

---
itemtype: Item/Page/Article
guid: "urn:UUID:3a0cf3ce-501a-4ab7-994c-c72c019d96ae"
Date: 2013-07-22 15:46
Author: Vince Veselosky
Slug: toward-reusable-content-repository
Category:
    name: Technology
    label: technology
Title: Toward a Reusable Content Repository
---

# Toward a Reusable Content Repository

There are a plethora of web-based content management systems and website
publishing systems in the world. Almost all of them are what you might
call "full stack solutions," meaning that they try to cover everything
you need to cook up a full publishing system, from content editing to
theming. Wordpress is the most obvious example, but there are hundreds
of such systems varying in complexity, cost, and implementation
platform.

So many of the available products are full stack solutions that the
market seems to have forgotten the possibility of anything else. What
would it look like if you could assemble a CMS from ready-made
components? What might those components be, and how would they
interoperate?

Every web CMS that I have seen can be divided into three major
components. They are:

-   Content Repository
-   Publishing Tools
-   Site Presentation

Each of those major components could further be described with a feature
set that might be implemented with sub-components. The Site Presentation
component might provide Themes or Sidebar Modules. The Publishing Tools
might be as simple as a bare textarea, or might include WYSIWYG with
spell checking and media embedding. The Content Repository is, almost
universally, a relational database.

The Content Repository, I believe, is the reason that so many systems
ship as full-stack solutions. There is no reusable Content Repository
component that meets the general needs of content management systems.
Without that central component, implementors are forced to bind both
their Publishing Tools and their Site Presentation systems tightly to
their own custom repository.

I would suggest the following feature set for a reusable Content
Repository.

-   Flexible and extensible information architecture, with a sensible
    default that will work out of the box for most users.
-   Web API for content storage and retrieval (not just a native
    language API).
-   Fielded search and full-text search over stored objects.
-   Optional version history for content objects.
-   Optional explicit relationships between content objects.
-   Pluggable backends, allowing for implementations at different
    scales.

Most internal repositories are quite weak in this feature set. For
example, very few embedded repositories implement full-text search. Of
those who do implement it, the implementation is often naive (SQL LIKE %
queries), leading to poor performance and poor scalability. 

Most embedded repositories implement only a native-language API, not a
web API, which prevents access to the content unless you also have
access to the code (some see this as a feature rather than a bug). 

Relational databases are notoriously bad at flexible information
architecture, so it has taken a lot of time and effort for content
management systems to add flexibility. Tools like [Drupal's Content
Construction Kit][] and [Wordpress Custom Post Types][] are getting
there, but without a common base architecture to build on, every
implementation is custom and incompatible with the next.

Regardless of the features listed above, there are two key requisites
that a reusable Content Repository must fulfill:

-   A published (and preferably simple) protocol for accessing its
    features.
-   A common base information architecture for content objects.

A Content Repository with these features would serve as a good backing
store for Publishing Tools and Site Presentation systems alike, and
would be agnostic to both. Any tool that understood the information
architecture and protocol used by the Content Repository could build on
it easily. Tools could ship with an embedded Content Repository, or
connect to an external one that might be hosted on a provider's servers.
Most importantly, your Site Presentation would no longer need to be
bundled with your Publishing Tools.

## Content Repository Protocol

There are very few contenders for content repository protocols. I only
know of two that might be reasonable to build on: [AtomPub][], and
[CMIS][]. To my mind, neither of these is a solution, but examining them
might help us develop a solution.

CMIS, despite its name, is geared more toward Document Management than
Content Management (IMHO). 

CMIS is far from being simple, and it makes some assumptions about
information architecture that make it awkward to use in many cases. For
example, it assumes a distinction between documents and folders, and
assumes that there is a single folder hierarchy for all content. This is
a restrictive and unnecessary constraint that does not fit all use
cases. 

It also requires repositories to implement a SQL-like query language,
forcing them to map content to a relational model even when it is not
stored that way. This makes implementations expensive, and makes certain
kinds of queries difficult to craft.

AtomPub, on the other hand, is simple and well-crafted, but defines only
a fraction of the feature set we would want in a protocol. For example,
it has no defined search protocol at all. Some implementations extend
the protocol to mimic Google's [GData][] search protocol, but it is not
a standard, and Google is no longer using it.

Implementers of a reusable Content Repository will have to face the
challenge of a new protocol for accessing it. That's a pretty high
barrier.

## Common Information Architecture

When I talk about a common information architecture, I am referring to
standardizing the shape of content objects in terms of the semantics of
its field structure. We need a commonly understood set of metadata, so
that tools can share content in a sensible way. Some metadata will be
required by Publishing Tools, other metadata will be useful to Site
Presentation systems, and some will be needed internally by the Content
Repository itself.

[Atom][] and [RSS][] are format standards, but each also defines a base
information architecture, and they are mostly compatible with each
other. Neither is sufficient for a full Content Repository, but any
information architecture incompatible with these formats is a
non-starter.

The [IPTC][] has done a huge amount of work in
developing interoperability standards for the news industry, which is
all about content management. Their [G2 News Architecture][] is
documented implicitly in the specifications for their XML exchange
formats, and in their [rNews metadata format for HTML][]. I think the G2
News Architecture is a great start on a common information architecture,
but a reusable Content Repository would need to define a simpler useful
subset of it if it wanted to gain wide adoption.

## Conclusion: A Hole in the Market? or No Market?

There are no real conclusions to draw from this, only questions to ask.
Namely, is there an under-served market for a reusable Content
Repository out there? Perhaps everyone is content with their vertically
integrated solutions, and no one is interested in mixing and matching
their presentation layer with different publishing tools.

I suspect, however, that the market for a reusable Content Repository
will emerge as a result of the proliferation of Internet accessible
devices. As people want access to their CMS across desktops, tablets,
smart phones, and other devices, the utility of separating the
presentation from the repository will become obvious.

Of course, the only way to know is to put in the hard work to build it,
and see who bites.


  [Drupal's Content Construction Kit]: https://www.drupal.org/project/cck
  [Wordpress Custom Post Types]: https://codex.wordpress.org/Post_Types
  [AtomPub]: http://bitworking.org/projects/atom/rfc5023.html
  [CMIS]: https://en.wikipedia.org/wiki/Content_Management_Interoperability_Services
  [GData]: https://developers.google.com/gdata/
  [Atom]: https://en.wikipedia.org/wiki/Atom_(standard)
  [RSS]: https://en.wikipedia.org/wiki/Rss
  [IPTC]: https://iptc.org/
  [G2 News Architecture]: https://iptc.org/standards/newsml-g2/
  [rNews metadata format for HTML]: http://dev.iptc.org/rNews

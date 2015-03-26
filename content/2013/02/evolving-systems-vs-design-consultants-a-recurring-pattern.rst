:Title: Evolving Systems vs Design Consultants - A Recurring Pattern
:Date: 2013-02-04
:Author: Vince Veselosky
:Slug: evolving-systems-vs-design-consultants
:Category: Technology

Evolving Systems vs Design Consultants — A Recurring Pattern
=============================================================

I often think of systems architecture as analogous to this word game I
played as a child. I don't know if the game has a name, but it is begun
by selecting two words, say "cat" and "dog". The goal is to begin with
one word, and end with the other. The rules are, you can change only one
letter each turn, and at the end of every turn, you must be left with a
true word. Hence, one way the game might play out is CAT -> COT -> COG
-> DOG. You might also get there through CAT -> COT -> DOT -> DOG.
Either path is valid, but there is no direct "upgrade" from CAT to DOG.

This is an apt analogy for the problem of systems architecture when
dealing with an operational system. The constraints of the system's
operation almost always prevent you from changing more than one
component at a time. Every change to any component must result in a
system that continues to operate. Real life systems also tend to have
far more components than the three-letter word, in fact they comprise
sentences, paragraphs, even whole novels.

In my work, I have occasionally had the good fortune to work with some
great outside consultants. To date, I have always found these
interactions to be productive and educational on multiple levels. It is
a remarkable luxury to pick the brain of someone who is truly an expert
in their field, and I try to take advantage of such opportunities
whenever I can. In those interactions, I have noticed a curious
recurring pattern.

Because of my role, I am often dealing with a consultant who is a
systems designer. This expert comes in to help us improve the design of
our systems. Unfortunately for her (or me), evolving operational systems
tend to be more organically grown than designed, and the consultant must
infer a design intent from examining the system as built, because the
original design intent is lost in the mists of time.

Invariably, a conversation will occur that goes something like this.

"I see that you are using a COT in this part of the system," the
consultant will say, attempting to hide a smirk. "A DOG would be much
more appropriate. Why don't you try using a DOG?"

Of course, the consultant is being tactful here. No person in his right
mind would use a COT as a replacement for a DOG. We, who built the
system, are embarrassed even to be showing anyone this particular
mangled part of our system. My response, when I have sufficient presence
of mind to compose a rational one, always has a similar pattern.

"Well yes, ideally you want a DOG there, but when we were building this
aspect of the system, we didn't have enough budget left for a pre-built
DOG component. It would have taken us several months to build a custom
DOG, which would have caused us to miss our launch deadline. But we had
a well-tested CAT component we had built for a different system, and
that mostly did the job. We found we could use that if we made some
adjustments to the FOOD component to accommodate the CAT, and we could
do that faster than building a whole new DOG."

Pause for a breath. Here's where the explanation gets messy. "After we
launched, we wanted to come back and fix this to use a DOG, as
originally designed, but of course we couldn't switch from a CAT to a
DOG without changing the FOOD component again. Since we can only change
one component at a time, during the upgrade process either the CAT or
the DOG would get the wrong FOOD at some point, breaking the system."
Remember that constraint about changing only one component at a time?

"We can't afford to break the system, we have live customers to support
now." Here's that other constraint, every change must result in an
operational system. Paying customers enforce that pretty strictly. It's
hard to say you're lucky if you don't have paying customers, but
sometimes it feels that way.

"So instead, we have migrated to using a COT. It's obviously not very
efficient, but it fits, and it eliminates the dependency on the FOOD
component (a COT does not eat). We're planning to replace the COT with a
COG in a future release, which should be a smooth transition, and free
up some system resources. Once that's done, we can use those resources
to re-engineer the FOOD component to support a DOG, assuming management
signs off on the additional cost."

By this time, depending on the consultant's level of experience, she
will either be staring at me like I'm a lunatic, or shaking her head
with a sympathetic grimace (usually the latter). In either case, the
response is usually some variant of "I see." And the final report will
advise, "Upgrade from COT to DOG ASAP."

*Sigh.*

There is no aspect of an organically grown system that could not be
better designed in retrospect. The shape of the completed system is not
governed solely by the appropriateness of the design/architecture. It is
largely shaped by convenience, the accessibility of specific tools or
components, the cost-benefit trade-offs and time constraints imposed
externally on the design process.

The line between sense and nonsense is squiggly, because it must be
drawn through the whole history of the system. And it's not always
obvious which side of the line you are on.

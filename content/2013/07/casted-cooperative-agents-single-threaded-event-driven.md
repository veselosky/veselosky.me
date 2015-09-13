Title: CASTED: Cooperative Agents, Single Threaded, Event Driven
Date: 2013-07-20 13:40
Author: Vince Veselosky
Slug: casted-cooperative-agents-single
Category: Technology

# CASTED: Cooperative Agents, Single Threaded, Event Driven

The past looked like this: A User logs into a Computer, launches a
Program, and interacts with it.

The future looks like this: The Computer on your desk runs a Program (in
the background) that collaborates with a Program running on the Computer
in your pocket and another Program running on a Computer in the Cloud,
operating on your behalf without the need to interact.

In the past, a Program and an Application were the same thing. More and
more, the Applications of today and tomorrow are made up of multiple
Programs running on multiple Computers but cooperating with each other
to achieve some utility for You (formerly the User).

The web development community has lately been very excited about
single-threaded event-driven servers like Node.js. These processes are
very good at maintaining a large number of connections, each of which
requires only a small amount of work. (These servers are not very good
at the inverse case, a small number of clients asking for very hard work
to be done. For that, you want a different model.)

This paradigm of a large number of connections and small amounts of work
fits neatly into the world where large numbers of processes collaborate
to create a useful result. Each process does a relatively small amount
of work, but the value emerges from the coordination of the processes
through their communication.

Example: There is a process on your phone that displays emails. There is
a process on the mail server that sends the messages to your phone.
There is a process that examines messages as they arrive at the server
to filter out junk mail. There is another process that examines the
messages to rank them by importance and places some in your Priority
Inbox. These processes are constantly running, on multiple servers,
operating on your behalf in the background.

Years ago, Tim O'Reilly was writing about [software above the level of a
single device][] as part of his Web 2.0 concept. Tim's classic example
is the iPod-iTunes-iStore triumvirate. You have servers on the Internet,
a desktop or laptop computer, and a small handheld device all
coordinating your data for you.

As more devices have computers embedded into them, there are more
opportunities for cross-device applications. And as more such
applications emerge, users will expect applications to coordinate across
devices like this. If you are designing a new application today, you'd
better be thinking about it as a distributed system of cooperating
processes.


  [software above the level of a single device]: http://radar.oreilly.com/archives/2007/11/software-above-the-level-of-a.html

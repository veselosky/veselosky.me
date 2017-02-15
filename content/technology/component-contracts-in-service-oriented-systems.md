---
guid: "urn:UUID:c4a90c81-16c8-4b14-aa2a-271e7fcf6ae3"
itemtype: Item/Page/Article
Date: 2013-11-11 17:09
Author: Vince Veselosky
Category:
    name: Technology
    label: technology
Title: Component Contracts in Service Oriented Systems
...

# Component Contracts in Service Oriented Systems

> PRINCIPLE: Relationships must be governed by contracts that are
> monitored for performance.

In order to build a reliable system that is composed of many services,
we need to have some guidelines for making the services reliable, both
in the technical sense, and in the more psychological sense of people
having confidence that things will work.

In a system of services, just like in a society, business relationships
should be governed by contracts that are monitored for performance.
Wherever a dependency exists between services, components, or teams, a
contract needs to exist to govern that dependency. That contract
comprises an agreement that defines the scope of responsibility of the
service provider and the service consumer. Here's a description of the
contracts each service should provide to its customers.

## Interface Contract

Every service must guarantee that its interface will remain consistent.
Assuming the service is delivered over HTTP, the interface includes:

-   Names and meanings of query string parameters.
-   Definitions of what HTTP headers are used or ignored.
-   Format of any document body submitted in the request
-   Format of the response body.
-   Use of HTTP methods.

Note that in this context, "consistent" does not have to mean
unchanging. It only means that no backwards incompatible changes can be
made. If your service is designed on the same RESTful hypermedia
principles of the web, your interface can remain consistent while
growing over time.

The Interface Contract must be documented and available to both your
customers and your delivery team. In fact, I would strongly recommend
that the Interface Contract be created and delivered before you begin
writing code for your service. It serves not only as documentation, but
as the specification for developers to work from, and as the starting
point for your test plan.

If changes require breaking compatibility, the best policy is to expose
a new version of your service at a different endpoint. You must then
establish a deprecation cycle to ensure clients have time to move to the
new version. Only after all clients have migrated to the new version can
you stop providing the old version. Such deprecation cycles can be very
long, depending on the complexity of the service and the velocity of
client development. Avoid backwards-incompatible changes in your
interface if at all possible.

## Service Level Agreement

Where your Interface Contract defines what your service will deliver,
the Service Level Agreement (SLA) governs how it will be delivered (or
how much). Things that need to be documented in your SLA include:

-   Availability: Uptime guarantees, scheduled maintenance windows, and
    communication policies around downtime.
-   Response time: What is the target for acceptable response times?
    What is the limit beyond which you will consider the service
    unavailable?
-   Throughput: How many requests is the service expected to handle? How
    many is the client allowed to send in a given time window?
-   Service classes: Are there certain kinds of requests that have
    non-standard response time or throughput requirements? Document them
    explicitly.

Your SLA should also describe how you monitor and report on conformance
with the agreement. Measurements of these aspects of performance are
usually called Key Performance Indicators (KPIs), and those measurements
should be made available to your customers as well as your delivery
team. These might be circulated in a regular email, or made available as
a web-based dashboard.

If there is a financial arrangement involved in using the service, your
SLA should also include remedies for non-conformance. However, even for
services designed for internal consumption only, the SLA should be
explicitly documented and agreed on by the service provider and the
service consumer.

Internally, you should also monitor the error rate of your application
and subtract it from your availability. A server that throws a 500
Internal Server Error was not available to the customer who received the
error. If a high percentage of requests result in errors, you have an
availability problem.

## Communication and Escalation Policy

The key to any relationship is communication. When you provide a
service, you must have a communication plan around delivering that
service to customers. Some of that communication is discussed above.
Issues to cover in your communication plan include:

-   Notification of changes and new service features.
-   Notification of deprecation cycles.
-   Reporting on service level performance.
-   Notification of incidents and how problems that affect customers are
    being managed.

In addition to these important communications from you to your
consumers, it is also important to establish how your customers will
communicate to you.

-   How can your customers contact you with questions or concerns?
-   How do they report problems?
-   What are the business hours for normal communications, and what is
    the policy for after-hours emergencies?

Establishing these policies up front will help people remain calm when
an emergency does occur. A clear communication plan can ensure that you
can focus on solving problems rather than fielding complaints. It also
ensures that the customer feels confident that you have things well in
hand.

## Conclusion

At any point where dependencies exist between systems (or teams), that
relationship must be governed by a contract. That contract comprises an
agreement that defines the scope of responsibility of the service
provider, including the interface for the service, a Service Level
Agreement that establishes Key Performance Indicators along with targets
and limits, and a Communication and Escalation Policy to ensure good
support for the running service.

With these parameters defined and clearly communicated, all parties
should have confidence in the reliability of the service (or at least a
clear path to getting there).

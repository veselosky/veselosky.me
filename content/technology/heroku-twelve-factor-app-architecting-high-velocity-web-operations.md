---
guid: "urn:UUID:a0d86e97-f0ec-4f62-96ae-9c4aa18c7968"
itemtype: Item/Page/Article
Date: 2012-02-11
Author: Vince Veselosky
Category:
    name: Technology
    label: technology
Title: "Heroku and the Twelve Factor App: Architecting for High Velocity Web Operations"
---

# Heroku and the Twelve Factor App: Architecting for High Velocity Web

A while back I wrote that [infrastructure should be delivered as code][]
along with every web application, because web applications are not run
by users, they are *operated* on behalf of users, and are therefore
incomplete without the infrastructure needed to operate them. In that
article, I mentioned [Heroku][], a platform-as-a-service company that
makes a living operating other people's web applications. Inspired by
their experience in web operations, some of those folks recently wrote a
guide to creating web applications that can be operated easily. They
call it [The Twelve Factor App][].

There is a great deal to be learned from this 12 Factor guide and the
platform Heroku has designed. Their business depends on consistent,
repeatable, and successful deployment and operation of web applications,
and they have this stuff precision-cut and well oiled. The guide, and
the Heroku platform, make a clear distinction between what is part of
the platform, and what is part of the application. Even if you are
heeding my earlier advice and delivering infrastructure with your
applications, you will benefit from understanding the points of
separation 12 Factor recommends between your application and the
platform on which it runs.

I had been planning to summarize each factor here, but the descriptions
at the web site are sufficiently concise that summary seems redundant.
Just click through the links for each factor and read, it will only take
you a few minutes, and it will be well worth your time.

[1. One codebase tracked in revision control, many deploys.][]

[2. Explicitly declare and isolate dependencies.][]

[3. Store config in the environment.][]

[4. Treat backing services as attached resources.][]

[5. Strictly separate build and run stages.][]

[6. Execute the app as one or more stateless processes.][]

[7. Export services via port binding.][]

[8. Scale out via the process model.][]

[9. Maximize robustness with fast startup and graceful shutdown.][]

[10. Keep development, staging, and production as similar as possible.][]

[11. Treat logs as event streams.][]

[12. Run admin/management tasks as one-off processes (see 6 above).][]



  [infrastructure should be delivered as code]: /technology/web-developers-infrastructure-is-part-of-your-application.html
  [Heroku]: https://www.heroku.com/
  [The Twelve Factor App]: https://12factor.net/
  [1. One codebase tracked in revision control, many deploys.]: https://12factor.net/codebase
  [2. Explicitly declare and isolate dependencies.]: https://12factor.net/dependencies
  [3. Store config in the environment.]: https://12factor.net/config
  [4. Treat backing services as attached resources.]: https://12factor.net/backing-services
  [5. Strictly separate build and run stages.]: https://12factor.net/build-release-run
  [6. Execute the app as one or more stateless processes.]: https://12factor.net/processes
  [7. Export services via port binding.]: https://12factor.net/port-binding
  [8. Scale out via the process model.]: https://12factor.net/concurrency
  [9. Maximize robustness with fast startup and graceful shutdown.]: https://12factor.net/disposability
  [10. Keep development, staging, and production as similar as possible.]: https://12factor.net/dev-prod-parity
  [11. Treat logs as event streams.]: https://12factor.net/logs
  [12. Run admin/management tasks as one-off processes (see 6 above).]: https://12factor.net/admin-processes

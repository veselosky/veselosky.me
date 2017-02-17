---
Item:
    itemtype: Item/Page/Catalog
    guid: "urn:UUID:8aba9c05-fd78-4ac7-8ff5-532ed62097f2"
    created: 2017-02-15T06:36:31.453366-05:00
    updated: 2017-02-15T06:36:31.453366-05:00
    published: 2017-02-15T06:36:31.453366-05:00
    title: "Articles by Date"
Webquills:
    scribes: [html, atom]
Catalog:
    queries:
        - "* | [?starts_with(itemtype, `Item/Page/Article`)]| reverse(sort_by(@, &updated))"
...

# Vince Veselosky's Blog Archive


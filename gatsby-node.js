/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/node-apis/
 */
const path = require("path")
const _ = require("lodash")
const moment = require("moment")
//const siteConfig = require("./data/SiteConfig")

/**
 * When article nodes are created, this "lifts" the metadata fields from
 * frontmatter to the node fields, supplying defaults.
 */
exports.onCreateNode = ({ node, actions, getNode }) => {
  const { createNodeField } = actions
  let category, date, description, itemtype, slug, tags, title

  // Only care about markdown nodes (articles)
  if (node.internal.type === "MarkdownRemark") {
    const fileNode = getNode(node.parent)
    const parsedFilePath = path.parse(fileNode.relativePath)

    // If we have frontmatter, interrogate it. NOTE: Webquills allows title
    // case metadata, check for both.
    if ("frontmatter" in node) {
      // Lift title & description.
      title = node.frontmatter.title || node.frontmatter.Title
      description = node.frontmatter.description || node.frontmatter.Description
      itemtype = node.frontmatter.itemtype

      // Lift category.
      category = node.frontmatter.category || node.frontmatter.Category

      // Lift tags
      tags = node.frontmatter.tags || node.frontmatter.Tags || []

      const dateStr =
        node.frontmatter.date ||
        node.frontmatter.Date ||
        node.frontmatter.updated ||
        node.frontmatter.Updated ||
        node.frontmatter.published ||
        node.frontmatter.Published

      date = moment(dateStr)
      // if (!date.isValid) console.warn(`WARNING: Invalid date.`, dateStr)
    } // if frontmatter

    /**
     * Now set values for fields not found in frontmatter
     */
    // TODO Pull the create/modify date from the file node.
    if (!date || !date.isValid) date = moment()
    if (!description) description = node.excerpt

    if (!title && "headings" in node && node.headings.length > 0) {
      const headline = node.headings.find(x => (x.depth === 1 ? true : false))
      if (headline) title = headline.value
    }
    // Generate slug without title
    if (!slug) {
      if (parsedFilePath.name !== "index" && parsedFilePath.dir !== "") {
        if (!category) category = _.startCase(parsedFilePath.dir)
        slug = `/${parsedFilePath.dir}/${parsedFilePath.name}`
      } else if (parsedFilePath.dir === "") {
        slug = `/${parsedFilePath.name}`
      } else {
        slug = `/${parsedFilePath.dir}/`
      }
    }
    // Append .html extension unless the slug ends in /
    if (!slug.endsWith("/")) slug += ".html"

    if (!tags) tags = ["_UNTAGGED"]

    createNodeField({ node, name: "category", value: category })
    createNodeField({ node, name: "date", value: date.toISOString() })
    createNodeField({ node, name: "description", value: description })
    createNodeField({ node, name: "itemtype", value: itemtype })
    createNodeField({ node, name: "slug", value: slug })
    // FIXME After adding tags here, query results in error below. WTF? VV 2019-04-16
    // GraphQLError: Cannot query field "tags" on type "MarkdownRemarkFields".
    // Not actually using tags in practice (yet) so I removed that from the query for now.
    createNodeField({ node, name: "tags", value: tags })
    createNodeField({ node, name: "title", value: title })
  } // if markdown
} // onCreateNode

exports.createPages = ({ graphql, actions }) => {
  const { createPage } = actions

  const articleTemplate = path.resolve(`./src/templates/article.jsx`)
  const categoryTemplate = path.resolve(`./src/templates/category.jsx`)
  return graphql(
    `
      {
        allMarkdownRemark(
          filter: { fields: { itemtype: { eq: "Item/Page/Article" } } }
          sort: { fields: [fields___date], order: DESC }
          limit: 1000
        ) {
          edges {
            node {
              excerpt
              fields {
                category
                date
                description
                slug
                title
              }
            }
          }
        }
      }
    `
  ).then(result => {
    if (result.errors) {
      throw result.errors
    }

    // Create article pages.
    const articles = result.data.allMarkdownRemark.edges
    let categories = {}

    articles.forEach((article, index) => {
      const previous = index === articles.length - 1 ? null : articles[index + 1].node
      const next = index === 0 ? null : articles[index - 1].node

      createPage({
        path: article.node.fields.slug,
        component: articleTemplate,
        context: {
          slug: article.node.fields.slug,
          previous,
          next,
        },
      })
      // Accumulate articles by category
      if (article.node.fields.category) {
        if (article.node.fields.category in categories === false) {
          categories[article.node.fields.category] = []
        }
        categories[article.node.fields.category].push(article)
      }
    })
    // TODO Generate list pages by category
    for (var category in categories) {
      createPage({
        path: `/${_.kebabCase(category)}/`,
        component: categoryTemplate,
        context: {
          articles: categories[category],
          category: category,
        },
      })
    }

    return null
  })
}

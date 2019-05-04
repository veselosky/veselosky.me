/**
 * Implement Gatsby's Node APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/node-apis/
 */
const path = require("path")
const _ = require("lodash")
// const moment = require("moment")
const webquills = require("./lib/webquills.js")
//const siteConfig = require("./data/SiteConfig")

/**
 * When article nodes are created, this "lifts" the metadata fields from
 * frontmatter to the node fields, supplying defaults.
 */
exports.onCreateNode = ({ node, actions, getNode }) => {
  const { createNodeField } = actions

  // Only care about markdown nodes (articles)
  if (node.internal.type === "MarkdownRemark") {
    console.info("MarkdownRemark node")
    let meta = webquills.extractRemarkMeta(node, getNode)
    console.info(meta)
    for (let key in meta) {
      createNodeField({ node, name: key, value: meta[key] })
    }
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

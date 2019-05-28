import React from "react"
import PropTypes from "prop-types"
import { graphql } from "gatsby"
import "bootstrap/dist/css/bootstrap.min.css"

import Layout from "../components/layout"
import SEO from "../components/seo"
import TeaseList from "../components/teaseList"

const BlogPage = props => {
  const { data } = props
  const posts = data.allMarkdownRemark.edges
  return (
    <Layout>
      <SEO title="All posts" keywords={[`blog`, `gatsby`, `javascript`, `react`]} />
      <TeaseList pages={posts} />
    </Layout>
  )
}

BlogPage.propTypes = {
  location: PropTypes.object,
  data: PropTypes.object,
}

export default BlogPage

export const pageQuery = graphql`
  query {
    allMarkdownRemark(
      filter: { fields: { itemtype: { eq: "Item/Page/Article" } } }
      sort: { fields: [fields___date], order: DESC }
    ) {
      edges {
        node {
          excerpt
          fields {
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

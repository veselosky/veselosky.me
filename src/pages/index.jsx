import React from "react"
import PropTypes from "prop-types"
import { graphql } from "gatsby"
import "bootstrap/dist/css/bootstrap.min.css"

import Layout from "../components/layout"
import SEO from "../components/seo"
import TeaseList from "../components/teaseList"

const IndexPage = props => {
  const { data } = props
  const siteTitle = data.site.siteMetadata.title
  const posts = data.allMarkdownRemark.edges
  return (
    <Layout location={props.location} title={siteTitle}>
      <SEO title="All posts" keywords={[`blog`, `gatsby`, `javascript`, `react`]} />
      <TeaseList pages={posts} />
    </Layout>
  )
}

IndexPage.propTypes = {
  location: PropTypes.string,
  data: PropTypes.object,
}

export default IndexPage

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
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

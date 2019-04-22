import React from "react"
import PropTypes from "prop-types"
import { graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"
import TeaseList from "../components/teaseList"

const ArticleTemplate = props => {
  const category = props.pageContext.category
  const articles = props.pageContext.articles
  const siteTitle = props.data.site.siteMetadata.title

  return (
    <Layout location={props.location} title={siteTitle}>
      <SEO title={category} />
      <TeaseList pages={articles} />
    </Layout>
  )
}

ArticleTemplate.propTypes = {
  data: PropTypes.object,
  pageContext: PropTypes.object,
  location: PropTypes.string,
}

export default ArticleTemplate

export const pageQuery = graphql`
  query SiteMetadata {
    site {
      siteMetadata {
        title
        author
      }
    }
  }
`

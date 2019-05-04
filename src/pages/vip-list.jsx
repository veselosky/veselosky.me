import React from "react"
import PropTypes from "prop-types"
import "bootstrap/dist/css/bootstrap.min.css"

import Layout from "../components/layout"
import SEO from "../components/seo"

const EmailSignupPage = () => {
  return (
    <Layout>
      <SEO title="VIP List" />
      <script type="text/javascript" src="https://app.mailerlite.com/data/webforms/871304/t3m9n5.js?v1" />
    </Layout>
  )
}

EmailSignupPage.propTypes = {
  location: PropTypes.object,
  data: PropTypes.object,
}

export default EmailSignupPage

import React from "react"
import { Link } from "gatsby"
import { Media } from "reactstrap"

const TeaseList = ({ pages }) => {
  const items = pages.map(({ node }) => {
    return (
      <Media tag="li" key={node.fields.slug}>
        <Media body>
          <Media heading>
            <Link to={node.fields.slug}>{node.fields.title}</Link>
          </Media>
          <small>{node.fields.date}</small>
          <p
            dangerouslySetInnerHTML={{
              __html: node.fields.description || node.excerpt,
            }}
          />
        </Media>
      </Media>
    )
  })
  return <Media list>{items}</Media>
}

export default TeaseList

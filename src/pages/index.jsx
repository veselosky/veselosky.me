import React from "react"
import PropTypes from "prop-types"
import { graphql } from "gatsby"
import Img from "gatsby-image"
import "bootstrap/dist/css/bootstrap.min.css"
import { Button, Col, Container, Jumbotron, Row } from "reactstrap"

import Layout from "../components/layout"
import SEO from "../components/seo"
import TeaseList from "../components/teaseList"

const IndexPage = props => {
  const { data } = props
  const posts = data.allMarkdownRemark.edges
  return (
    <Layout>
      <SEO title="Author of awesome fantasy" />
      <div>
        <Jumbotron>
          <Container>
            <Row>
              <Col md="8">
                <h1 className="display-3">Summoning Courage is here!</h1>
                <p className="lead">The final installment of The Piero Codex trilogy is now available!</p>
                <hr className="my-2" />
                <p>
                  <b>
                    A corrupt oligarchy. An ancient relic of power. A handful of seers stand between them.
                  </b>
                </p>
                <p>
                  Mack may be a dedicated member of the Order, but he’s always been a loner. Bad things happen
                  to people who get too close to him. Case in point, Recca has been imprisoned by the Seers
                  Guild for helping him protect the Piero Codex. Not to mention this week’s funeral. Mack is
                  tempted crawl into a bottle of bourbon to hide.
                </p>
                <p>
                  But the Order’s secrets have been leaked, and it’s only a matter of time before the Seers
                  Guild has all the pieces they need to steal the Piero Codex and its history-bending spells.
                  To stop them and save Recca, Mack will have to change his solo ways and become, not just a
                  team player, but a team leader. But the people he can trust are few, and those few don’t
                  necessarily like each other. Getting them to work together may be the hardest challenge of
                  his life.
                </p>
                <p>
                  With an unknown traitor inside the Order, and the Seers Guild willing to kill them all to
                  get the relic, can Mack turn enemies into allies in time to save his friend and the Codex?
                </p>
                <p>Don’t miss this exciting conclusion to The Piero Codex trilogy!</p>
              </Col>
              <Col md="4" style={{ textAlign: "right" }}>
                <div>
                  <a href="https://books2read.com/b/vv-summoning-courage">
                    <Img
                      fixed={data.latestCover.childImageSharp.fixed}
                      style={{ width: 200, display: "inline-block", margin: "0 10px 10px 0" }}
                    />
                  </a>
                </div>
                <p>
                  <a href="https://books2read.com/b/vv-summoning-courage">
                    <Button color="primary">Get the ebook</Button>
                  </a>
                </p>
                <hr className="my-2" />
                <h4>Never miss a release!</h4>
                <p>
                  Get your name on the VIP List to be notified whenever Vince has a new release. You will also
                  get occasional updates and reading recommendations, and even free stuff to read!
                </p>
                <p>
                  <a href="https://www.subscribepage.com/veselosky-vip-list">
                    <Button color="primary">Become a VIP</Button>
                  </a>
                </p>
              </Col>
            </Row>
          </Container>
        </Jumbotron>
      </div>
      <TeaseList pages={posts} />
    </Layout>
  )
}

IndexPage.propTypes = {
  location: PropTypes.object,
  data: PropTypes.object,
}

export default IndexPage

export const pageQuery = graphql`
  query {
    latestCover: file(relativePath: { eq: "news/cover-PC3-SummoningCourage.jpg" }) {
      childImageSharp {
        fixed(width: 200) {
          ...GatsbyImageSharpFixed
        }
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

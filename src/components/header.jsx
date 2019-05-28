import PropTypes from "prop-types"
import React from "react"
import { Nav, NavItem, NavLink } from "reactstrap"

import HeaderBackground from "../images/CF-Banner.jpg"
import headerStyles from "./header.module.css"

const Header = ({ siteTitle }) => (
  <header
    className="px-3 pt-3"
    style={{
      backgroundImage: `url(${HeaderBackground})`,
      backgroundPosition: `center`,
      backgroundRepeat: `repeat-x`,
      backgroundSize: `contain`,
      color: `white`,
      textDecoration: `none`,
    }}
  >
    <h1>
      <a href="/" className={headerStyles.link}>
        {siteTitle}
      </a>
    </h1>
    <p className="h6">Author of Awesome Fantasy</p>
    <Nav className="justify-content-end">
      <NavItem>
        <NavLink className={headerStyles.link} href="/">
          Home
        </NavLink>
      </NavItem>
      <NavItem>
        <NavLink className={headerStyles.link} href="/seers-guild">
          Seers Guild
        </NavLink>
      </NavItem>
      <NavItem>
        <NavLink className={headerStyles.link} href="/vip-list">
          VIP List
        </NavLink>
      </NavItem>
      <NavItem>
        <NavLink className={headerStyles.link} href="/blog">
          Blog
        </NavLink>
      </NavItem>
    </Nav>
  </header>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header

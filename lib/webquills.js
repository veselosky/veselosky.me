const path = require("path")
const _ = require("lodash")
const moment = require("moment")
var webquills = {}

webquills.dateValidator = function(dateString) {
  const mydate = moment(dateString)
  if (mydate.isValid) {
    return mydate.toISOString()
  }
  console.warn(`Invalid date value: ${dateString}`)
  return null
}

// Validation functions attempt to coerce correct types from provided values.
// If unable to do so, will toss the value with a warning.
webquills.validatorFor = {
  created: webquills.dateValidator,
  date: webquills.dateValidator,
  published: webquills.dateValidator,
  updated: webquills.dateValidator,
}

webquills.extractRemarkMeta = function(node, getNode) {
  const fileNode = getNode(node.parent)
  const parsedFilePath = path.parse(fileNode.relativePath)
  let meta = {}

  // If we have frontmatter, interrogate it. NOTE: Webquills allows mixed case
  // metadata keys. We normalize them for internal use.
  if ("frontmatter" in node) {
    Object.keys(node.frontmatter)
      .sort()
      .reverse() // prefer the uppercased versions, lower may be artifacts of the schema
      .forEach(userProp => {
        if (node.frontmatter[userProp] === null || node.frontmatter[userProp] === "") {
          return
        }
        let key = userProp.toLowerCase()
        if (this.validatorFor[key]) {
          // Known keys get validated/fixed
          console.debug(`Validating ${key} (${node.frontmatter[userProp]})`)
          meta[key] = this.validatorFor[key](node.frontmatter[userProp])
        } else {
          console.debug(`Passing through ${key} (${node.frontmatter[userProp]})`)
          // Unknown keys pass through as-is
          meta[key] = node.frontmatter[userProp]
        }
      })
  } // if frontmatter

  /**
   * Now set values for fields not found in frontmatter
   */
  if (!meta.description) meta.description = node.excerpt

  // If no explicit title, use the top-level headline
  if (!meta.title && "headings" in node && node.headings.length > 0) {
    const headline = node.headings.find(x => (x.depth === 1 ? true : false))
    if (headline) meta.title = headline.value
  }
  // Generate "slug", a special name for many gatsby plugins containing the page URL
  if (!meta.slug) {
    if (parsedFilePath.name !== "index" && parsedFilePath.dir !== "") {
      if (!meta.category) meta.category = _.startCase(parsedFilePath.dir)
      meta.slug = `/${parsedFilePath.dir}/${parsedFilePath.name}`
    } else if (parsedFilePath.dir === "") {
      meta.slug = `/${parsedFilePath.name}`
    } else {
      meta.slug = `/${parsedFilePath.dir}/`
    }
  }
  // Append .html extension unless the slug ends in /
  if (!meta.slug.endsWith("/")) meta.slug += ".html"

  if (!meta.date) {
    meta.date = meta.updated || meta.published || meta.created
  }
  // To ensure proper gatsby schema creation, this field needs to be a non-empty array.
  if (!meta.tags) meta.tags = ["_UNTAGGED"]

  return meta
}

module.exports = webquills

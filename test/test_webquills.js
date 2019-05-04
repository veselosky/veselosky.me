const webquills = require("../lib/webquills")
const expect = require("chai").expect
const moment = require("moment")

describe("webquills.dateValidator", function() {
  it('parses "2012-05-13 22:19"', function() {
    expect(webquills.dateValidator("2012-05-13 22:19")).is.equal("2012-05-14T02:19:00.000Z")
  })
})
describe("webquills.extractRemarkMeta", function() {
  it(`is a function`, function() {
    expect(webquills.extractRemarkMeta).is.a("function")
  })

  var testdata = require("./markdownremark_normal.json")
  console.log(testdata)

  function getNode(parent) {
    return parent
  }
  describe("returns an object whose", function() {
    var meta = webquills.extractRemarkMeta(testdata, getNode)
    it("title is a string", function() {
      expect(meta.title).is.a("string")
    })
    it("date is a normalized date string", function() {
      expect(meta.date).is.equal("2012-05-14T02:19:00.000Z")
    })
    it("slug matches its path", function() {
      expect(meta.slug).to.match(new RegExp("^/business/a-framework-for-innovation.html$"))
    })
    it("description defaults to the excerpt", function() {
      expect(meta.description).to.equal(testdata.excerpt)
    })
  })
})

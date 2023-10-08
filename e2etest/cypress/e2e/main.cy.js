const baseURL = "https://butopea.com/";

describe("Banner square overlay", () => {
  it("should contain text and a button", () => {
    cy.visit(baseURL);
    const square = ".banner-square-overlay.flex";
    cy.get(square).find("p").should("exist");
    cy.get(square).find("button").should("exist");

    cy.get(square)
      .find(".banner-square-overlay-heading > p")
      .then(($value) => {
        cy.log("Text: ", $value.text().trim());
      });

    cy.get(square)
      .find(".banner-square-overlay-cta > button")
      .then(($value) => {
        cy.log("Button: ", $value.text().trim());
      });
  });
});

describe("Banner square column", () => {
  it("should get image url of column", () => {
    cy.visit(baseURL);
    cy.get(".banner-square-column")
      .find(".banner-square-image > img")
      .then(($imgs) => {
        const imgsArray = $imgs
          .map((index, el) => Cypress.$(el).attr("src"))
          .get();
        cy.log("image: ", imgsArray[1]);
      });
  });
});

describe("Click on new products tab", () => {
  it("should click on new products tab", () => {
    cy.visit(baseURL);
    cy.get("div[data-v-78adabb3].tab > button").eq(2).click({ timeout: 10000 });
    const listing = cy.get(".product-listing");

    listing.get(".product-name").then(($title) => {
      const titlesArray = $title.map((index, el) => Cypress.$(el).text()).get();
      cy.log("product titles: ", titlesArray);
    });

    listing.get('[data-testid="productLink"]').then(($prodLink) => {
      const hrefsArray = $prodLink
        .map((index, el) => Cypress.$(el).attr("href"))
        .get();
      cy.log("product link: ", hrefsArray);
    });

    listing.get(".preview-img-item").then(($imgs) => {
      const imgsArray = $imgs
        .map((index, el) => Cypress.$(el).attr("src"))
        .get();
      cy.log("img urls: ", imgsArray);
    });

    listing.get(".lh30").then(($prices) => {
      const pricesArray = $prices
        .map((index, el) => Cypress.$(el).text())
        .get();
      cy.log("product prices: ", pricesArray);
    });
  });
});

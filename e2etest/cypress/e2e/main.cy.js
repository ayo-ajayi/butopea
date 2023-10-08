const baseURL = "https://butopea.com/";

describe("Banner square overlay", () => {
  it("should contain text and a button", () => {
    //go to the main page of the website
    cy.visit(baseURL);

    //take a screenshot before any action
    cy.screenshot("BannerSquareOverlay/Initial");

    const square = ".banner-square-overlay.flex";

    //check if button and text exist in the square
    cy.get(square).find("p").should("exist");
    cy.get(square).find("button").should("exist");

    //get the text
    cy.get(square)
      .find(".banner-square-overlay-heading > p")
      .then(($value) => {
        cy.log("Text: ", $value.text().trim());
      });

    //get the button label
    cy.get(square)
      .find(".banner-square-overlay-cta > button")
      .then(($value) => {
        cy.log("Button: ", $value.text().trim());
      });

    //take a screenshot after all actions
    cy.get(square).screenshot("BannerSquareOverlay/Final");
  });
});

describe("Banner square column", () => {
  it("should get image url of column", () => {
    //visit the main page and take intial screenshot
    cy.visit(baseURL).screenshot("BannerSqrCol/Initial");

    //get the image url of the second column
    cy.get(".banner-square-column")
      .find(".banner-square-image > img")
      .eq(1)
      .then(($img) => {
        cy.log("image: ", $img.attr("src"));
      });

    //take a screenshot of the column
    cy.get(".banner-square-column")
      .find(".banner-square-image > img")
      .eq(1)
      .screenshot("BannerSqrCol/Final");
  });
});

describe("Click on new products tab", () => {
  it("should click on new products tab", () => {
    //visit the main page and take intial screenshot
    cy.visit(baseURL);
    cy.screenshot("NewProductsTab/Initial");

    //click on new products tab and wait for the page to load
    cy.get("div[data-v-78adabb3].tab > button").eq(2).click({ timeout: 10000 });

    //take screenshots
    cy.screenshot("NewProductsTab/OnClick");
    const listing = cy.get(".product-listing");
    listing.screenshot("NewProductsTab/AfterClick");

    //list the product titles, links, images and prices
    listing.get(".product-name").then(($title) => {
      //use jquery to get the text of the title
      const titlesArray = $title.map((index, el) => Cypress.$(el).text()).get();
      cy.log("product titles: ", titlesArray);
    });

    listing.get('[data-testid="productLink"]').then(($prodLink) => {
      const hrefsArray = $prodLink

        //use jquery to get the href attribute of the link
        .map((index, el) => Cypress.$(el).attr("href"))
        .get();
      cy.log("product link: ", hrefsArray);
    });

    listing.get(".preview-img-item").then(($imgs) => {
      const imgsArray = $imgs

        //use jquery to get the src attribute of the image
        .map((index, el) => Cypress.$(el).attr("src"))
        .get();
      cy.log("img urls: ", imgsArray);
    });

    listing.get(".lh30").then(($prices) => {
      const pricesArray = $prices

        //use jquery to get the text of the price
        .map((index, el) => Cypress.$(el).text())
        .get();
      cy.log("product prices: ", pricesArray);
    });

    //take a screenshot after all actions
    cy.screenshot("NewProductsTab/AfterListing");
  });
});

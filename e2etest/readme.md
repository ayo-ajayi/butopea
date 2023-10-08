# Documentation: Cypress E2E Testing for Butopea Website

This readme outlines the Cypress tests written for the website "https://butopea.com/". The primary objective is to check the existence of certain elements on the website and extract relevant data.

## Prerequisites

- Ensure you have `node.js` and `npm` installed on your system.

## Execution

1. **Navigate to the project directory:**
    ```bash
    cd <project_path>
    ```
2. **Install dependecies via npm:**
    ```bash

    npm i
    ```

3. **Run the tests:**
    ```bash
    npx cypress run --spec cypress/e2e/main.cy.js
    ```

## Code Workflow:

### 1. **Banner Square Overlay Test:**

- **URL Visitation:**
  The test starts by visiting the main page of the website. 

- **Initial Screenshot:**
  An initial screenshot named `BannerSquareOverlay/Initial` is taken before any operations.

- **Element Checks:**
  Checks the existence of a paragraph and button inside the banner square overlay.

- **Logging Text and Button Label:**
  Extracts and logs the text and the label of the button.

- **Final Screenshot:**
  A final screenshot named `BannerSquareOverlay/Final` is taken to capture the square.

### 2. **Banner Square Column Test:**

- **URL Visitation:**
  Begins by visiting the main page.

- **Initial Screenshot:**
  An initial screenshot named `BannerSqrCol/Initial` is taken.

- **Extracting Image URL:**
  The URL of the second image in the `.banner-square-column` is extracted and logged.

- **Final Screenshot:**
  A screenshot named `BannerSqrCol/Final` is taken of the second image in the column.

### 3. **New Products Tab Test:**

- **URL Visitation:**
  Starts by navigating to the main page.

- **Initial Screenshot:**
  An initial screenshot named `NewProductsTab/Initial` is taken.

- **Click Operation:**
  Clicks on the new products tab.

- **Mid and Post-Click Screenshots:**
  Screenshots named `NewProductsTab/OnClick` and `NewProductsTab/AfterClick` are taken to capture the site's states.

- **Data Extraction and Logging:**
  Extracts and logs product titles, product links, image URLs, and product prices from the new products listing.

- **Final Screenshot:**
  A final screenshot named `NewProductsTab/AfterListing` captures the end state.

---

## Screenshots:

All screenshots are stored in the [cypress/screenshots/main.cy.js](./cypress/screenshots/main.cy.js) directory.

## Conclusion:

These Cypress tests offer a structured approach to automatically verify elements and content on the Butopea website. They ensure a consistent user experience by validating that the main components and data are present and correctly rendered.

## Author:

- [Ayomide Ajayi](https://github.com/ayo-ajayi)


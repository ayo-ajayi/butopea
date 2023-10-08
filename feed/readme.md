# Documentation: Product Feed (XML) from Database

This readme explains how to fetch product data from an SQLite database, process the results, and save the structured data into an XML file.

## Prerequisites

- Ensure you have `python` installed on your system.

## Setup and Execution

1. **Navigate to the project directory:**
    ```bash
    cd <project_path>
    ```

2. **Create and activate a virtual environment:**

    - **Setting up the environment:**
        ```bash
        python -m venv <virtual_environment_name>
        ```

    - **Activating the environment:**
        ```bash
        cd <virtual_environment_name>/Scripts
        source activate
        ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the script:**
    ```bash
    python main.py
    ```

## Code Workflow:

### 1. **Database Connection and Data Fetching:**
   
- **Establishing Connection:**
  The script uses the `sqlalchemy` library to create a connection (`engine`) to the SQLite database [data.sqlite](./data.sqlite).

- **Creating a Session:**
  A session is initialized in order to interact with the database.

- **Executing the Query:**
  - The query primarily involves three tables: `product_description`, `product`, and `manufacturer`. It also optionally includes data from `product_image` using a `LEFT JOIN`.
  - `INNER JOIN` is used between `product_description` and `product` to fetch only products that adhere to the Google product data specification.
  - Another `INNER JOIN` between `product` and `manufacturer` ensures the brand's presence for each product.
  - `LEFT JOIN` with `product_image` is utilized to fetch optional additional images associated with each product, as well as the order in which they should appear.
  - Multiple `<additional_image_link>` elements appear in one product in the xml because this is allowed in the google spec.
  
### 2. **Data Transformation:**

- **Base URL Definition:**
  The script uses a base URL (`https://butopea.com/`) to construct product URLs and image URLs.

- **Data Structuring:**
  Raw data from the database is transformed into a Python dictionary, ensuring that each product ID acts as a unique key. 
  - Additional image links associated with each product are grouped together.
  - The sort order is maintained for these additional image links.

### 3. **XML Generation:**

- **Building the XML Data Structure:**
  The script structures the transformed data into a dictionary format compatible with the XML structure, where each product entry forms a `product` element under the root `feed` element.

- **Converting Dictionary to XML:**
  The `xmltodict` library is used to serialize the Python dictionary into an XML string.

- **Saving to File:**
  The XML string is then saved to a [feed.xml](./feed.xml) file. UTF-8 encoding is utilized to ensure special characters are correctly encoded.

### Important Notes:

- **Error Handling:** Throughout the script, error-handling mechanisms are in place, primarily using `try-except` blocks. This ensures that any potential issues, whether during data fetching or XML generation, are gracefully managed, and descriptive error messages are printed to the console.
  
- **Memory Management:** After processing, temporary data structures that are no longer needed (like the `products_dict` dictionary) are explicitly deleted to free up memory.

---

## Conclusion:

The script provides an automated way to extract, transform, and save product data from an SQLite database into a structured XML file, adhering to google product data specification.


## Author:

- [Ayomide Ajayi](https://github.com/ayo-ajayi)

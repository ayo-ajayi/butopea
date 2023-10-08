#import the required libraries
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import xmltodict

#create engine and session
engine = create_engine("sqlite:///data.sqlite")
session = sessionmaker(bind=engine)()


#use a try except block to catch any errors that may occur in the session.execute() function
try:
    #execute the query using the session object

    result = session.execute(
        text(
            """
    SELECT 
        pd.product_id AS id, 
        pd.name AS title, 
        pd.description, 
        p.image AS image_link,
        pi.image AS additional_image_link,
        pi.sort_order,
        p.quantity AS availability, 
        p.price, 
        m.name AS brand,
        p.status AS condition
    FROM product_description AS pd
    JOIN product AS p ON pd.product_id = p.product_id
    JOIN manufacturer AS m ON p.manufacturer_id = m.manufacturer_id
    LEFT JOIN product_image AS pi ON pd.product_id = pi.product_id
    WHERE p.status != '0'
    """
        )
    )
except Exception as e:
    print("sql exec error: "+ str(e))

#close the session
finally:
    session.close()

base_url = "https://butopea.com/"


if result == []:
    print("No products found")
    exit()

products_dict = {}

#loop through the array of results and attach the additional image links to the appropriate product id
for row in result:

    #assert the result into an idiomatic python dictionary
    prod_dict = row._asdict()
    prod_id = prod_dict["id"]

    #create the product link by appending each product id to the base url
    prod_dict["link"] = base_url +"p/"+ str(prod_id)

    #create the image link by appending each image_link from db to the base url
    prod_dict["image_link"] = base_url + prod_dict["image_link"]

    
    #if the product id of the row from the database is not already in the products_dict, add it to the products_dict
    #the product id is the focus and the products_dict is now a key-value pair,
    # where it's id is the key and the value is the dictionary (prod_dict) that contains additional image links of each product id together in one place
    if prod_id not in products_dict:
        products_dict[prod_id] = prod_dict

        #create an empty array that will hold the additional image links
        products_dict[prod_id]["additional_image_links"] = []
    
    
    if prod_dict["additional_image_link"]:
        
        # if additional_image_link exists for the row in the table, append it to the base_url to form a complete link
        prod_dict["additional_image_link"] = base_url + prod_dict["additional_image_link"]

        #collect the addtional image links and their sort order into the products_dict value that corresponds to the product id
        #the value is a dictionary that has "additional_image_links" as the key and an array of tuples as the value
        products_dict[prod_id]["additional_image_links"].append((prod_dict["additional_image_link"], prod_dict["sort_order"]))

        #delete the additional_image_link and sort_order keys from the products_dict[prod_id] dictionary since the values are already read
        if "additional_image_link" in products_dict[prod_id]:
            del products_dict[prod_id]["additional_image_link"]
        if "sort_order" in products_dict[prod_id]:
            del products_dict[prod_id]["sort_order"]

products=[]

#take out all the values from the products_dict and put them in an array (instead of the dictionary that has the product id as the key)
for prod_id in products_dict:
    if products_dict[prod_id]["additional_image_links"]:

        #sort the additional image links by their sort order
        sorted_links = sorted(products_dict[prod_id]["additional_image_links"], key=lambda x: int(x[1]))

        #create an additional_image_link key and assign it the value of the sorted additional image links
        products_dict[prod_id]["additional_image_link"] = [link[0] for link in sorted_links]

        #important: del the additional_image_links key from the products_dict[prod_id] dictionary since the values are already read and to avoid confusion
        del products_dict[prod_id]["additional_image_links"]
    #append the values to the products array
    products.append(products_dict[prod_id])

#free up memory
del products_dict
del result


#save the products to a an xml file
try:
    feed = {"feed":{
        "product": products
    }}

    #serialize the feed object to xml
    xml_data = xmltodict.unparse(feed, pretty=True)

    #open a file for writing with utf-8 encoding because of special characters
    f= open("feed.xml", "w", encoding="utf-8")
    f.write(xml_data)
    print("XML file created successfully")

    #close the file
    f.close()
except Exception as e:
    print("dict to xml error: "+ str(e))

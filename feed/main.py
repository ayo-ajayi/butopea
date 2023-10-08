from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
import xmltodict
engine = create_engine("sqlite:///data.sqlite")
session = sessionmaker(bind=engine)()

result = []
try:
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
session.close()

base_url = "https://butopea.com/"
products_dict = {}
result_list = list(result)
for i in range(len(result_list)):
    prod_dict = result_list[i]._asdict()
    prod_id = prod_dict["id"]
    prod_dict["link"] = base_url +"p/"+ str(prod_id)
    prod_dict["image_link"] = base_url + prod_dict["image_link"]
    if prod_id not in products_dict:
        products_dict[prod_id] = prod_dict
        products_dict[prod_id]["additional_image_links"] = []
    
    if prod_dict["additional_image_link"]:
        prod_dict["additional_image_link"] = base_url + prod_dict["additional_image_link"]
        products_dict[prod_id]["additional_image_links"].append((prod_dict["additional_image_link"], prod_dict["sort_order"]))
    if "additional_image_link" in products_dict[prod_id]:
        del products_dict[prod_id]["additional_image_link"]
    if "sort_order" in products_dict[prod_id]:
        del products_dict[prod_id]["sort_order"]

products=[]
for prod_id in products_dict:
    if products_dict[prod_id]["additional_image_links"]:
        sorted_links = sorted(products_dict[prod_id]["additional_image_links"], key=lambda x: int(x[1]))
        products_dict[prod_id]["additional_image_link"] = [link[0] for link in sorted_links]
        del products_dict[prod_id]["additional_image_links"]
    products.append(products_dict[prod_id])
    
try:
    feed = {"feed":{
        "product": products
    }}
    xml_data = xmltodict.unparse(feed, pretty=True)
    f= open("feed.xml", "w", encoding="utf-8")
    f.write(xml_data)
    print("XML file created successfully")
except Exception as e:
    print("dict to xml error: "+ str(e))

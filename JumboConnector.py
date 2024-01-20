"""
JumboConnector Module

This module defines the JumboConnector class for interacting with the Jumbo API to retrieve food information.
It includes methods for searching food, retrieving product details, and displaying information about products.
"""
from supermarktconnector import jumbo

# Author and version information
__author__ = "J. Gray"
__version__ = "1.0"

# This code is licensed under the MIT License.
# See the LICENSE file for details.

class JumboConnector:

    jumbo_api_version = "v17"
    connector = jumbo.JumboConnector()
    current_product_id = {}
    current_products = {}
    incompatible_products = []

    def __init__(self):
        """
        Initialize JumboConnector with the specified API version.
        """
        # package is out of date, setting version manually
        self.connector.jumbo_api_version = self.jumbo_api_version

    def __str__(self):
        """
        Return a string representation of the JumboConnector.
        """
        return f"Show me the money version: {self.jumbo_api_version}"

    def search_food(self, food):
        """Returns all food matching search term
        params:
            food: Search term [string]
        output
            API response containing search term [dict]"""
        for product in self.connector.search_products(food)["products"]["data"]:
            if product["productType"] == "Product":
                self.current_products[product["id"]] = {
                    "title": product["title"],
                    "price": product["prices"]["price"]["amount"],
                    "unitPrice": product["prices"]["unitPrice"]["price"]["amount"],
                    "unit": product["prices"]["unitPrice"]["unit"]
                }
            else:
                self.incompatible_products.append(product["id"])
        return self.current_products

    def get_nutrition(self, id):
        """
        Returns nutritional information for a product.

        Args:
            id (str): Product ID.

        Returns:
            list: Nutritional information entries.
        """
        try:
            return self.connector.get_product_details(id)\
                                    ['product']['data']\
                                    ['nutritionalInformation'][0]\
                                    ['nutritionalData']['entries']
        except IndexError:
            return None

    def get_products(self):
        """
        Print information about current products
        """
        for key in self.current_products.keys():
            title = self.current_products[key]['title']
            price = self.current_products[key]['price']
            unitprice = self.current_products[key]['unitPrice']
            unit = self.current_products[key]['unit']
            print(unitprice/100, f"€/{unit}", "---", title)

    def get_product_details(self):
        """Returns complete description of product matching id
        params:
            id : product ID [string]
        output:
            API response containing product information [dict]"""

        for id in self.current_products.keys():
            if not id in self.incompatible_products:
                try:
                    print(self.current_products[id]['title'])
                    for nutrition in self.get_nutrition(id):
                        print(nutrition['name'], nutrition['valuePer100g'])
                except:
                    pass

if __name__ == "__main__":
    print(JumboConnector)

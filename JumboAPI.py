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
        products = []

        for product in self.connector.search_products(food)["products"]["data"]:
            if product["productType"] == "Product":
                products.append({
                    "title": product["title"],
                    "price": product["prices"]["price"]["amount"],
                    "unitPrice": product["prices"]["unitPrice"]["price"]["amount"],
                    "unit": product["prices"]["unitPrice"]["unit"]
                })
            else:
                pass
        return products


if __name__ == "__main__":
    j1 = JumboConnector()
    print(j1.search_food("aardappeltjes"))
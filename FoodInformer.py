"""
FoodInformer Module

This module defines the FoodInformer class for searching and retrieving food information
using JumboConnector. It utilizes the JumboConnector, ShoppingCart, and Product classes
to interact with the Jumbo API and manage a shopping cart.
"""

# 3rd party import
import pandas as pd

# Local import
from Product import Product
from ShoppingCart import ShoppingCart
from JumboConnector import JumboConnector

# Author and version information
__author__ = "J. Gray"
__version__ = "1.0.0"

# This code is licensed under the MIT License.
# See the LICENSE file for details.

class FoodInformer:
    """A class for searching and retrieving food information using JumboConnector."""

    def search_food(self, product_name):
        """
        Search for a product using JumboConnector and add it to the shopping cart.

        Parameters:
        - product_name (str): The name of the product to search for.

        Returns:
        - pd.DataFrame: A DataFrame containing information about the added products.
        """
        c1 = ShoppingCart()
        j1 = JumboConnector()
        j1.current_products = {}
        j1.search_food(product_name)

        for product_id in j1.current_products:
            product_info = j1.current_products[product_id]
            c1.add_product(
                Product(name=product_info['title'],
                        stock_price=product_info['price'],
                        unit_price=product_info['unitPrice'],
                        unit=product_info['unit']))
        products = self.get_products(c1)
        return self.get_dataframe(products)

    def get_products(self, products):
        """
        Get all products in the shopping cart.

        Returns:
        - list: A list of Product objects in the shopping cart.
        """
        return products.get_all_products()

    def get_dataframe(self, products):
        """
        Convert the products in the shopping cart to a Pandas DataFrame.

        Returns:
        - pd.DataFrame: A DataFrame containing information about the products in the shopping cart.
        """
        columns = ["product", "stock_price", "unit_price", "unit"]
        df = pd.DataFrame(columns=columns)

        for i, product in enumerate(products):
            df.loc[i] = [product.name, product.stock_price, product.unit_price, product.unit]

        return df

if __name__ == "__main__":
    informer = FoodInformer()
    print(informer.search_food("Biet rode").sort_values(by="unit_price"))
    print(informer.search_food("Kool boeren").sort_values(by="unit_price"))
    print(informer.search_food("doperweten").sort_values(by="unit_price"))

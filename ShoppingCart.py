"""
ShoppingCart Module

This module defines the ShoppingCart class for managing a collection of products.
The class includes methods for getting all products, adding a product, and providing a string representation.
"""

# Dunder author and version information
__author__ = "J. Gray"
__version__ = "1.0"

# This code is licensed under the MIT License.
# See the LICENSE file for details.

class ShoppingCart:
    """
    ShoppingCart class for managing a collection of products.
    """

    products = []

    def get_all_products(self):
        """
        Get all products in the shopping cart.

        Returns:
            list: List of products in the shopping cart.
        """
        return self.products

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        Args:
            product: The product to be added to the shopping cart.
        """
        self.products.append(product)

    def __repr__(self):
        """
        Return a string representation of the shopping cart.

        Returns:
            str: String representation of the shopping cart.
        """
        return f"Cart containing: {self.products}"

    def empty(self):
        self.products = []

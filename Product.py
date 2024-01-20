"""
Product Module

This module defines the Product data class for representing information about a product.
The class includes attributes for the product name, stock price, unit price, and unit.
It also defines a custom comparison method for sorting products based on unit price.
"""

from dataclasses import dataclass

# Dunder author and version information
__author__ = "J. Gray"
__version__ = "1.0"

# This code is licensed under the MIT License.
# See the LICENSE file for details.

@dataclass(kw_only=True)
class Product:
    """
    Product class for representing information about a product.
    """

    name: str
    stock_price: int
    unit_price: int
    unit: str

    def __lt__(self, other):
        """
        Custom comparison method for sorting products based on unit price.

        Args:
            other (Product): Another product for comparison.

        Returns:
            bool: True if the current product's unit price is less than the other product's unit price.
        """
        return self.unit_price < other.unit_price


if __name__ == "__main__":
    print(Product)
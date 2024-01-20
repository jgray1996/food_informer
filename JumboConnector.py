from supermarktconnector import jumbo
from operator import itemgetter
import json
import logging

"""
About:
    This class handles the connection to the supermarket
    through the supermarketconnector framework built around the
    jumbomobile API.
Usage:
    JumboConnector.py
Author:
    James Gray
Version:
    v0.1
License:
    MIT License

    Copyright (c) 2017 David Whipp

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

class JumboConnector:


    jumbo_api_version = "v17"
    connector = jumbo.JumboConnector()
    current_product_id = {}
    current_products = {}
    incompatible_products = []


    def __init__(self):
        # package is out of date, setting version manually
        self.connector.jumbo_api_version = self.jumbo_api_version


    def __str__(self):
        return f"Show me the money version: {self.jumbo_api_version}"


    def search_food(self, food):
        """Returns all food matching search term
        params:
            food: Search term [string]
        output
            API response containing search term [dict]"""
        for product in self.connector.search_products(food)["products"]["data"]:
            if product["productType"] == "Product":
                self.current_products[product["id"]] = {"title": product["title"],
                                                        "price": product["prices"]["price"]["amount"],
                                                        "unitPrice": product["prices"]["unitPrice"]["price"]["amount"],
                                                        "unit": product["prices"]["unitPrice"]["unit"]}
            else:
                self.incompatible_products.append(product["id"])
        return self.current_products


    def getDasKiloPrice(self, id):
        """Returns the kg/price in euros
        params:
            id : product ID [string]
        output:
            euro/kg [float]"""
        return self.current_products[id]["unitPrice"]


    def get_nutrition(self, id):
        try:
            return self.connector.get_product_details(id)\
                                    ['product']['data']\
                                    ['nutritionalInformation'][0]\
                                    ['nutritionalData']['entries']
        except IndexError:
            return None


    def get_products(self):
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
    j = JumboConnector()
    j.search_food("biefstuk")
    print(j.get_products())

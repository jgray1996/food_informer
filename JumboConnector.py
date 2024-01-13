from supermarktconnector import jumbo
import json

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

    def __init__(self):
        self.connector.jumbo_api_version = self.jumbo_api_version ## package is out of date
        return
    
    def __str__(self):
        return f"Show me the money version: {self.jumbo_api_version}"
    
    def getDasfood(self, food):
        return self.connector.search_products(food)
    

if __name__ == "__main__":
    j = JumboConnector()
    print(j.getDasfood("brood"))
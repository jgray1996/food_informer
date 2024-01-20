from Product import Product
import pandas as pd
import ShoppingCart
import JumboConnector

class FoodInformer:

    jumbo = JumboConnector.JumboConnector()
    cart = ShoppingCart.ShoppingCart()

    def search_food(self, product_name):

        self.jumbo.search_food(product_name)

        for id in self.jumbo.current_products:
            product = self.jumbo.current_products[id]
            self.cart.add_product(
                Product(name=product['title'],
                        stock_price=product['price'],
                        unit_price=product['unitPrice'],
                        unit=product['unit']))

    def get_products(self):
        return self.cart.get_all_products()

    def get_dataframe(self):
        columns = ["product", "stock_price",
                   "unit_price", "unit"]
        df = pd.DataFrame(columns=columns)
        for i, product in enumerate(self.get_products()):
            df.loc[i] = [product.name, product.stock_price,
                     product.unit_price, product.unit]
        return df

if __name__ == "__main__":
    informer = FoodInformer()
    informer.search_food("brood")
    print(informer.get_dataframe())

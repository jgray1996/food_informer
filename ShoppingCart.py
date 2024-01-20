class ShoppingCart:

    products = []

    def get_all_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)

    def __repr__(self):
        return f"Cart containing:{self.products}"


if __name__ == "__main__":
    print(ShoppingCart)
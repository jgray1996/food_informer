class ShoppingCart:

    products = []

    def get_all_products(self):
        return self.products

    def add_product(self, product):
        self.products.append(product)


if __name__ == "__main__":
    print(f"ShoppingCart class {ShoppingCart}")
from dataclasses import dataclass

@dataclass(kw_only=True)
class Product:
    name : str
    stock_price : int
    unit_price : int
    unit : str

    def __lt__(self, other):
        return self.unit_price < other.unit_price


if __name__ == "__main__":
    print(Product)
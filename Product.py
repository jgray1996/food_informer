from dataclasses import dataclass

@dataclass(frozen=True, kw_only=True)
class Product:
    name : str
    id : str
    img_link : str
    stock_price : int
    unit_price : float


if __name__ == "__main__":
    print(f"Product class {Product}")
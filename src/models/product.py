from dataclasses import dataclass

@dataclass
class Product:
    """Модель данных товара в системе онлайн-магазина"""
    product_id: int
    name: str
    price: float
    stock_quantity: int
    category: str

    def is_available(self) -> bool:
        return self.stock_quantity > 0

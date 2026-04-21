import unittest
from src.models.product import Product

class TestStoreLogic(unittest.TestCase):
    """Верификация функциональных требований приложения"""
    
    def setUp(self):
        self.sample_product = Product(1, "Смартфон", 50000.0, 10, "Электроника")

    def test_availability_logic(self):
        """Проверка корректности отображения наличия товара"""
        self.assertTrue(self.sample_product.is_available())
        
        self.sample_product.stock_quantity = 0
        self.assertFalse(self.sample_product.is_available())

    def test_price_validation(self):
        """Проверка соответствия стандартам обработки цен"""
        self.assertGreater(self.sample_product.price, 0)

if __name__ == '__main__':
    unittest.main()

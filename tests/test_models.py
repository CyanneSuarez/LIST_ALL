import unittest
from LIST_ALL.models import Product  # Adjust the import to your project's structure
from LIST_ALL import db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Set up a test database or any required initial state
        db.create_all()  # Ensure the database and tables are created
        self.product1 = Product(name="Test Product 1", description="This is a test product 1", price=9.99, stock=10)
        self.product2 = Product(name="Test Product 2", description="This is a test product 2", price=19.99, stock=20)
        db.session.add(self.product1)
        db.session.add(self.product2)
        db.session.commit()

    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    def test_list_all_products(self):
        # List all products from the database
        products = Product.query.all()
        self.assertEqual(len(products), 2)
        
        product_names = [product.name for product in products]
        self.assertIn("Test Product 1", product_names)
        self.assertIn("Test Product 2", product_names)

if __name__ == "__main__":
    unittest.main()

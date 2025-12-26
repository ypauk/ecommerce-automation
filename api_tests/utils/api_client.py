import requests


class ApiClient:
    BASE_URL = "https://fakestoreapi.com"

    def get_products(self, params=None):
        """
         Retrieve a list of products.

         Args:
             params (dict, optional): Query parameters, e.g., {"limit": 5}

         Returns:
             requests.Response: Response object
         """
        return requests.get(
            f"{self.BASE_URL}/products",
            params=params, timeout=10
        )

    def get_product(self, product_id):
        """
        Retrieve a product by its ID.

        Args:
            product_id (int): ID of the product

        Returns:
            requests.Response: Response object
        """
        return requests.get(
            f"{self.BASE_URL}/products/{product_id}", timeout=10
        )

    def create_product(self, payload):
        """
        Create a new product.

        Args:
            payload (dict): JSON payload with product data

        Returns:
            requests.Response: Response object
        """
        return requests.post(
            f"{self.BASE_URL}/products",
            json=payload, timeout=10
        )
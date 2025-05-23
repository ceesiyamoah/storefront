from random import randint
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_products(self):
        print('View products')
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}', name='/store/products')

    @task(4)
    def view_product(self):
        print('View product details')

        product_id = randint(1, 1000)
        self.client.get(
            f'/store/products/{product_id}', name='/store/products/:id')

    @task(1)
    def add_to_cart(self):
        print('Add to cart')

        product_id = randint(1, 10)
        self.client.post(f'/store/carts/{self.cart_id}/items/',
                         name='/store/carts/items',
                         json={'product_id': product_id, 'quantity': 1})

    @task
    def say_hello(self):
        self.client.get('/playground/hello/')

    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']

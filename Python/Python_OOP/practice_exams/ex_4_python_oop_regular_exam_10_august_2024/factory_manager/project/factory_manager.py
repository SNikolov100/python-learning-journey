from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCTS = {"Chair": Chair,
                      "HobbyHorse": HobbyHorse}

    VALID_STORE = {"FurnitureStore": FurnitureStore,
                      "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCTS.keys():
            raise Exception("Invalid product type!")
        cls = self.VALID_PRODUCTS[product_type](model, price)
        self.products.append(cls)
        return f"A product of sub-type {cls.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORE:
            raise Exception(f"{store_type} is an invalid type of store!")
        cls = self.VALID_STORE[store_type](name, location)
        self.stores.append(cls)
        return f"A new {store_type} was successfully registered."


    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [pr for pr in products if pr.sub_type.lower() in store.store_type.lower()]
        for product in filtered_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price

        if filtered_products:
            return f"Store {store.name} successfully purchased {len(filtered_products)} items."

        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store_object = next((s for s in self.stores if s.name == store_name), None)

        if store_object is None:
            raise Exception("No such store!")

        if store_object.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store_object)
        return f"Successfully unregistered store {store_name}, location: {store_object.location}."

    def discount_products(self, product_model: str):
        filtered_products = [p for p in self.products if p.model == product_model]
        for product in filtered_products:
            product.discount()
        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store_object = next((s for s in self.stores if s.name == store_name), None)

        if store_object is None:
            return "There is no store registered under this name!"

        return store_object.store_stats()

    def statistics(self):
        sorted_products = sorted(self.products, key=lambda p: p.model)
        sorted_stores = sorted(self.stores, key=lambda s: s.name)
        factory_products_count = len(self.products)
        products_sum_price = sum(pr.price for pr in self.products)

        result = [f"Factory: {self.name}",
                  f"Income: {self.income:.2f}",
                  "***Products Statistics***",
                  f"Unsold Products: {factory_products_count}. Total net price: {products_sum_price:.2f}",
                  ]

        product_dict = {}
        for product in sorted_products:
            if product.model not in product_dict:
                product_dict[product.model] = 0
            product_dict[product.model] += 1

        for product_model, count_model in product_dict.items():
            result.append(f"{product_model}: {count_model}")

        result.append(f"***Partner Stores: {len(self.stores)}***")

        for store_name in sorted_stores:
            result.append(f"{store_name.name}")

        return '\n'.join(result)

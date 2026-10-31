from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products:list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) ->Product|None:
        pr_name = next((pn for pn in self.products if pn.name == product_name), None)
        if pr_name:
            return pr_name
        return None

    def remove(self, product_name: str):
        pr_name = next((pn for pn in self.products if pn.name == product_name), None)
        if pr_name:
            self.products.remove(pr_name)

    def __repr__(self):
        result = []
        for data in self.products:
            result.append(f"{data.name}: {data.quantity}")
        return "\n".join(result)
    

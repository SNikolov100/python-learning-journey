from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    INITIAL_CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        product_summary_toy = {}

        result =[f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                 self.get_estimated_profit(),
                 "**Toys for sale:"
                 ]

        for product in self.products:
            if product.model not in product_summary_toy:
                product_summary_toy[product.model] = {"counter": 0, "total_price": 0}
            product_summary_toy[product.model]["counter"] += 1
            product_summary_toy[product.model]["total_price"] += product.price

        for model, data in sorted(product_summary_toy.items(), key=lambda x: x[0]):
            result.append(f"{model}: {data['counter']}pcs, average price: {data['total_price']/data['counter']:.2f}")

        return '\n'.join(result)


from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        product_summary_furniture = {}

        result =[f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
                 self.get_estimated_profit(),
                 "**Furniture for sale:"
                 ]

        for product in self.products:
            if product.model not in product_summary_furniture.keys():
                product_summary_furniture[product.model] = {"counter": 0, "total_price": 0}
            product_summary_furniture[product.model]["counter"] += 1
            product_summary_furniture[product.model]["total_price"] += product.price

        for model, data in sorted(product_summary_furniture.items(), key=lambda x: x[0]):
            result.append(f"{model}: {data['counter']}pcs, average price: {data['total_price']/data['counter']:.2f}")

        return '\n'.join(result)





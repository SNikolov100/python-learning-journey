from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIAL = "Wood"
    SUB_TYPE = "Furniture"
    DISCOUNT = 10
    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.MATERIAL, self.SUB_TYPE)

    def discount(self):
        self.price = self.price - (self.price * self.DISCOUNT/100)
        return self.price

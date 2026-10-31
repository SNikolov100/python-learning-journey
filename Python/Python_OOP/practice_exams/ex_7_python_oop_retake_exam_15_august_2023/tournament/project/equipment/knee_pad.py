from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    INITIAL_PROTECTION = 120
    INITIAL_PRICE = 15.0
    PERCENTAGE = 20
    
    def __init__(self):
        super().__init__(self.INITIAL_PROTECTION, self.INITIAL_PRICE)

    def increase_price(self):
        self.price += self.price * self.PERCENTAGE/100


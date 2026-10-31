from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection            #protection of the equipment
        self.price = price                      #price of the equipment

    @abstractmethod
    def increase_price(self):
        pass

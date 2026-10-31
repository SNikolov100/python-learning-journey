from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

class ComputerStoreApp:
    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ["Desktop Computer", "Laptop"]:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        else:
            computer = Laptop(manufacturer, model)
        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer_object = next((pr for pr in self.warehouse
                                if pr.processor == wanted_processor
                                and pr.price <= client_budget
                                and pr.ram >= wanted_ram), None)
        if computer_object is None:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer_object.price
        result = f"{computer_object.__repr__()} sold for {client_budget}$."
        self.warehouse.remove(computer_object)
        return result

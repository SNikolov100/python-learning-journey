from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    plant_types = {
        "Flower": Flower,
        "LeafPlant": LeafPlant
    }

    client_types = {
        "RegularClient": RegularClient,
        "BusinessClient": BusinessClient,
    }

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.plant_types:
            raise ValueError("Unknown plant type!")
        cls = self.plant_types[plant_type]
        self.plants.append(cls(plant_name, plant_price, plant_water_needed, plant_extra_data))
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.client_types:
            raise ValueError("Unknown client type!")
        ph_number_is_exist = next((p for p in self.clients if p.phone_number == client_phone_number), None)
        if ph_number_is_exist is not None:
            raise ValueError("This phone number has been used!")
        cls = self.client_types[client_type]
        self.clients.append(cls(client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client_object = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client_object is None:
            raise ValueError("Client not found!")

        plants_name_founded = [p for p in self.plants if p.name == plant_name]
        if not plants_name_founded:
            raise ValueError("Plants not found!")
        count_plants = len(plants_name_founded)
        if count_plants < plant_quantity or plant_quantity <= 0 :
            return f"Not enough plant quantity."
        plants_to_sell = plants_name_founded[:plant_quantity]
        total_price = sum(p.price for p in plants_to_sell)
        for plant in plants_to_sell:
            self.plants.remove(plant)
        order_amount = total_price * (1 - client_object.discount / 100)
        self.income += order_amount
        client_object.update_total_orders()
        client_object.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        find_plant_name = next((p for p in self.plants if p.name == plant_name), None)
        if find_plant_name is None:
            return f"No such plant name."
        self.plants.remove(find_plant_name)
        return f"Removed {find_plant_name.plant_details()}"

    def remove_clients(self):
        list_remove_clients = [c for c in self.clients if c.total_orders == 0]
        for client in list_remove_clients:
            self.clients.remove(client)
        return f"{len(list_remove_clients)} client/s removed."

    def shop_report(self):
        from collections import Counter
        count_plants = Counter(p.name for p in self.plants)
        sorted_plants = sorted(count_plants.items(), key=lambda x: (-x[1], x[0]))

        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        orders = 0
        for c in self.clients:
            orders += c.total_orders
        result = ["~Flower Shop Report~",
                  f"Income: {self.income:.2f}",
                  f"Count of orders: {orders}",
                  f"~~Unsold plants: {len(self.plants)}~~"]
        for plant, number in sorted_plants:
            result.append(f"{plant}: {number}")
        result.append(f"~~Clients number: {len(self.clients)}~~")
        for c in sorted_clients:
            result.append(c.client_details())
        return '\n'.join(result)





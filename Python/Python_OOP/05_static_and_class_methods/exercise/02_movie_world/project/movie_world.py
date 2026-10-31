from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    CUSTOMER_CAPACITY = 10
    DVD_CAPACITY = 15
    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_id_object = next((cid for cid in self.customers if cid.id == customer_id), None)
        dvd_id_object = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        if customer_id_object and dvd_id_object:
            if dvd_id_object.age_restriction > customer_id_object.age:
                return f"{customer_id_object.name} should be at least {dvd_id_object.age_restriction} to rent this movie"
            if dvd_id_object in customer_id_object.rented_dvds:
                return f"{customer_id_object.name} has already rented {dvd_id_object.name}"
            if dvd_id_object.is_rented:
                return "DVD is already rented"
            customer_id_object.rented_dvds.append(dvd_id_object)
            dvd_id_object.is_rented = True
            return f"{customer_id_object.name} has successfully rented {dvd_id_object.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if customer and dvd:
            if dvd in customer.rented_dvds:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = "\n".join(c.__repr__() for c in self.customers) + "\n"
        result += '\n'.join(d.__repr__() for d in self.dvds)
        return result







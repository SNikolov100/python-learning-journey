from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: list[User] = []     #contain all users (objects) that are created.
        self.vehicles: list[BaseVehicle] = []    #contain all vehicles (objects) that are created
        self.routes: list[Route] = []       #contain all routes (objects) that are created

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user_object = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if user_object:
            return f"{driving_license_number} has already been registered to our platform."

        cls_user = User(first_name, last_name, driving_license_number)
        self.users.append(cls_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        valid_vehicles = {"PassengerCar": PassengerCar,
                          "CargoVan": CargoVan}
        if vehicle_type not in valid_vehicles:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if any(True for v in self.vehicles if v.license_plate_number == license_plate_number ):
            return f"{license_plate_number} belongs to another vehicle."

        cls_vehicle = valid_vehicles[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(cls_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                route.is_locked = True
        route_id = 1 + len(self.routes)
        cls_route = Route(start_point, end_point, length, route_id)
        self.routes.append(cls_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user_object = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        vehicle_object = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        route_object = next((r for r in self.routes if r.route_id == route_id), None)

        if user_object.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle_object.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route_object.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle_object.drive(route_object.length)

        if is_accident_happened:
            vehicle_object.is_damaged = True
            user_object.decrease_rating()
        else:
            user_object.increase_rating()

        return (f"{vehicle_object.brand} {vehicle_object.model}"
                f" License plate: {vehicle_object.license_plate_number}"
                f" Battery: {vehicle_object.battery_level}% Status: {'Damaged' if vehicle_object.is_damaged else 'OK'}")

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        if len(sorted_damaged_vehicles) < count:
            count = len(sorted_damaged_vehicles)

        take_count_vehicles = sorted_damaged_vehicles[:count]
        for vehicle in take_count_vehicles:
            vehicle.change_status()
            vehicle.recharge()
        return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        sorted_user = sorted(self.users, key=lambda u: -u.rating)
        result = [f"*** E-Drive-Rent ***"]
        for user in sorted_user:
            result.append(str(user))

        return '\n'.join(result)










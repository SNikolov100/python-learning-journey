from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    def add_service(self, service_type: str, name: str):
        valid_serv_types = {"MainService": MainService,
                            "SecondaryService": SecondaryService}
        if service_type not in valid_serv_types:
            raise Exception("Invalid service type!")

        cls_service = valid_serv_types[service_type](name)
        self.services.append(cls_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robot_types = {"MaleRobot":MaleRobot,
                             "FemaleRobot":FemaleRobot}
        if robot_type not in valid_robot_types:
            raise Exception("Invalid robot type!")

        cls_robot = valid_robot_types[robot_type](name, kind, price)
        self.robots.append(cls_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot_obj = self.get_robot_object_from_name(robot_name)
        service_obj = self.get_service_object_from_name(service_name)

        if not isinstance(robot_obj, service_obj.allowed_robot_types):
            return "Unsuitable service."

        if service_obj.capacity <= len(service_obj.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot_obj)
        service_obj.robots.append(robot_obj)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service_object = self.get_service_object_from_name(service_name)
        robot_object = next((r for r in service_object.robots if r.name == robot_name ), None)
        if robot_object is None:
            raise Exception("No such robot in this service!")

        service_object.robots.remove(robot_object)
        self.robots.append(robot_object)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        counter_feed = 0
        filtered_all_robots_from_service = [s for s in self.services if s.name == service_name]
        for service in filtered_all_robots_from_service:
            for robot in service.robots:
                robot.eating()
                counter_feed += 1

        return f"Robots fed: {counter_feed}."

    def service_price(self, service_name: str):
        total_price = 0
        filtered_all_robots_from_service = [s for s in self.services if s.name == service_name]
        for service in filtered_all_robots_from_service:
            for robot in service.robots:
                total_price += robot.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)


    def get_service_object_from_name(self, name):
        return next((r for r in self.services if r.name == name), None)

    def get_robot_object_from_name(self, name):
        return next((r for r in self.robots if r.name == name), None)
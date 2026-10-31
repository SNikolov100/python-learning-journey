from project.services.base_service import BaseService


class SecondaryService(BaseService):
    INITIAL_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def details(self):
        result = [f"{self.name} Secondary Service:"]
        if not self.robots:
            result.append("Robots: none")
            return '\n'.join(result)
        result.append(f"Robots: {' '.join(r.name for r in self.robots)}")
        return '\n'.join(result)

    @property
    def allowed_robot_types(self):
        from project.robots.female_robot import FemaleRobot
        return FemaleRobot
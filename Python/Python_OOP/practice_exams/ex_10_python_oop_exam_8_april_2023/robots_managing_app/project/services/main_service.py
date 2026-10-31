
from project.services.base_service import BaseService


class MainService(BaseService):
    INITIAL_CAPACITY = 30
    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def details(self):
        result = [f"{self.name} Main Service:"]
        if not self.robots:
            result.append("Robots: none")
            return '\n'.join(result)
        result.append(f"Robots: {' '.join(r.name for r in self.robots)}")
        return '\n'.join(result)

    @property
    def allowed_robot_types(self):
        from project.robots.male_robot import MaleRobot
        return MaleRobot
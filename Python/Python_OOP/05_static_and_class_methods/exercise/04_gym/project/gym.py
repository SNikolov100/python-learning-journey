from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    @staticmethod
    def __add_object_if_not_exist(obj, collection: list):
        if obj not in  collection:
            collection.append(obj)

    def add_customer(self, customer: Customer):
        self.__add_object_if_not_exist(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_object_if_not_exist(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_object_if_not_exist(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_object_if_not_exist(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_object_if_not_exist(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription_obj = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer_obj = next((c for c in self.customers if c.id == subscription_obj.customer_id), None)
        trainer_obj = next((t for t in self.trainers if t.id == subscription_obj.trainer_id), None)
        plan_obj = next((p for p in self.plans if p.id == subscription_obj.exercise_id), None)
        equipment_obj = next((e for e in self.equipment if e.id == plan_obj.equipment_id), None)
        return "\n".join([subscription_obj.__repr__(),
                          customer_obj.__repr__(),
                          trainer_obj.__repr__(),
                          equipment_obj.__repr__(),
                          plan_obj.__repr__()
                          ])




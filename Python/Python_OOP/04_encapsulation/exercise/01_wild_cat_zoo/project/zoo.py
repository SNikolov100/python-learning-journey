from project.animal import Animal
from project.lion import Lion
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        name_worker = next((wn for wn in self.workers if wn.name == worker_name), None)
        if name_worker:
            self.workers.remove(name_worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_workers = sum(w.salary for w in self.workers)
        if self.__budget >= salary_workers:
            self.__budget -= salary_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_tend_animals = sum(mfc.money_for_care for mfc in self.animals)
        if money_for_tend_animals <= self.__budget:
            self.__budget -= money_for_tend_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animal_dict = {"Lion":[],
                       "Tiger": [],
                       "Cheetah": []}
        for animal in self.animals:
            animal_dict[animal.__class__.__name__].append(repr(animal))
        result = [f"You have {len(self.animals)} animals"]
        for animal, data in animal_dict.items():
            result.append(f"----- {len(data)} {animal}s:")
            result.extend(data)
        return "\n".join(result)

    def workers_status(self):
        worker_dict = {"Keeper":[],
                       "Caretaker": [],
                       "Vet": []}
        for worker in self.workers:
            worker_dict[worker.__class__.__name__].append(repr(worker))
        result = [f"You have {len(self.workers)} workers"]
        for worker, data in worker_dict.items():
            result.append(f"----- {len(data)} {worker}s:")
            result.extend(data)
        return "\n".join(result)


from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Dog(Animal):
    def make_sound(self):
        return "woof-woof"

class Mouse(Animal):
    def make_sound(self):
        return "chterrrr"

def animal_sound(animals:list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Mouse()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
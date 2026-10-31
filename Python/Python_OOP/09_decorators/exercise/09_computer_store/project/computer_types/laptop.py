from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def available_processor(self) -> dict[str, int]:
        processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }
        return processors

    @property
    def available_ram(self) ->int:
        return 64

    def __str__(self):
        return "laptop"
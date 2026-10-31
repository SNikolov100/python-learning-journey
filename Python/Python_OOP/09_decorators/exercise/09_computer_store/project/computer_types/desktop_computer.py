from project.computer_types.computer import Computer


class DesktopComputer(Computer):


    @property
    def available_processor(self) -> dict[str, int]:
        processors = {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800,
        }
        return processors

    @property
    def available_ram(self) ->int:
        return 128

    def __str__(self):
        return "desktop computer"


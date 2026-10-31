from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons : list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        # for data in self.pokemons:
        #     if pokemon_name == data.name:
        #         self.pokemons.remove(data)
        #         return f"You have released {pokemon_name}"
        release_pokemon = next((data for data in self.pokemons if pokemon_name == data.name), None)
        if release_pokemon:
            self.pokemons.remove(release_pokemon)
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self) -> str:
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for data in self.pokemons:
            result.append(f"- {data.pokemon_details()}")
        return '\n'.join(result)


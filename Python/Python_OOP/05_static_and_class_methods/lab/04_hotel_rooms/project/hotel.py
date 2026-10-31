from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room_obj = next((r for r in self.rooms if r.number == room_number), None)
        if room_obj:
            return room_obj.take_room(people)
        return None

    def free_room(self, room_number: int):
        room_obj = next((r for r in self.rooms if r.number == room_number), None)
        if room_obj:
            return room_obj.free_room()
        return None

    def status(self):
        guests = sum(q.guests for q in self.rooms)
        result = list([f"Hotel {self.name} has {guests} total guests"])
        result.append(f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}")
        result.append(f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")
        return '\n'.join(result)




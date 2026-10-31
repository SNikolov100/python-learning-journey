
def accommodate(*args, **kwargs):
    rooms_dict = {}
    result = []
    accommodate_rooms = {}
    no_accommodation = 0
    for rooms, capacity in kwargs.items():
        room, number = rooms.split("_")
        if number not in rooms_dict:
            rooms_dict[number] = 0
        rooms_dict[number] = capacity
    sorted_rooms = sorted(rooms_dict.items(), key=lambda x: (x[1], x[0]))
    for group in args:
        accommodation = False
        for room, capacity in sorted_rooms:
            if group <= capacity:
                accommodate_rooms[room] = group
                sorted_rooms.remove((room, capacity))
                accommodation = True
                break
        if not accommodation:
            no_accommodation += group

    sorted_accommodate_rooms = sorted(accommodate_rooms.items(), key=lambda x: x[0])
    if accommodate_rooms:
        result.append(f"A total of {len(accommodate_rooms)} accommodations were completed!")
        for room_number, quest in sorted_accommodate_rooms:
            result.append(f"<Room {room_number} accommodates {quest} guests>")
    else:
        result.append(f"No accommodations were completed!")


    if no_accommodation > 0:
        result.append(f"Guests with no accommodation: {no_accommodation}")

    if sorted_rooms:
        result.append(f"Empty rooms: {len(sorted_rooms)}")


    return '\n'.join(result)







print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))


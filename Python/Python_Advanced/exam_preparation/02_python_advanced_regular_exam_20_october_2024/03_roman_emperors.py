def list_roman_emperors(*args, **kwargs):
    false_emperors = {}
    successful_emperors = {}
    result = []

    for name, status in args:
        if status:
            if name in kwargs:
                successful_emperors[name] = kwargs[name]
        else:
            if name in kwargs:
                false_emperors[name] = kwargs[name]
    sorted_success = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0])) if successful_emperors else ""
    sorted_false = sorted(false_emperors.items(), key=lambda x: (x[1], x[0])) if false_emperors else ""
    result.append(f"Total number of emperors: {len(sorted_success) + len(sorted_false)}")

    if sorted_success:
        result.append(f"Successful emperors:")
        for data in sorted_success:
            result.append(f"****{data[0]}: {data[1]}")

    if sorted_false:
        result.append(f"Unsuccessful emperors:")
        for data in sorted_false:
            result.append(f"****{data[0]}: {data[1]}")

    return '\n'.join(data for data in result)


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print("===================================")
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print("======================================")
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
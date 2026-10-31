def concatenate(*args, **kwargs):
    result_string = ""
    for ch in args:
        result_string += ch
    for key, value in kwargs.items():
        if key in result_string:
            result_string = result_string.replace(key, value)
    return result_string







print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print("-------------------")
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
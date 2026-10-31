def forecast(*args):
    result = []
    weather_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }
    for location, weather in args:
        weather_dict[weather].append(location)
    for weather, location in weather_dict.items():
        sorted_location = sorted(location)
        for loc in sorted_location:
            result.append(f"{loc} - {weather}")
    return "\n".join(result)



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

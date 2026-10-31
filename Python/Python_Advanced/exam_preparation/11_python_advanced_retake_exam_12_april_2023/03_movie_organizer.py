def movie_organizer(*args):
    movie_dict = {}
    result = []
    for movie_name, genre in args:
        if genre not in movie_dict:
            movie_dict[genre] = []
        movie_dict[genre].append(movie_name)
    sorted_movie = tuple(sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for genre, movie_names in sorted_movie:
        result.append(f"{genre} - {len(movie_names)}")
        for movie in sorted(movie_names):
            result.append(f"* {movie}")
    return "\n".join(result)



print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

from sys import maxsize
number_movies = int(input())
max_rating = 0
min_rating = maxsize
max_name_rating = ""
min_name_rating = ""
sum_rating = 0

for _ in range(number_movies):
    name_movie = input()
    rating_movie = float(input())
    sum_rating += rating_movie
    if max_rating < rating_movie:
        max_rating = rating_movie
        max_name_rating = name_movie
    if min_rating > rating_movie:
        min_rating = rating_movie
        min_name_rating = name_movie

average_rating = sum_rating / number_movies

print(f"{max_name_rating} is with highest rating: {max_rating}")
print(f"{min_name_rating} is with lowest rating: {min_rating}")
print(f"Average rating: {average_rating:.1f}")




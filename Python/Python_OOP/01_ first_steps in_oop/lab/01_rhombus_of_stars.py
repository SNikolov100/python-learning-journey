def print_up_stars(n):
    for row in range(1, n):
        print_stars_in_row(n, row)

def print_down_stars(n):
    for row in range(n, 0, -1):
        print_stars_in_row(n, row)

def print_stars_in_row(n, row):
    print(" " * (n - row) + "* " * row)

numb = int(input())

print_up_stars(numb)
print_down_stars(numb)
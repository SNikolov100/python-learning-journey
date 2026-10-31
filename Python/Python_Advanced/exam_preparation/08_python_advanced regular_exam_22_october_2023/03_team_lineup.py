def team_lineup(*args):
    book_players = {}
    result =[]
    for player_name, county_name in args:
        if county_name not in book_players:
            book_players[county_name] = []
        book_players[county_name].append(player_name)

    sorted_book_players = sorted(book_players.items(), key=lambda x: (-len(x[1]), x[0]))
    for county_name, players in sorted_book_players:
        result.append(f"{county_name}:")
        for player in players:
            result.append(f"  -{player}")
    return '\n'.join(result)



print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


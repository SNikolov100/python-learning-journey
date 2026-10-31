def draw_cards(*args, **kwargs):
    type_card = {}
    monster = []
    spell = []
    for name_of_the_card, type_c in args:
        if type_c not in type_card:
            type_card[type_c] = []
        type_card[type_c].append(name_of_the_card)

    for name, type_c in kwargs.items():
        if type_c not in type_card:
            type_card[type_c] = []
        type_card[type_c].append(name)

    for type_c, name in type_card.items():
        if type_c == "monster":
            monster.append(name)
        else:
            spell.append(name)
    result = []
    if monster:
        sorted_monster = sorted(*monster, reverse=True)
        result.append("Monster cards:")
        for monster in sorted_monster:
            result.append(f"  ***{monster}")
    if spell:
        sorted_spell = sorted(*spell)
        result.append("Spell cards:")
        for spell in sorted_spell:
            result.append(f"  $$${spell}")
    return "\n".join(result)



print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))

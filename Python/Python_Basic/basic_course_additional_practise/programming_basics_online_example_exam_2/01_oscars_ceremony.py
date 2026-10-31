STATUETTE = 0.3
CATERING = 0.15
MUSIC = 0.5

rend_hall = float(input())

price_statuette = rend_hall * (1 - STATUETTE)
price_catering = price_statuette * (1 - CATERING)
price_music = price_catering * (1 - MUSIC)

full_amount = rend_hall + price_statuette + price_catering + price_music

print(f"{full_amount:.2f}")

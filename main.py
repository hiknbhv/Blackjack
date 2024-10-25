import random

card1 = random.randint(2, 11)
card2 = random.randint(2, 11)
card = random.randint(2, 11)
print("your first card is",card1)
print("your second card is", card2)

print(" ")

card_sum = card2+card1
game_over = card_sum > 21
input("draw another card?")

if game_over:
    print("YOU BUSTED")
else:
    print("You got a",card)
card_sum=card1+card2+card
game_over = card_sum > 21
if game_over:
    print("YOU BUSTED")
else:
    print("YOU WIN")
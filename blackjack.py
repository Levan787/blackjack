import random
# Returns a random card from the deck
def deal_card():
    cards = [2,3,4,5,6,7,8,9,11,10,10,10,10]
    card = random.choice(cards)
    return card

#function calculate_score() that takes list of cards as input
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

# check 11(ace)
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# compare user and computer scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "you loose, oppontent has blackjack"
    elif user_score == 0:
        return "you win, you have a blackjack"
    elif user_score > 21:
        return "you went over. you loose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else: 
        return "you loose"

# Deal the user and computer 2 cards each using deal_card()
user_cards = []
computer_cards=[]
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

#take another card hit, or stand

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" your cards: {user_cards}, current_score: {user_score}")
    print(f" computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:

        user_should_deal =  input("Type 'y' to get another card, type 'n' to pass:")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

#computer move

while computer_score != 0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f" your final hand: {user_cards} final score: {user_score}")
print(f" computer's final card: {computer_cards}, final_score: {computer_score}")
print(compare(user_score, computer_score))




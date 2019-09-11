from deck_of_cards import Deck
import pandas as pd

print("Let's play a game.")
print("I have a standard deck of cards. You can draw as many cards as you like and I will add up all the numbers.")
print("After you draw your cards, I will draw the same number of cards and add up all my numbers.")
print("Whoever has the highest total sum, wins!")
print("Type 'q' at any time to quit the game.\n")

while True:
    starting_deck = Deck.copy()
    number_of_cards = int(input('How many cards would you like to draw?'))

    if number_of_cards == 'q':
        break
    user_cards = starting_deck.sample(number_of_cards, replace=True)
    print("You drew:\n")

    for card in range(0, number_of_cards):
        print("The " + str(user_cards['Face'].values[card]) + " of " + str(user_cards['Suits'].values[card]))
    user_sum = user_cards['Rank'].sum()
    print('Your cards sum up to a total of ' + str(user_sum) + '.\n')
    print('My turn to draw.')
    remaining_cards = pd.merge(starting_deck, user_cards, how='outer')
    dealer_cards = remaining_cards.sample(number_of_cards, replace=True)
    print('I drew:')
    for card in range(0, number_of_cards):
        print("The " + str(dealer_cards['Face'].values[card]) + " of " + str(dealer_cards['Suits'].values[card]))
    dealer_sum = dealer_cards['Rank'].sum()
    print('My cards sum up to a total of ' + str(dealer_sum) + '.\n')
    if user_sum > dealer_sum:
        print('You win!')
    elif user_sum < dealer_sum:
        print('I win!')
    elif user_sum == dealer_sum:
        print("It's a tie!")

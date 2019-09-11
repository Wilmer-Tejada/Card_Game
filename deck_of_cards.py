import pandas as pd


# Creates empty lists for the values for the Deck dataframe.
Suits = []
Rank = []
Colors = []

# Loops through all the suits one by one and then loops for values 2 to 14.
for suit in ["Hearts", "Spades","Clubs","Diamonds"]:
    for i in range(2,15):
        Suits.append(suit)
        Rank.append(i)

        if suit in ["Hearts", "Diamonds"]:
            Colors.append('Red')
        else:
            Colors.append('Black')

# Creates a Deck dataframe based on the previously created lists.
Deck = pd.DataFrame(
    {'Suits':Suits,
     'Rank':Rank,
     'Colors':Colors
    })

# Creates a new column Face, which stores the actual face of the card.
Deck['Face'] = Deck['Rank']
Deck.loc[Deck['Rank'] == 11,'Face'] = 'Jack'
Deck.loc[Deck['Rank'] == 12,'Face'] = 'Queen'
Deck.loc[Deck['Rank'] == 13,'Face'] = 'King'
Deck.loc[Deck['Rank'] == 14,'Face'] = 'Ace'

del Suits,Rank, Colors, suit, i


#
#
# 
#
#

from deckOfCards import *

dc = deckOfCards()
dc.shuffle()

def getcards(cards):                                                # The following method obtains indices for cards 1, 2 and 3
    for i in range(0,len(dc.list)):
        if(cards == dc.list[i]):
            return i


def searchCards():                                                  # Get the card from method deckOfCards.deal (return the top card)
    card1 = dc.deal()
    indexOfCard1 = getcards(card1)                                  # Take the index of card 1
    #print("A=",indexOfCard1)
    lowAce1 = (indexOfCard1 % 13)+1                                 # Apply modulus to get the low Ace value.  
    #print ("lowAce1=", lowAce1)

    print("Card 1:", card1)

    card2 = dc.deal()                                               # Get the card from method deckOfCards.deal (return the top card)
    indexOfCard2 = getcards(card2)                                  # Take the index of card 2
    lowAce2 = (indexOfCard2 % 13)+1                                 # Apply modulus to get the low Ace value.

    print("card 2:", card2)

    if (lowAce1 == lowAce2):                                        # Consider it a "TIE" if lowAce1 == lowAce2
        print("TIE")
        searchCards()                                               # Again get the cards from the deck
    else:
        amt = int(input("Please enter an amount:"))                 # If there is a tie, no bet will be placed and that round is skipped. Enter bet to continue                       
        card3 = dc.deal()                                           # take the 3rd card from the deck
        indexOfCard3 = getcards(card3)                              # Take the index of 3rd card
        lowAce3 = (indexOfCard3 % 13)+1                             # Apply modulus to get the low Ace value.

        print("card 3:", card3)

        if (lowAce1 < lowAce2):                                     # To check if the card is in between card 1 and 2. Based on the if-else conditions, player either wins or loses.
            if ((lowAce3 > lowAce1) and (lowAce3 < lowAce2)):
                print("Player wins!!", "Amount:", amt)
            else:
                print("Player loses.", "Amount:", amt)
        elif (lowAce1 > lowAce2):
            if ((lowAce3 < lowAce1) and (lowAce3 > lowAce2)):
                print("Player wins!!", "Amount:", amt)
            else:
                print("Player loses.", "Amount:", amt)
        else:
            print("Player loses.", "Amount:", amt)

searchCards()
#print(len(deckOfCards.fan()))

while (len(dc.fan()) > 2):                                      # The game loops on until the number of cards is less than 3. 
    searchCards()

print("Game Over")                                              # Game over :) 







        

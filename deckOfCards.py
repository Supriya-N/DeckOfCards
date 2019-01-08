#
#
# Create a class that represents a deck of playing cards.  The data for this object will be the cards themselves. The methods this class will have are the following
# deal - a method that returns the value of the card on top of the deck.  Once a card is dealt it cannot be dealt again until the deck is shuffled.
# shuffle - a method that returns to the deck all dealt cards (for a total of 52, no Jokers) and places it in a random order.
# fan - fan is a method that will simply list the cards in the deck from the top card to the card on the bottom of the deck.
# isOrdered - a method that returns True if the deck is in order and False if it is not.  If an ordered deck has a few cards dealt off of the top it is still in order. You do not need a full deck to be in order.
# Order - a method that sorts the deck or puts the cards in order with the 2 of clubs beings lowest and the ace of spades being highest (while there is no real ranking of suits we’ll go with the standard poker/bridge ranking of clubs(lowest), diamonds, hearts, spades(highest).
# We will also count the Ace as a high card and not a low card. The Ace of a particular suit should be the highest card when a suit is sorted (2 thru A).
#

import random                                                                                       # Import a module called random 

class deckOfCards():                                                                                # Creating a class called deckOfCards

    deck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D',  # Creating a new deck of cards
            '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2H', '3H', '4H', '5H',
            '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S',
            '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']

    list = deck[:]                                              # To sort the original deck 

    def order(self):                                            # A method that returns original deck 
        return self.deck

    def deal(self):                                             # A method to return the value of the card on top of the deck
        cardDeal = self.deck.pop()
        return cardDeal
    
    def shuffle(self):                                          # A method that returns all dealt cards to deck and places it in a random order.
        random.shuffle(self.deck)                               # Random function is used to achieve shuffling
        return self.deck

    def fan(self):                                              # A method to list the cards in the deck from the top card to the bottom card of the deck.
        return self.deck

    def isOrdered(self):                                        # A method that returns True if the deck is in order and False if it is not.
        c = 0                                                   
        for i in range(0, len(self.deck)):                      # Taking the range from 0 to 52(len of deck)
            if (self.list[i] == self.deck[i]):                  # if current deck == original deck, then the condition is passed.
                pass
            else:
                c = c + 1                                       

        if (c > 0):                                             # if counter > 0, then there is atleast a single card in current deck which does not match with original deck
            return False                                        # Then, return False.
        else:
            return True                                         # Else return True.



        

import random
from card import Card

class Deck:
    def __init__(self):
        # Initialize an empty deck
        self.cards = []

    def shuffle(self):
        # Initialize the shoe with 52 cards
        self.cards = [Card(suit, rank) for suit in ['hearts', 'diamonds', 'clubs', 'spades'] for rank in range(2, 15)]


    def deal_card(self):
        # Deal one random card from the deck
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def __str__(self):
        # Return a string representation of the deck
        return ', '.join(str(card) for card in self.cards)
    
# Example usage:
if __name__ == "__main__":
    # Create an empty deck
    deck = Deck()
    # check size of deck - should be zero
    print(len(deck.cards))
    #shuffle the deck - size should be 52
    deck.shuffle()
    print(len(deck.cards))
    # display the full deck
    print(deck)
    print("")
    # Deal and print a few cards
    for _ in range(5):
        dealt_card = deck.deal_card()
        print(f"Dealt card: {dealt_card}")

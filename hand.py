from abc import ABC, abstractmethod

class Hand(ABC):
    def __init__(self):
        # Initialize an empty hand
        self.cards = []

    def clear_hand(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def card_count(self):
        return len(self.cards)

    def __str__(self):
        # Return a string representation of the hand
        return ', '.join(str(card) for card in self.cards)

    @abstractmethod
    def value_of_hand(self):
        pass

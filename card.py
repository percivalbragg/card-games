class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.show_rank = True

    def __str__(self):
        # Map numerical ranks to corresponding names for face cards
        rank_names = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

        # Get the rank name or use the numerical rank
        rank_str = rank_names.get(self.rank, str(self.rank))

        if self.show_rank:
            return f"{rank_str}_of_{self.suit}"
        else:
            return "card_back"

    def get_image_name(self):
        return f"{str(self.rank)}_of_{self.suit}"

    def is_ace(self):
        if self.rank == 14: # Ace
            return True
        return False

    def get_rank(self):
        return self.rank
    
# Example usage:
if __name__ == "__main__":
    # Create instances of the Card class
    card1 = Card('hearts', 10)
    card2 = Card('spades', 14)

    # Print the card representations
    print(card1)  # Output: "10_of_Hearts"
    print(card2)  # Output: "Ace_of_Spades"

    print(card1.get_image_name())
    print(card2.get_image_name())

    print(card1.is_Ace())   # Output: "False"
    print(card2.is_Ace())   # Output: "True"

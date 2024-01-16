'''
Deck module that defines the Deck class.
'''
import random
class Deck:
    def __init__(self):
        self.cards = self.create_deck()
    def create_deck(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = []
        for suit in suits:
            deck.extend(f"{rank} of {suit}" for rank in ranks)
        return deck
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]
from card import Card, suits, ranks
from random import shuffle


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        cards = ''
        for card in self.all_cards:
            cards += f'{card.rank} of {card.suit}\n'

        return cards

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

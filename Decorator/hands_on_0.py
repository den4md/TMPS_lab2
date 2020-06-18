from Decorator.icard import ICard
from Decorator.number_card import NumberCard
from Decorator.special_card import SpecialCard


class HandsOn0(SpecialCard):

    def __init__(self, color: str):
        super(HandsOn0, self).__init__(color)
        self._card = NumberCard(0, color)

    def action(self):
        print("ALL PLAYERS NEED TO PUT THEIR HANDS ON THE CARD")
        self.super_action()

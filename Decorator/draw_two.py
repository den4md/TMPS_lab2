from Decorator.icard import ICard
from Decorator.skip import Skip
from Decorator.special_card import SpecialCard


class DrawTwo(SpecialCard):

    def __init__(self, color: str, card: ICard = None):
        super(DrawTwo, self).__init__(color)
        self._card = Skip(color, card)

    def action(self):
        print("Next player should take two cards")
        self.super_action()

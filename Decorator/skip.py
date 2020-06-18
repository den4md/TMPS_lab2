from Decorator.icard import ICard
from Decorator.special_card import SpecialCard


class Skip(SpecialCard):

    def __init__(self, color: str, card: ICard = None):
        super(Skip, self).__init__(color)
        self._card = card

    def action(self):
        print("Next player should skip his move")
        self.super_action()

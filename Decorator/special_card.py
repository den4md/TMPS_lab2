from Decorator.icard import ICard


class SpecialCard(ICard):

    def __init__(self, color: str):
        super(SpecialCard, self).__init__(color)
        self._card = None

    def action(self):
        pass

    def super_action(self):
        if isinstance(self, SpecialCard) and self._card is not None:
            self._card.action()

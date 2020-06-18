from Decorator.icard import ICard


class NumberCard(ICard):

    def __init__(self, number: int, color: str):
        super(NumberCard, self).__init__(color)
        self.number = number

    def action(self):
        print(f"Top card is {self.number} of {self.color}")

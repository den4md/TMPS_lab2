from Decorator.draw_two import DrawTwo
from Decorator.hands_on_0 import HandsOn0
from Decorator.number_card import NumberCard

if __name__ == '__main__':
    predefined_board = [
        NumberCard(7, "green"),
        NumberCard(7, "red"),
        HandsOn0("red"),
        DrawTwo(color="red")
    ]

    for card in predefined_board:
        card.action()

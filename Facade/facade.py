from Facade.internal_logic import InternalLogic


class Facade:

    @staticmethod
    def method_a():
        print("Facade a")
        InternalLogic.help_a()
        InternalLogic.logic_a()

    @staticmethod
    def method_b():
        print("Facade b")
        InternalLogic.help_c()
        InternalLogic.logic_c()
        InternalLogic.logic_b()

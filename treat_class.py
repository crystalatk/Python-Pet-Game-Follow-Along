class Treat:
    def __init__(self, fullness_imp, happiness_imp):
        self.fullness_imp = fullness_imp
        self.happiness_imp = happiness_imp

class ColdPizza(Treat):
    def __init__(self):
        super().__init__(15, 20)

class Bacon(Treat):
    def __init__(self):
        super().__init__(30, 30)

class VeganSnack(Treat):
    def __init__(self):
        super().__init__(2, 1)
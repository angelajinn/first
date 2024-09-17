class Ingredient:
    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type

    def __str__(self):
        return f"{self.name}: {self.amount} ({self.type})"

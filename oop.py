class NFL():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def speak(self):
        print("Player is", self.name, "Position is",  self.position)


print("The NFL team")
joe = NFL("Joe Montana", "QB")
joe.speak()

barry = NFL("Barry Sanders", "RB")
barry.speak()

jerry = NFL("Jerry Rice", "WR")
jerry.speak()

graham = NFL("Graham Gano", "K")
graham.speak()



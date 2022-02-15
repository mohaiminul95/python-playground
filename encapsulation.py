class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'My name is {self.name} and my age is {self.age}')

player1 = PlayerCharacter('Rabid', 28)

print(player1.speak())

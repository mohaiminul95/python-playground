class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        print(f'My name is {self._name} and my age is {self._age}')

player1 = PlayerCharacter('Rabid', 28)
player1.speak = "BOOOM!!"

print(player1.speak())

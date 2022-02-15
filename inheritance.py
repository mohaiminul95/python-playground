class User:
    def signin(self):
        print('Logged In')

class Wizard(User):
    def signin(self):
        pass

class Archer(User):
    def signin(self):
        pass

wizard1 = Wizard()
print(wizard1.signin())
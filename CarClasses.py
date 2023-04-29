class v1:       #Покоління автомобілів
    speed = 140
    weight = 1467
    hp = 28
    age = 95
    def __str__(self):
        print("Перше покоління:")
        print(self.speed)
        print(self.weight)
        print(self.hp)
        print(self.age)
        print()
        print()

class v2(v1):
    weight = 1250
    hp = 31
    age = 60
    def __str__(self):
        print("Друге покоління:")
        print(self.speed)
        print(self.weight)
        print(self.hp)
        print(self.age)
        print()
        print()

class v3(v2):
    speed = 180
    weight = 1301
    hp = 87
    age = 45
    def __str__(self):
        print("Третє покоління:")
        print(self.speed)
        print(self.weight)
        print(self.hp)
        print(self.age)
        print()
        print()

class v4(v3):
    weight = 1247
    age = 25
    def __str__(self):
        print("Четверте покоління:")
        print(self.speed)
        print(self.weight)
        print(self.hp)
        print(self.age)
        print()
        print()

rarity = v1()
old = v2()
classic = v3()
new = v4()

print()
rarity.__str__()
old.__str__()
classic.__str__()
new.__str__()
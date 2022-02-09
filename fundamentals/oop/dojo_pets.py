class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet
        self.treast = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()


class Pet:
    def __init__(self, name, typeof, tricks, health, energy):
        self.name = name
        self.typeof = typeof
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health +=5
    def noise(self):
        print(self.tricks)

dog = Pet('dog', 'pitbull','Bark',50,50)
donovan = Ninja('donovan','lemmerman', dog ,'bacon','dog food')
donovan.feed()
donovan.walk()
donovan.bathe()
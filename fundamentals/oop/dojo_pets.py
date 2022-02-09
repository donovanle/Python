class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
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
        print("Pets Energy Increased by 25 while sleeping!")
        print(f"Total Energy = {self.energy}")
    def eat(self):
        self.energy += 5
        self.health += 10
        print("Pets Energy Increased by 5 and Health increased by 10 while eating!")
        print(f"Total Health = {self.health} Total Energy = {self.energy}")
    def play(self):
        self.health +=5
        print("Pets health increased by 5 while walking!")
        print(f"Total Health = {self.health}")
    def noise(self):
        print(self.tricks)

dog = Pet('dog', 'pitbull','Bark',50,50)
donovan = Ninja('donovan','lemmerman', dog ,'bacon','dog food')
donovan.feed()
donovan.walk()
donovan.bathe()
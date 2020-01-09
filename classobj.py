class Enemy:
    life = 6

    def attack(self):
        print(" Ouch!")
        self.life -= 1

    def blessings(self):
        print(" I am blessed by this")
        self.life += 1

    def checklife(self):
        if self.life <= 0:
            print(" It is finished, no more life")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

enemy1.attack()
enemy1.checklife()

enemy1.attack()
enemy1.checklife()

enemy1.attack()
enemy1.checklife()

enemy1.attack()
enemy1.checklife()

enemy1.attack()
enemy1.checklife()

enemy1.attack()
enemy1.blessings()
enemy1.checklife()






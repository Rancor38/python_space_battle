import random

class Ship:
    def __init__(self, name, hull, firepower, accuracy):
        self.name = name
        self.hull = hull
        self.firepower = firepower
        self.accuracy = accuracy

    def __str__(self):
        return f'Ship ({self.name}) hull {self.name} firepower {self.firepower} accuracy {self.accuracy}'

class Player(Ship):
    def __init__(self, name, hull, firepower, accuracy, continu=True, score=0):
        Ship.__init__(self, name, hull, firepower, accuracy)
        
        self.continu = continu
        self.score = score
    
    def checkContinu(self):
        response = input("Would you like to continue? y/n \n")
        if response.lower() in ['y', 'yes']:
            #keep going
            pass
        else:
            #stop
            self.continu = False
class Alien(Ship):
    def __init__(self, name, hull=random.randint(3,6), firepower=random.randint(2,4), accuracy=random.uniform(.6, .8)):
        Ship.__init__(self, name, hull, firepower, accuracy)
    

player = Player("Assembly", 20, 5, .7)
alien1 =Alien("Gloob Glop")
alien2 =Alien("Flump Flurp")
alien3 =Alien("Blorg Blip")
alien4 =Alien("Vex Vexx")
alien5 =Alien("Zorg Zazz")
alien6 =Alien("Snix Snax")

aliens=[alien1, alien2, alien3, alien4, alien5, alien6]

while player.continu:
    #play the game
    print("You are the USS Assembly, you are floating through space when an alien vessel attacks!")
    round = 0
    while (len(aliens) > round and player.continu):
        print(f'Alien vessel of {aliens[round].name} has appeared!')
        print(f'Firing upon alien vessel')
        while (aliens[round].hull > 1) or (player.hull > 1):
            print('Fire in the hole!')
            if random.uniform(0, 1) > player.accuracy:
                print('We missed!')
            else: 
                print('We hit!')
                aliens[round].hull -= player.firepower
                if aliens[round].hull < 1:
                    print("They were destroyed!")
                    break
            print("They're firing back!")
            if random.uniform(0,1) > aliens[round].accuracy:
                print("They missed!")
            else:
                print("They hit!")
                player.hull -= aliens[round].firepower
                if player.hull < 1:
                    print("Your ship was destroyed")
                    player.continu = False
                    break

            
                
    #check if it's over
        round +=1
        print(f'Your current hull: {player.hull}')

        if round == 6:
            print("You win!")
            break
        if player.hull > 0:
            player.checkContinu()
        else:
            print("game over")
    #end the game    
    player.continu=False
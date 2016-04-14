## Importing modules
import sys
import random
import os
import math

## Setting up classes and subclasses
class Character(object):
    def __init__(self, name, classification, 
                    maxHealth, curHealth, 
                    maxMana, curMana, 
                    weapon, armor, 
                    alive):
        self.name = name
        self.classification = classification
        self.maxHealth = maxHealth
        self.maxMana = maxMana
        self.curHealth = curHealth
        self.curMana = curMana
        self.weapon = weapon
        self.armor = armor
        self.alive = alive
    
    def getName(self):
        return self.name
        
    def getClass(self):
        return self.classification
        
    def getMaxHealth(self):
        return self.maxHealth
        
    def setMaxHealth(self, x):
        self.maxHealth = x
        
    def getCurHealth(self):
        return self.curHealth
        
    def setCurHealth(self, x):
        self.curHealth = x
        
    def getMaxMana(self):
        return self.maxMana
        
    def setMaxMana(self, x):
        self.maxMana = x
        
    def getCurMana(self):
        return self.curMana
        
    def setCurMana(self, x):
        self.curMana = x
        
    def getWeapon(self):
        return self.weapon
        
    def setWeapon(self, x):
        self.weapon = x
        
    def getArmor(self):
        return self.armor
        
    def setArmor(self, x):
        self.armor = x
    
    def getAlive(self):
        return self.alive
    
    def setAlive(self, x):
        self.alive = x

    def getNameAndHealth(self):
        return "%s %s/%s" % (self.name, self.curHealth, self.maxHealth)
            
    def __str__(self):
        return "%s is a %s" % (self.name, self.classification)
        
class Weapon(object):
    def __init__(self, name, atk, special): 
        self.name = name
        self.atk = atk
        self.special = special
    
    def getAtk(self):
        return self.atk
        
    def getSpecial(self):
        return self.special
        
    def __str__(self):
        return self.name
        
class Armor(object):
    def __init__(self, name, dfs, special): 
        self.name = name
        self.dfs = dfs
        self.special = special
        
    def getDfs(self):
        return self.dfs
        
    def getSpecial(self):
        return self.special
    
    def __str__(self):
        return self.name
        
    
def printStats(stats):
    print ('Name: %s' % stats[0])
    print ('Class: %s' % stats[1])
    print ('Health: %s / %s' % (stats[2], stats[3]))
    print ('Mana: %s / %s' % (stats[4], stats[5]))
    print ('Weapon: %s +%s Atk ' % (stats[6],stats[6].getAtk()))
    print ('Armor: %s +%s Dfs' % (stats[7],stats[7].getDfs())) 

def getStats(character): 
    stats = [character.getName(), character.getClass(), 
    character.getMaxHealth(), character.getCurHealth(), 
    character.getMaxMana(), character.getCurMana(), 
    character.getWeapon(),character.getArmor()]
    return stats
    
def printEnemies(enemies):
        number = 1
        for x in enemies:
            print('(%s.) %s ' % (number, x.getNameAndHealth()))
            if x.getAlive():
                print ('Alive')
            else: print('Dead')
            number = number+1
            
        
def doDamage(attacker, attacked):
        if attacker.getAlive():
            print ('%s attacked %s for %s damage' 
		% (attacker.getName(), attacked.getName(), attacker.getWeapon().getAtk()))
            attacked.setCurHealth(attacked.getCurHealth() - attacker.getWeapon().getAtk())
            if attacked.getCurHealth() <= 0:
                attacked.setAlive(False)
        else: return
        
def checkForDead(enemies):
    number = 0
    for x in enemies:
        if x.getAlive():
            return True
        else: 
            number = number+1
            if number == len(enemies):
                return False
    
def getQuestion(question):
    if question == 1:
        return 'What will you do?\n(1.) Attack\n(2.) Run\n-->'
    if question == 2:
        return 'Which enemy to attack?\n-->'

def initEnemies(count, weapons, armor):
    print ('INiting Enemeies')
    enemies = []
    n = 0
    while n <= count:
        enemies.append(Character("Goblin", "Scout", 
                    20, 20,
                    0, 0, 
                    weapons[0], armor[0],
                    True))
        n = n + 1
    return enemies
    

def getRandom(num1,num2):
    number = random.randrange(num1,num2)
    return number
    
def battle(player, enemies):
    print ('You have encountered %s enemies!' % len(enemies))
    while True:
        ## If player dead, gameover
        if player.getAlive: 
            ## If all enemies dead, exit
            if checkForDead(enemies):
                ## Choose attack or run
                print ('%s' % player.getNameAndHealth())
                choice = int(input(getQuestion(1)))
                if choice == 1:
                    ## Player attack phase
                    ## Choose enemy
                    
                    printEnemies(enemies)
                    choice1 = int(input(getQuestion(2)))-1
                    ## Attack doDamage
                    doDamage(player, enemies[choice1])
                    printEnemies(enemies)
                    ## enemy attack phase
                    for x in enemies:
                        doDamage(x, player)
                ## Run, exit
                if choice == 2:
                    sys.exit()
            else:
                print('You Killed all enemies')
                sys.exit()
        else: 
            print('You Died')
            sys.exit()
    
        
def main():
    ## INIT OBJECTS
    ## INIT WEAPONS & ARMOR
    weapons = [Weapon('Tin Sword', 5, 0),
                Weapon('Iron Sword', 10, 0)]
    armor = [Armor('Tin Armor', 5, 0),
                Armor('Iron Armor', 10, 0)]
    
    ## INIT CHARACTERS
    player = Character("BOB", "Paladin", 
                            100, 100,
                            100, 100, 
                            weapons[1], armor[1], 
                            True)
    enemyCount =  getRandom(1,5) 
    enemies = initEnemies(enemyCount, weapons, armor)
    ## GET AND SHOW CHARACTER STATS
    # playerStats = getStats(player)
    # enemy1Stats = getStats(enemy1)
    # printStats(playerStats)
    # printStats(enemy1Stats)
    
    ## Battle Start
    battle(player, enemies)
    
    
                

    


## This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
        
    

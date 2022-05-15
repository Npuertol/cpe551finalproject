# Author: Nixon Puertollano
# Professor: Mukund Iyengar
# Class: CPE-551
#                                   LOST ARK DPS DEADEYE CALCULATOR
#
#

from math import floor, sqrt
from deSkills import skillList

spacer = "=========================================================================="
mamenu = "                           -- MAIN MENU --                                "
slhead = "                           -- SKILL LIST --                               "
addskl = "                           -- ADD A SKILL --                              "
delskl = "                         -- DELETE A SKILL --                             "
sklrot = "                         -- SKILL ROTATION --                             "
chrsts = "                         -- CHARACTER STATS --                            "
helpme = "                            -- HELP MENU --                               "
godbye = "                             -- GOODBYE --                                "


def displaySkills():
    for item in skillList:
        print(str(skillList.index(item)+1)+ '. ' + item[0])

def skillDesc(n):
    i = n-1
    print(skillList[i][0] + ": " + skillList[i][1])
    print(skillList[i][0] + " does " + str(skillList[i][2]) + " damage.")
    print(skillList[i][0] + " takes " + str(skillList[i][3] + skillList[i][4]) + " seconds to cast.") 

class Stats:
    
    def __init__(self, name, strength, wp, skillCount = 0, totalDamage = 0, idleTime = 0, moveTime = 0):
        self.name = name
        self.strength = strength
        self.wp = wp
        self.skillCount = skillCount
        self.totalDamage = totalDamage
        self.idleTime = idleTime
        self.moveTime = moveTime
        self.charRotation = []

    def calcAP(self):
        AP = floor(sqrt((self.strength*self.wp)/6))
        return AP

    def calculateDPS(self):
        DPS = round((self.totalDamage /(self.idleTime + self.moveTime)), 2)
        return DPS

    def displayStats(self):
        print("Name: " + self.name)
        print("Strength: " + str(self.strength))
        print("Weapon Power: " + str(self.wp))
        print("Attack Power: " + str(self.calcAP()))
        print("Total Number of Skills: " + str(self.skillCount))
        print("Total Damage: " + str(self.totalDamage))
        print("Time spent Stationary: " + str(self.idleTime) + " seconds")
        print("Time spent Moving: " + str(self.moveTime) + " seconds")
        print("Total Cast Time: " + str(self.idleTime + self.moveTime) + " seconds")
        try:
            print("Total DPS: " + str(self.calculateDPS()) + " damage per second")
        except:
            print("Total DPS: Cannot be Calculated")

    def addSkill(self, skill):
        skill -= 1
        if self.charRotation.count(skillList[skill]) == 1:
            print("You cannot add this skill since it is already in your rotation.")
            return
        try:
            skillLevel = int(input("Choose skill level of 1, 4, 7, or 10: "))
        except:
            print("Invalid input, defaulting skill level to 1.")
            skillLevel = 1
        if skillLevel == 1 or skillLevel == 4 or skillLevel == 7 or skillLevel == 10:
            currentDamage = ((skillLevel*self.calcAP()) + (skillLevel*skillList[skill][2]))
            self.totalDamage += currentDamage                                                   # given skill level, calculate totalDamage of ability and add value to character's totalDamage
            print("This ability does " + str(currentDamage) + " damage.")
        else:
            print("Invalid input, please choose 1, 4, 7, or 10 next time")
            return
        self.charRotation.append(skillList[skill])                                              # add to end of skillList
        self.charRotation[-1][5] = skillLevel                                                   # change skill Level in charRotation
        self.idleTime += skillList[skill][3]                                                    # increment character's idle and move time given abilities' stats
        self.moveTime += skillList[skill][4]
        self.skillCount += 1
        print("You added " + skillList[skill][0] + " to your skill rotation!")
        if self.skillCount == 1:
            print("You have " + str(self.skillCount) + " skill in your rotation now.")
        else:
            print("You have " + str(self.skillCount) + " skills in your rotation now.")


    def deleteSkill(self, skill):
        if skill not in range(1, self.skillCount + 1):
            print("Invalid input, enter number within Rotation List range.")
            return
        else:
            skill -= 1
            skillLevel = self.charRotation[skill][5]
            self.totalDamage -= ((skillLevel*self.calcAP()) + (skillLevel*self.charRotation[skill][2]))
            self.idleTime -= self.charRotation[skill][3]
            self.moveTime -= self.charRotation[skill][4]
            self.skillCount -= 1
            print("You have successfully deleted " + self.charRotation[skill][0] + " from your Skill Rotation.")
            print("You now have " + str(self.skillCount) + " skills in your Rotation.")
            self.charRotation.pop(skill)
            
        

    def displayRotation(self):
        for item in self.charRotation:
            print(str(self.charRotation.index(item)+1)+ '. ' + item[0] + " - " + "Level " + str(item[5]))

def main():
    print("Welcome to Lost Ark Deadeye Class DPS Calculator!")
    username = input("First, enter your character's name. ")
    try:
        userstrength = int(input("Please input your character's strength (int only): "))
    except:
        print("Invalid input, defaulting strength to value of 1")
        userstrength = 1
    try:
        userwp = int(input("Please input your character's weapon power: "))
    except:
        print("Invalid input, defaulting weapon power to value of 1")
        userwp = 1
    char = Stats(username, userstrength, userwp)
    print("Welcome, " + char.name + ".")
    
    while True:
        print(spacer)
        print(mamenu)                            
        print("1. Display Skill List")
        print("2. Add Skill to Rotation")
        print("3. Delete Skill from Rotation")
        print("4. Display Skill Rotation List")
        print("5. Display Character Stats")
        print("6. Help")
        print("Press any other key to quit out of the program.")
        print(spacer)

        menuin = input("Please choose an input: ")

        if menuin == "1":
            while True:
                print(spacer)
                print(slhead)
                displaySkills()
                print(spacer)
                print("Press any non-integer key to go back to main menu OR")
                try:
                    skillin = int(input("Enter a skill's list number to display its description: "))
                except:
                    break
                else:
                    skillDesc(skillin)
                    print(spacer)
                    input("Press enter or any key to go back to Skill List ")
                
        
        elif menuin == "2":
            if char.skillCount == 16:
                print("You cannot add anymore skills since you have gone over the limit. Delete a skill first.")
                input("Press enter or any key to go back to main menu ")
                pass
            else:
                print(spacer)
                print(addskl)
                displaySkills()
                print(spacer)
                print("Press any non-integer key to go back to main menu OR")
                try:
                    skillin = int(input("Enter a skill's list number to add it to your rotation: "))
                except:
                    pass
                else:
                    char.addSkill(skillin)
                    print(spacer)
                    input("Press enter or any to go back to main menu ")
            
        
        elif menuin == "3":
            if char.skillCount == 0:
                print("You cannot delete any skills since you haven't added any yet.")
                input("Press enter or any key to go back to main menu ")
                pass
            else:
                print(spacer)
                print(delskl)
                char.displayRotation()
                print(spacer)
                try:
                    skillin = int(input("Enter the skill rotation's number to delete it: "))
                except:
                    pass
                else:
                    char.deleteSkill(skillin)
                    print(spacer)
                    input("Press enter or any to go back to main menu ")
            
      
        elif menuin == "4":
            print(spacer)
            print(sklrot)
            char.displayRotation()
            print(spacer)
            input("Press enter or any key to return to main menu ")
        
        elif menuin == "5":
            print(spacer)
            print(chrsts)
            char.displayStats()
            print(spacer)
            input("Press enter or any key to return to main menu ")
        
        elif menuin == "6":
            print(spacer)
            print(helpme)
            print("The goal of this program is to allow Users to input their character's combat stats")
            print("and skill rotation in order to calculate in-game stats such as Attack Power, DPS,")
            print("and Time to Cast.")
            print("Pressing 1 shows all of the skills that the Deadeye Class has. You can also read")
            print("each skill's description here.")
            print("Pressing 2 allows users to add a skill of their choice and the skill's level.")
            print("Pressing 3 allows users to delete a skill from their current Rotation.")
            print("Pressing 4 displays the users' current Skill Rotation.")
            print("Pressing 5 displays all of the users' combat stats and in-game stats.")
            print("Pressing 6 brings up this help menu.")
            print("We hope you enjoy using this program!")
            print(spacer)
            input("Press enter or any key to return to the main menu ")
            pass
        
        else:
            print(spacer)
            print(godbye)
            print("Thank you for using the Lost Ark Deadeye Class DPS Calculator!")
            break
            

if __name__ == "__main__":
    main()

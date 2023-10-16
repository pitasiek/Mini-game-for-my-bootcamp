# Project made on 16.10.2023. Made by Piotr Zięba.
# It's a text-based mini-game where the player needs to select answers wisely.
# This project is related with 100 days of Code - Bootcamp.

print("Welcome to the ZOO office! You need to investigate the building and survive.")
print("Each right decision gives you 20 points.")
points = 0

decision = input("""You enter a big building located somewhere in your local zoo. 
Do you go "upstairs" or straight to the "information desk"?""")

if decision == "upstairs": # Two options.
    points += 20
    print("-----------------------------------------------------------------------------------------------------------")
    print("On the way upstairs, there is a big and dangerous python crawling downstairs.")
    danger = input("Will you 'run away' or 'pass it'?")
    if danger == "pass it": # Two options.
        points += 20
        print("-----------------------------------------------------------------------------------------------------------")
        print("The python doesn't harm you; in fact, it doesn't even pay attention to you. ")
        print("You reach the second floor where you realize that you're all by yourself. ")
        print("It is suspicious, but you look through the window, and there are people walking and doing their things not feeling any danger.")
        print("It gives you some relief. Soon, your eyes look at the nearest door which leads to room 12. ")
        safety = input("Do you 'open' the door or 'ignore' it?")
        if safety == "ignore": # Three options.
            points += 20
            print("-----------------------------------------------------------------------------------------------------------")
            print("You ignore that door and you walk down the hall.")
            print("A few meters away from door 12, you hear a loud noise.")
            print("You turn back and you see the door shattered into pieces.")
            print("A huge gorilla is standing a few meters behind you, a little bit disoriented, and its leg doesn't seem to be okay. ")
            luck = input("Do you decide to 'help' the gorilla, 'run' to the nearest door, or go 'upstairs'?")
            if luck == "upstairs": # Three options.
                points += 20
                print("-----------------------------------------------------------------------------------------------------------")
                print("Going upstairs, you find one door leading to the side staircase, and the door has a mirror.")
                print("Before you grab the knob, you look into the mirror, finding out that you're not alone.")
                print("You feel shivers and cold sweat.")
                print("There's been something on your head along the way, and you didn't realize it until now.")
                mirror = input("What do you do about the creature? Do you 'hit it', 'shake it off,' or 'ignore it'?")
                if mirror == "ignore it": # Three options.
                    points += 20
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("You ignored the creature, and that was wise!")
                    print("You've always been scared of insects, but this little cockroach saves your life on the way down.")
                    print("As you enter the staircase, you notice some crazy woman with a knife.")
                    print("Not having anything else with you than that cockroach, you grab it and throw it at her.")
                    print("Seeing it, she starts to scream, and she drops the knife.")
                    print("You grab the knife and run downstairs without looking back.")
                    end = input("THE END! You're the winner! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
                    if end == "y":
                        print("-----------------------------------------------------------------------------------------------------------")
                        print("Goodbye!")
                    else:
                        print("I'm sorry, but there is nothing more to do here.")
                elif mirror == "shake it off":
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("Small insect falls on the ground and you quickly run inside the staircase.")
                    print("Three steps in, you hear loud scream from behind and a crazy woman jumps on you stabbing you on your back 3 times.")
                    print("You turn slighly to look into her face to ask for marcy but its too late, her face looks content and you loose to much blood.")
                    print("GAME OVER")
                    end = input(
                        "THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
                    if end == "y":
                        print("-----------------------------------------------------------------------------------------------------------")
                        print("Goodbye!")
                    else:
                        print("I'm sorry, but there is nothing more to do here.")
                elif mirror == "hit it":
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("You hit the insect and it leaves nasty stain on your hair. You get angry as you do your best to wipe it out.")
                    print("You forget about the gorilla, which had enough time to catch up with you.")
                    print("Just as it was about to tear you apart you managed to push your finger into it's eye. Ignoring the door you run downstairs.")
                    print("The huge python jumps on you and wraps around you to eat you alive.")
                    print("GAME OVER")
                    end = input(
                        "THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
                    if end == "y":
                        print("-----------------------------------------------------------------------------------------------------------")
                        print("Goodbye!")
                    else:
                        print("I'm sorry, but there is nothing more to do here.")
            elif  luck == "run":
                print("-----------------------------------------------------------------------------------------------------------")
                print("Behind the nearest door you find a wall of bricks. The door leads to nowehere!")
                print("the gorilla grabs you from behind and throws you out the window.")
                print("GAME OVER")
                end = input(
                    "THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
                if end == "y":
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("Goodbye!")
                else:
                    print("I'm sorry, but there is nothing more to do here.")
            else:
                print("-----------------------------------------------------------------------------------------------------------")
                print("As you approach the gorilla, it is surprised and it doesn't move.")
                print("The moment you touch it's leg it grabs you and throws you to the stairs.")
                print("The big python from before bites your arm and wraps around you.")
                print("GAME OVER")
                end = input(
                    "THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
                if end == "y":
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("Goodbye!")
                else:
                    print("I'm sorry, but there is nothing more to do here.")
        elif safety == "open":
            print("-----------------------------------------------------------------------------------------------------------")
            print("It is dark inside and you have nothing with you that could be useful in this situation. You don't know where the switch is.")
            print("A huge gorilla grabs you and pulls you into the darkness of the room.")
            print("GAME OVER")
            end = input("THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
            if end == "y":
                print("-----------------------------------------------------------------------------------------------------------")
                print("Goodbye!")
            else:
                print("I'm sorry, but there is nothing more to do here.")
    elif danger == "run away":
        print("-----------------------------------------------------------------------------------------------------------")
        print("You decide to run away from the dangerous python. You've managed to escape.")
        end = input("THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
        if end == "y":
            print("-----------------------------------------------------------------------------------------------------------")
            print("Goodbye!")
        else:
            print("I'm sorry, but there is nothing more to do here.")
    else:
        print("-----------------------------------------------------------------------------------------------------------")
        print("Sorry, your input is not recognized. Please enter 'pass it' or 'run away'.")
elif decision == "information desk":
    print("-----------------------------------------------------------------------------------------------------------")
    print("You decide to go straight to the information desk. The friendly staff there provide you with useful information about the zoo. Unfortunately, you don't earn any points in this route.")
    end = input("THE END! You've scored: " + str(points) + " points. Do you want to turn off the game? y or n")
    if end == "y":
        print("-----------------------------------------------------------------------------------------------------------")
        print("Goodbye!")
    else:
        print("I'm sorry, but there is nothing more to do here.")
else:
    print("-----------------------------------------------------------------------------------------------------------")
    print("Sorry, your input is not recognized. Please enter 'upstairs' or 'information desk.'")

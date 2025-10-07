import time

name = input("What is your name, adventurer? ")
hp = 10
inventory: list[str] = []

print("Welcome to the adventure,", name + "!")
print("You have", hp, "health points.")
time.sleep(1)

print("You wake up in a dark forest...")
time.sleep(1)

choice1 = input(
    "You reach a crossroad. Do you go left or right? (left/right): "
).lower()

if choice1 == "left":
    print("You walk along a narrow path and see a small cabin.")
    choice2 = input("Do you go inside or keep walking? (inside/walk): ").lower()

    if choice2 == "inside":
        print("You find a dusty old chest...")
        choice3 = input("Do you open it? (yes/no): ").lower()
        if choice3 == "yes":
            print("Inside, you find a shiny sword! (+ item)")
            inventory.append("sword")
        else:
            print("You decide not to open it and leave the cabin.")

    elif choice2 == "walk":
        print("You walk further and it starts raining heavily.")
        print("You lose 2 health points from the cold.")
        hp -= 2

    else:
        print("You hesitate too long. A wolf appears and bites you!")
        hp -= 5

elif choice1 == "right":
    print("You find a river. The water is fast and cold.")
    choice2 = input("Do you swim across or look for a bridge? (swim/bridge): ").lower()

    if choice2 == "swim":
        print("You try to swim but the current is strong!")
        hp -= 5
        print("You lose 5 health points.")
    elif choice2 == "bridge":
        print("You find a small bridge and cross safely.")
        print("On the other side, you meet an old man who gives you a healing potion.")
        inventory.append("potion")
    else:
        print("You wait too long. Night falls and you get lost.")
        hp -= 3

else:
    print("You stand still without choosing and fall asleep under a tree.")
    hp -= 2

print("After a long journey, you see a glowing cave entrance.")
choice_final = input("Do you enter the cave? (yes/no): ").lower()

if choice_final == "yes":
    if "sword" in inventory:
        print("A dragon appears! But you fight bravely with your sword!")
        print("After a tough battle, you defeat the dragon. You win!")
    elif "potion" in inventory:
        print(
            "You drink your potion and escape safely with a secret treasure. You win!"
        )
    else:
        print("You enter unarmed. The dragon sees you and breathes fire... Game over.")
        hp = 0
else:
    print("You turn away and live to adventure another day.")

print("=== GAME SUMMARY ===")
print("Health points left:", hp)
print("Inventory:", inventory)
if hp <= 0:
    print("You did not survive the adventure.")
else:
    print("You survived, brave adventurer!")
print("Thanks for playing,", name + "!")

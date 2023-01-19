import random

# Initialize the player's health, hunger, and thirst and define running
health = 100
hunger = 100
thirst = 100
running = True

# Initialize the player's max health, hunger, and thirst
max_health = 100
max_hunger = 100
max_thirst = 100

# Initialize the player's inventory
inventory = []

# Create a dictionary of crafting recipes
recipes = {
    "bandage": ["cloth", "clean water"],
    "clean water": ["rocks", "water"],
    "torch": ["stick", "cloth"],
    "cloth": ["leaves"]
}

# Create a list of possible actions
actions = ["eat", "drink", "sleep", "explore", "craft", "mine", "heal"]

# Create the game loop
while running == True:
    # Print the player's health, hunger, and thirst
    print("Health:", health)
    print("Hunger:", hunger)
    print("Thirst:", thirst)

    # Print the player's inventory
    print("Inventory:", inventory)

    # Ask the player for their next action
    action = input("What would you like to do? ").strip().lower()

    # Check if the player's action is valid
    if action not in actions:
        print("Invalid action.")
        continue

    # Perform the player's action
    if action == "eat":
        if "food" in inventory:
            hunger -= random.randint(10, 20)
            inventory.remove("food")
            print("You eat some food.")
        else:
            print("You don't have any food.")

    elif action == "drink":
        if "water" in inventory:
            thirst -= random.randint(10, 20)
            inventory.remove("water")
            print("You drink some water.")
        else:
            print("You don't have any water.")

    elif action == "sleep":
        health = min(health+random.randint(10, 20), max_health)
        hunger += random.randint(5, 10)
        thirst += random.randint(5, 10)
        print("You sleep for the night.")

    elif action == "explore":
        chance = random.randint(1, 100)
        if chance < 50:
            print("You find some food.")
            inventory.append("food")
        elif chance < 25:
            print("You find some water.")
            inventory.append("water")
        else:
            print("you were ambushed and died")
            health -= 1000

    elif action == "craft":
        # Ask the player what they want to craft
        craft_item = input("What would you like to craft? ").strip().lower()

        # Check if the craft_item is a valid recipe
        if craft_item not in recipes:
            print("Invalid recipe.")
            continue

        # Check if the player has the required items
        required_items = recipes[craft_item]
        for item in required_items:
            if item not in inventory:
                print("You don't have the required items.")
                break
        else:
            # Craft the item
            for item in required_items:
                inventory.remove(item)
            inventory.append(craft_item)

if health <= 0:
    print("you died")

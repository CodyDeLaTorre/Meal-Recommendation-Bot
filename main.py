import random

foods1d = ["TeryChick", "ChickenVeggie", "HoneyLemChick", "ChickenStrips", "ChipotleBowl", "ButterChicken"]
foods2d = ["Hamburger", "Spaghetti", "Roast", "Steak", "KBBQBeef", "Burritos", "Tacos", "Lasagna", "Albondigas"]
foods3 = ["FastFood", "Breakfast"]
foods4 = ["EggsBacon", "Oatmeal", "SpamEggs", "Cereal"]
foods5 = ["Burritos"]

def lunch():
    print("You should have " + random.choice(foods5))

def dinner():
    answer = input("Do you have beef or chicken? ")
    if answer == "Chicken":
        return "You should have " + random.choice(foods1d)
    if answer == "chicken":
        return "You should have " + random.choice(foods1d)
    elif answer == "Beef":
        return "You should have " + random.choice(foods2d)
    elif answer == "beef":
        return "You should have " + random.choice(foods2d)
    elif answer == "Both":
        return "You should have " + random.choice(foods1d) + " or", random.choice(foods2d)
    else:
        return "You should have " + random.choice(foods3)


def breakfast():
    return random.choice(foods4)


name = input("Hello! I am the Meal Recommendation Bot, what's your name? \n")
print("Okay " + name)
choice = input("Are you having breakfast, lunch or dinner? ")

if choice == "dinner":
    print(dinner())
elif choice == "breakfast":
    print(breakfast())

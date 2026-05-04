# simple dungeon text based game
# where the player can input their name
# have their own stats
# you provide the player classes to choose from your own declared classes
# attack system
# defense and skill mechanism or additional mechanics
# complete
# gold and shop system
# end game

import random

print("*"*30)
print(f'{"Dungeon Crawler":^30}')
print("*"*30)
print("1. Start Game")
print("2. Support the Dev ")
print("3. Exit")
print("*"*30)

# my_list = ["", ""]
# my_tuple = [test , test_2]
# sample_dictionary = {"Item 1 " : "Item 1 Value"}

# Class List using dictionary
player_jobs = {
    "Paladin" : {
        "hp": 1,
        "atk": 1,
        "def": 1
    }, 
    "Ranger" : {
        "hp": 1,
        "atk": 1,
        "def": 1
    }, 
}

# sample_key = player_jobs.get("Paladin")
# print(sample_key)

monsters = [
    ("Gob", 10, 2),
    ("Orc", 50, 10),
    ("Dragon", 10000, 1000)
]

def spawn_monster (monsters):
    monster = random.choice(monsters)
    return [monster [0], monster [1], monster [2]]

# monster_name, monster_hp, monster_atk = spawn_monster(monsters)

def start_game():
    print("Starting Game...")
    player_name = input("Enter your name: ")
    
    player_class = select_job()

    print(f"Welcome, {player_name} the {player_class}")

def select_job():
    print("Choose your class: ")
    print("1. Paladin")
    print("2. Ranger")

    while True:
        job_choice = input("Enter choice: ")

        match job_choice:
            case "1":
                return "Paladin"
            case "2":
                return "Ranger"
            case _:
                return "Invalid input"

while True: #main menu choice

    menu_choice = input("What would you like to do?: ")
    
    match menu_choice:

        case "1":
            start_game()
            
        case "2":
            print("Support the dev?\nGive a coffee.")
        
        case "3":
            print("Exiting the game")
            break
        
        case _:
            print("Invalid choice")
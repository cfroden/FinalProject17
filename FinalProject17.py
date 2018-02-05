import random
list = ["one" "two" "three"]
print("\t*Super Smash Brothers opening music")
print("\t*Melee*.")

print("\nHow to play.\n\nPlayers take turn to choose a move. Moves deal certain aounts of damage")

player_health = 100
enemy_health = 100

print("epic win start")

while player_health >= 0 and enemy_health >= 0:


    decision = input("""You are faced with an enemy, what do u wanna do?
    1 = ForwardSmash
    2 = Downtilt
    3 = MaximumTomato
    ---> """)

    if decision == "1":
        enemy_health -= 20
        print(f"enemy health is {enemy_health}")
    elif decision == "2":
        enemy_health -= 10
        print(f"enemy health is {enemy_health}")
    elif decision == "3":
        player_health += 10
        print(f"your health is {player_health}")

    enemy_choice = random.randint(1,3)
    if enemy_choice == "1":
        player_health -= 10
        print(f"your health is {player_health}")
    elif enemy_choice == "2":
        player_health -= 10
        print(f"your health is {player_health}")
    elif enemy_choice == "3":
        enemy_health += 10
        print(f"enemy health is {enemy_health}")

if enemy_health <= 0:
    print("you win xD")
if player_health <= 0:
    print("you lose xC")





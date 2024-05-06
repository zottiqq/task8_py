import random

def game(num_doors, num_prizes):
    doors = ['пусто'] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"


    player1_choice = random.randint(0, num_doors-1)
    player2_choice = random.randint(0, num_doors-1)
    
    opened_door = random.choice([idx for idx in range(num_doors) if doors[idx] == "пусто" and idx != player1_choice])
    new_choice_player1 = [idx for idx in range(num_doors) if idx != player1_choice and idx != opened_door][0]

    result_player1 = "выиграл" if doors[new_choice_player1] == "приз" else "проиграл"
    result_player2 = "выиграл" if doors[player2_choice] == "приз" else "проиграл"
    return {"doors": doors, "player1_choice": player1_choice, "player2_choice": player2_choice, "opened_door": opened_door, "result_player1": result_player1, "result_player2": result_player2}



num_doors = 3
num_prizes = 1
num_simulations = 10000

wins_player1_switch = 0
wins_player2_stay = 0

for _ in range(num_simulations):
    game_result = game(num_doors, num_prizes)
    if game_result["result_player1"] == "выиграл":
        wins_player1_switch += 1
    if game_result["result_player2"] == "выиграл":
        wins_player2_stay += 1

probability_player1_switch = wins_player1_switch / num_simulations
probability_player2_stay = wins_player2_stay / num_simulations

print("Вероятность выигрыша для игрока, меняющего свой выбор:", probability_player1_switch)
print("Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе:", probability_player2_stay)
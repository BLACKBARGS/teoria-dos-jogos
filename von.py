import random
import matplotlib.pyplot as plt
import numpy as np

class TitForTat:
    def __init__(self):
        self.last_move = 1
    
    def play(self, opponent_last_move):
        if opponent_last_move is not None:
            return opponent_last_move  
        return 1  

class AlwaysCooperate:
    def play(self, opponent_last_move):
        return 1  

class AlwaysDefect:
    def play(self, opponent_last_move):
        return 0  

class RandomStrategy:
    def play(self, opponent_last_move):
        return random.choice([0, 1]) 

class Grudger:
    def __init__(self):
        self.betrayed = False
    
    def play(self, opponent_last_move):
        if opponent_last_move == 0:
            self.betrayed = True
        return 0 if self.betrayed else 1 

class TitForTwoTats:
    def __init__(self):
        self.history = []
    
    def play(self, opponent_last_move):
        if opponent_last_move is not None:
            self.history.append(opponent_last_move)
        if len(self.history) >= 2 and self.history[-2:] == [0, 0]:
            return 0
        return 1

strategies = {
    "Tit For Tat": TitForTat(),
    "Always Cooperate": AlwaysCooperate(),
    "Always Defect": AlwaysDefect(),
    "Random": RandomStrategy(),
    "Grudger": Grudger(),
    "Tit For Two Tats": TitForTwoTats(),
}

good_guys = ["Tit For Tat", "Always Cooperate", "Tit For Two Tats"]
bad_guys = ["Always Defect", "Grudger"]

REWARDS = {
    (1, 1): (3, 3),  
    (1, 0): (0, 5),  
    (0, 1): (5, 0), 
    (0, 0): (1, 1),  
}

scores = {name: 0 for name in strategies.keys()}
num_rounds = random.randint(50, 200)

for player1 in strategies:
    for player2 in strategies:
        if player1 == player2:
            continue
        
        strat1 = strategies[player1]
        strat2 = strategies[player2]

        history1 = None
        history2 = None

        for _ in range(num_rounds):
            move1 = strat1.play(history2)
            move2 = strat2.play(history1)
            
            score1, score2 = REWARDS[(move1, move2)]
            scores[player1] += score1
            scores[player2] += score2

            history1 = move1
            history2 = move2

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
players = [x[0] for x in sorted_scores]
scores_values = [x[1] for x in sorted_scores]

plt.figure(figsize=(10, 5))
plt.barh(players[::-1], scores_values[::-1], color=['green' if p in good_guys else 'red' for p in players])
plt.xlabel("Pontuação Média")
plt.ylabel("Estratégia")
plt.title("Torneio do Dilema do Prisioneiro")
plt.show()

print("Ranking:")
for rank, (player, score) in enumerate(sorted_scores, 1):
    print(f"{rank}. {player} - {score}")

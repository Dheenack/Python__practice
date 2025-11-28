import random

choices = ["Explore", "Repeat Best Option"]

def cognitive_decision(reward_history):
    if not reward_history:
        return random.choice(choices)
    
    if max(reward_history) > 0.7:
        return "Repeat Best Option"
    else:
        return "Explore"

reward_history = [0.4, 0.6, 0.8]
print(cognitive_decision(reward_history))

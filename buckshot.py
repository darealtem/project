import random

def Players():
    player = None
    print(f"player: {player}")
    player2 = None
    print(f"player2: {player2}")
    


def shotgun():
    chance = random.choice([i/10 for i in range (11)])
    if chance <= 0.5:
        print("blank")
        return "blank"
    elif chance >= 0.6:
        print("live")
        return "live"
    
def load_shotgun():
    num_of_shells = random.randint (4,9)
    shells = []
    for _ in range(num_of_shells):
        shells.append(shotgun())
    return shells
    
"""
def round():
    who starts round

'''
def main():
    round logic
    round count
    shoot self/other player
    '''
"""
load_shotgun()
Players()

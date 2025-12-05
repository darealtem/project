import random

def Players():
    player1_name = input("please enter player 1's name. ")
    player2_name = input("please enter player 2's name. ")
    player = player1_name
    print(f"player: {player}")
    player2 = player2_name
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
    gun = shotgun
    who starts round
    pvpp
    items
    

'''
def main():
    item logic
    round logic
    reviving
    round count
    countinue/quit
    shoot self/other player
    '''
"""
load_shotgun()
Players()

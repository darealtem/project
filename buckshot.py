import random

def Players():
    player = "player"
    print(f"player: {player}")
    player2 = "dealer"
    print(f"player2: {player2}")
    


def shotgun():
    chance = random.choice([i/10 for i in range (11)])
    if chance <= 0.5:
        print("blank")
    elif chance >= 0.6:
        print("live")
    

    
'''
def round():
    who starts round
    pvpp
    items
    


def main():
    item logic
    round logic
    reviving
    round count
    countinue/quit
    shoot self/other player
    '''

    
Players()

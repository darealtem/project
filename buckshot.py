import random

class Player:
    def __init__(self, name, health=3, is_ai=False):
        self.name = name
        self.health = health
        self.is_ai = is_ai
        self.items = []
    
    def take_damage(self):
        self.health -= 1
        print(f"{self.name} takes damage! Health: {self.health}")
    
    def is_alive(self):
        return self.health > 0
    
def shotgun():
    chance = random.choice([i/10 for i in range (11)])
    if chance <= 0.5:
        print("blank")
        return "blank"
    elif chance >= 0.6:
        print("live")
        return "live"
    
def load_shotgun():
    num_of_shells = random.randint(4, 9)
    shells = []
    for _ in range(num_of_shells):
        shell_type = random.choice(['blank', 'blank', 'live', 'live', 'live'])
        shells.append(shell_type)
    live_count = shells.count('live')
    blank_count = shells.count('blank')
    print(f"\n[Shotgun loaded: {num_of_shells} shells - {live_count} live, {blank_count} blank]")
    return shells

def calculate_shoot_self_value(shells, known_info):
    if not shells:
        return 0
    live_count = shells.count('live')
    blank_count = shells.count('blank')
    total = len(shells)
    if total == 0:
        return 0
        
def greedy_ai_decision(shells, player, opponent):
    if not shells:
        return "opponent"
    
    blank_prob = calculate_shoot_self_value(shells, {})
    live_prob = 1 - blank_prob
    
    print(f"\n[AI Analysis: {len(shells)} shells left]")
    print(f"[Blank probability: {blank_prob:.2%}, Live probability: {live_prob:.2%}]")
    
    # Greedy strategy:
    # 1. If blank probability > 60%, shoot self (safe + get another turn)
    # 2. If opponent health is low and live probability > 50%, shoot opponent
    # 3. Otherwise, shoot opponent if live probability > blank probability
    
    if blank_prob > 0.6:
        print(f"[AI Strategy: High blank probability - shooting self for extra turn]")
        return "self"
    elif opponent.health <= 1 and live_prob > 0.5:
        print(f"[AI Strategy: Opponent low health - going for kill]")
        return "opponent"
    elif live_prob > blank_prob:
        print(f"[AI Strategy: More lives than blanks - shooting opponent]")
        return "opponent"
    else:
        print(f"[AI Strategy: Playing it safe - shooting opponent]")
        return "opponent"
def shoot(target, shells, shooter, opponent):
    """Execute shot and return if shooter gets another turn"""
    if not shells:
        print("Shotgun empty!")
        return False
    
    shell = shells.pop(0)
    print(f"\n{shooter.name} shoots {target}...")
    print(f"*BANG* - {shell.upper()}!")
    
    if shell == 'live':
        if target == 'self':
            shooter.take_damage()
        else:
            opponent.take_damage()
        return False  
    else:
        print(f"{shooter.name} survives and gets another turn!")
        return target == 'self' 

def player_turn(player, opponent, shells):
    """Handle player's turn"""
    while True:
        if not shells:
            print("\nShotgun empty! Reloading...")
            return True
        
        if player.is_ai:
            target = greedy_ai_decision(shells, player, opponent)
        else:
            print(f"\n{player.name}'s turn - Shells remaining: {len(shells)}")
            target = input("Shoot (s)elf or (o)pponent? ").lower()
            while target not in ['s', 'o']:
                target = input("Invalid choice. Shoot (s)elf or (o)pponent? ").lower()
            target = 'self' if target == 's' else 'opponent'
        
        gets_extra_turn = shoot(target, shells, player, opponent)
        
        if not opponent.is_alive():
            return False
        
        if not gets_extra_turn:
            return True

def game_round(player1, player2):
    """Play one round"""
    shells = load_shotgun()
    current_player = player1 if random.choice([True, False]) else player2
    
    print(f"\n{current_player.name} goes first!")
    
    while shells and player1.is_alive() and player2.is_alive():
        opponent = player2 if current_player == player1 else player1
        
        continue_round = player_turn(current_player, opponent, shells)
        
        if not continue_round:
            break
        

        current_player = player2 if current_player == player1 else player1

def main():
    print("=== BUCKSHOT ROULETTE ===\n")
    
    player1 = Player("Player 1", health=3, is_ai=False)
    player2 = Player("AI Opponent", health=3, is_ai=True)
    
    round_num = 1
    
    while player1.is_alive() and player2.is_alive():
        print(f"\n{'='*40}")
        print(f"ROUND {round_num}")
        print(f"{player1.name}: {player1.health} HP | {player2.name}: {player2.health} HP")
        print(f"{'='*40}")
        
        game_round(player1, player2)
        round_num += 1
    
    print("\n" + "="*40)
    if player1.is_alive():
        print(f" {player1.name} WINS!")
    else:
        print(f" {player2.name} WINS!")
    print("="*40)

if __name__ == "__main__":
    main()

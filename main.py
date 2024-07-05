from classes import *
import matplotlib.pyplot as plt
import numpy as np

# initalize variables -------------------------------------------------------------------------------------------------
initial_stack = 1000
num_hands = 100
num_games = 1000
hit_cutoff = 18
bet_type = 'Dynamic'



# ---------------------------------------------------------------------------------------------------------------
game = Game() # initialize game instance
player = Player('Sam', initial_stack) # generate player
dealer = Dealer() # generate dealer
profit_tracker = []

# play -----------------------------------------------------------------------------------------------------------
while game.game_numer <= num_games:
    print(f'\nGame number: {game.game_numer} -------------------')
    while game.hand_number < num_hands:
        deck = Deck()  # generate and randomize deck of cards
        print(f'Starting hand {game.hand_number}')
        print(f'{player.name} bets 5')
        if bet_type == 'Static':
            bet = 0.01*initial_stack
        elif bet_type == 'Dynamic':
            bet = 0.01*player.stack

        Deck.deal_cards(2, player, 1, dealer, deck)

        stop_flag = False
        while stop_flag == False:
            if player.showing_tot == 21:
                print('Blackjack! Player wins!')
                player.stack += bet
                stop_flag = True
                break

            elif player.showing_tot > 21:
                print('Bust! Dealer wins')
                player.stack -= bet
                stop_flag = True
                break

            elif player.showing_tot <= hit_cutoff:
                print('Hit me')
                Deck.deal_cards(1, player, 0, dealer, deck)

            else:
                print('Stay')
                break

        while dealer.showing_tot < 17 and stop_flag == False:
            Deck.deal_cards(0, player, 1, dealer, deck)

        if stop_flag is not True:
            if player.showing_tot > dealer.showing_tot:
                print('Player wins!')
                player.stack += bet
            elif player.showing_tot == dealer.showing_tot:
                print('Split')
            elif dealer.showing_tot > 21:
                print('Dealer busts! Player wins!')
                player.stack += bet
            else:
                print('Dealer wins')
                player.stack -= bet

        # reset for next hand
        print(f'{player.name} has a stack of {player.stack}')
        game.reset_hand(player, dealer)

    profit = 100*(player.stack-initial_stack)/initial_stack
    print(f'Player finishes with a profit of: {profit}%')
    profit_tracker.append(profit)
    game_tracker = list(range(1,num_games+1))
    game.reset_game(player, initial_stack)

mean = np.sum(profit_tracker)/len(profit_tracker)
variance = sum([((x - mean) ** 2) for x in profit_tracker]) / len(profit_tracker)
std_dev = variance ** 0.5
print(f'\nAverage profit: {mean}%')
print(f'Variance of profits: {variance}')
print(f'Standard Deviation of profits: {std_dev}')
plt.figure(figsize=(8,5))
plt.hist(profit_tracker, bins=20)
plt.xlabel('Profit (%)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Blackjack Player Profits using {bet_type} Betting and a Hit Cutoff of {hit_cutoff}')
plt.show()


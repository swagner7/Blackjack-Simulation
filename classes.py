class Game:
    def __init__(self):
        print('Initializing game...')
        self.hand_number = 1
        self.game_numer = 1

    def reset_hand(self, player, dealer):
        player.showing_cards = []
        dealer.showing_cards = []
        self.hand_number += 1

    def reset_game(self, player, initial_stack):
        self.game_numer += 1
        self.hand_number = 1
        player.stack = initial_stack


class Player(Game):
    def __init__(self, name, stack):
        print('Generating player...')
        self.name = name
        self.stack = stack
        self.showing_cards = []
        self.showing_tot = 0
        print(f'Hello, my name is {self.name} and I have a stack of {self.stack}')



class Dealer(Game):
    def __init__(self):
        print('Generating dealer...')
        self.showing_cards = []
        self.showing_tot = 0

class Deck:
    def __init__(self):
        import random
        print('\nGenerating 52-card deck...')
        suits = ['h', 'c', 'd', 's']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

        deck = []
        for i in values: # combine suits and values
            deck.append(str(i + suits[0]))
            deck.append(str(i + suits[1]))
            deck.append(str(i + suits[2]))
            deck.append(str(i + suits[3]))

        random.shuffle(deck) # shuffle deck
        self.cards = deck


    def deal_cards(amount_player, player, amount_dealer, dealer, deck):

        def eval_cards(cards):
            tot = 0
            for card in cards:
                if card[0] == 'A':
                    tot += 11
                else:
                    try:
                        tot += int(card[0])
                    except:
                        tot += 10

            return(tot)

        print(f'\nDealing...')

        player.showing_cards.extend(deck.cards[:amount_player])
        player.showing_tot = eval_cards(player.showing_cards)
        deck.cards = deck.cards[amount_player:]

        dealer.showing_cards.extend(deck.cards[:amount_dealer])
        dealer.showing_tot = eval_cards(dealer.showing_cards)
        deck.cards = deck.cards[amount_dealer:]

        print(f'Player is showing: {player.showing_cards} for a total of {player.showing_tot}')
        print(f'Dealer is showing: {dealer.showing_cards} for a total of {dealer.showing_tot}')
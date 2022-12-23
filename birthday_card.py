import random

def deal_cards(num_players, num_cards):
    # This function deals a given number of cards to a given number of players.
    # It returns a list of hands, where each hand is a list of cards.
    # The cards are represented as integers, with the values ranging from 1 to 10.
    # The function shuffles the deck of cards before dealing them.
    deck = list(range(1, 11))
    random.shuffle(deck)
    hands = [[] for _ in range(num_players)]
    for i in range(num_cards):
        for j in range(num_players):
            hands[j].append(deck.pop())
    return hands

def play_card(player, card, hands, draw_pile):
    # This function plays a card for a given player.
    # It updates the hands of the players and the draw pile based on the rules of the game.
    # If the card is a 2 or a 7, the function prompts the player to choose another player to draw cards or swap hands with.
    # If the card is any other number, the function discards it and the player's turn ends.
    if card == 2:
        target = int(input(f'{player}, choose a player to draw two cards (1-{len(hands)}): ')) - 1
        draw_pile += hands[target][:2]
        hands[target] = hands[target][2:]
    elif card == 7:
        target = int(input(f'{player}, choose a player to swap hands with (1-{len(hands)}): ')) - 1
        hands[player], hands[target] = hands[target], hands[player]
    else:
        draw_pile.append(card)

def get_winner(hands):
    # This function checks if any player has run out of cards and returns their index if they have.
    # If no player has run out of cards, it returns None.
    for i, hand in enumerate(hands):
        if not hand:
            return i
    return None

def main():
    # This is the main function of the game.
    # It initializes the players and hands, and then enters a loop that gets moves from the players
    # and checks if anyone has won the game.
    # The game continues until either player runs out of cards or the draw pile is empty.
    num_players = int(input('Enter the number of players: '))
    num_cards = int(input('Enter the number of cards per player: '))
    hands = deal_cards(num_players, num_cards)
    draw_pile = []
    current_player = 0
    while True:
        print(f'Player {current_player+1} hand: {hands[current_player]}')
        print(f'Draw pile: {len(draw_pile)} cards')
        choice = input(f'Player {current_player+1}, [d]raw or [p]lay a card: ')
        if choice == 'd':
            hands[current_player].append(draw_pile.pop())
        else:
            card = int(input(f'Player {current_player+

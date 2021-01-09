from card import Card
from values import values
from deck import Deck
from player import Player


def game():

    player_one = Player('One')
    player_two = Player('Two')

    new_deck = Deck()
    new_deck.shuffle()

    for _ in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    is_game_over = False

    round_num = 0

    while not is_game_over:

        round_num += 1
        print(f'Round {round_num}')

        if len(player_one.all_cards) == 0:
            print('Player one is out of cards. Player Two wins!')
            is_game_over = True
            break
        elif len(player_two.all_cards) == 0:
            print('Player two is out of cards. Player One wins!')
            is_game_over = True
            break

        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        is_at_war = True

        while is_at_war:

            card_one = player_one_cards[-1].value
            card_two = player_two_cards[-1].value

            # Player one wins
            if card_one > card_two:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                is_at_war = False

            # Player two wins
            elif card_one < card_two:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                is_at_war = False

            else:
                print('WAR')

                if len(player_one.all_cards) < 3:
                    print('Player One unable to declare war')
                    print('Player Two wins')
                    is_game_over = True
                    break

                elif len(player_two.all_cards) < 3:
                    print('Player Two unable to declare war')
                    print('Player One wins')
                    is_game_over = True
                    break

                else:
                    for _ in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())


if __name__ == '__main__':
    game()

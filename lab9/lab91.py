import random


def blackjack(num_of_players):
    if num_of_players > 4 or num_of_players < 2:
        exit('Maximum of players is 4 and minimum is 2')
    blackjack_dictionary = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': [11, 1]
    }
    # creating deck of cards
    cards = []
    for key in blackjack_dictionary:
        cards += [key] * 4
    # shuffle cards
    random.shuffle(cards)

    # creating players
    players = {}
    for i in range(0, num_of_players):
        # player = [] - array with cards he or she has
        players['Player ' + str(i + 1)] = []
    # starting game
    game = True
    stoped_players = 0
    num_of_stoped_players = []  # players whose said stop -> have no chance to take one more card
    isWinner = False
    sums = {}  # sums of players' cards

    while game:
        for player in list(players):
            if player in num_of_stoped_players:
                continue
            player_cards = players[player]
            print(player, ' : ')
            choice = input('1. One more card\n2. Skip\n3. Stop\n')
            if choice == '1':
                # adding card to player cards
                player_cards += cards.pop()
                # counting sum of cards if it's less then 21
                player_cards_sum = 0
                for card in player_cards:
                    # if card is A
                    if isinstance(blackjack_dictionary[card], list):
                        # taking first grater value
                        player_cards_sum += blackjack_dictionary[card][0]
                        # if it's sum > 21 then remove this value(11) from sum and add less one (1)
                        if player_cards_sum > 21:
                            player_cards_sum -= blackjack_dictionary[card][0]
                            player_cards_sum += blackjack_dictionary[card][1]
                            # if anyway sum is grater then 21 , so player lost
                            if player_cards_sum > 21:
                                print(player_cards)
                                print(player, 'Bust!!!')
                                players.pop(player)
                        if player_cards_sum == 21:
                            print(player_cards)
                            print(player, 'WINS!!!')
                            isWinner = True
                            game = False
                            break
                    else:
                        player_cards_sum += blackjack_dictionary[card]
                        if player_cards_sum > 21:
                            print(player_cards)
                            print(player, 'Bust!!!')
                            players.pop(player)
                        elif player_cards_sum == 21:
                            print(player_cards)
                            print(player, 'WINS!!!')
                            isWinner = True
                            game = False
                            break

                    sums[player] = player_cards_sum

            elif choice == '2':
                pass
            elif choice == '3':
                stoped_players += 1
                num_of_stoped_players.append(player)
            else:
                pass
            # if everyone said stop -> game will end
            if stoped_players == num_of_players:
                game = False
            if len(players) == 1:
                print(players[next(iter(players))])
                print(next(iter(players)), 'WINS!!!')
                isWinner = True
                game = False
                break
            print(players)

    if not isWinner:
        winner = next(iter(sums))
        biggest_sum = sums[next(iter(sums))]
        for player in sums:
            if sums[player] > biggest_sum:
                biggest_sum = sums[player]
                winner = player
        print('Score', biggest_sum)
        print('Winner', winner)


number_of_players = int(input('Enter number of players(max:4): '))
blackjack(number_of_players)

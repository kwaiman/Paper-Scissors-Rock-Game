#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# Assign intital score to players; later can be used to count the updated score
    def __init__(self):
        self.score = 0


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
# Define an answer variable and assign an empty string; used later
# to store human player's answer
        self.answer = ''

    def move(self):
        self.answer = input('Rock, paper, scissors? >\nto end this game right'
                            ' now, type quit.\n').lower()
        while (self.answer != 'rock' and self.answer != 'paper' and
               self.answer != 'scissors' and self.answer != 'quit'):
            self.answer = input('Rock, paper, scissors? >\nto end this game '
                                'right now, type quit.\n').lower()
        return self.answer


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        # Set the initial move to be random (since in Round 0, there is no
        # previous move)
        if game.round == 0:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        # Set the initial move to be random (since in Round 0, there is no
        # previous move)
        if game.round == 0:
            return random.choice(moves)
        else:
            if self.my_move == 'rock':
                return 'paper'
            elif self.my_move == 'paper':
                return 'scissors'
            elif self.my_move == 'scissors':
                return 'rock'


# List of computer player types, used later for human player to choose
players_list = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
# Set the initial round number to 0, used later to count number of rounds
        self.round = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
# If human player typed 'quit', get out of this function immediately
# with the return code
        if move1 == 'quit':
            return
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print('** TIE **')
        elif beats(move1, move2):
            print('** PLAYER ONE WINS **')
            self.p1.score += 1
        else:
            print('** PLAYER TWO WINS **')
            self.p2.score += 1
        print('Score: Player One ' + str(self.p1.score) + ', Player Two ' +
              str(self.p2.score))

    def play_game(self):
        print("Game start!\nRock Paper Scissors, Go!\n")
        print('The player who is ahead by 4 points will win!')
        while (abs(player1.score - player2.score) < 4):
            print(f"Round {game.round}:")
            self.play_round()
# If human player quits, get out of this loop
            if player1.answer == 'quit':
                break
            game.round += 1
        if player1.answer != 'quit':
            if player1.score > player2.score:
                print('Player One WINS!!!')
                print('Congratulations!')
            else:
                print('Player Two WINS!!!')
                print('Better luck next time:(')
        else:
            print('Hope you will play for longer next time:)')
        print('FINAL Score: Player One ' + str(self.p1.score) +
              ', Player Two ' + str(self.p2.score))
        print("Thank you for playing!!\nGame over!")


if __name__ == '__main__':
    # Assign player objects to variables, so that later can have access to
    # and use the properties/information of the player objects
    player1 = HumanPlayer()
    # Ask human player to select the computer player
    player_type = input('Choose the type of player to play againt: '
                        '1. RandomPlayer, 2. ReflectPlayer, or '
                        '3. CyclePlayer\nType 1, 2, or 3. ')
    while (player_type != '1' and player_type != '2' and player_type != '3'):
        player_type = input('Choose the type of player to play againt: '
                            '1. RandomPlayer, 2. ReflectPlayer, or '
                            '3. CyclePlayer\nType 1, 2, or 3. ')
    player2 = players_list[int(player_type)-1]
    game = Game(player1, player2)
    game.play_game()

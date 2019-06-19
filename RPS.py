#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(self, one, two):
    return((one == 'rock' and two == 'scissors') or
           (one == 'scissors' and two == 'paper') or
           (one == 'paper' and two == 'rock'))


class Player:

    def move(self):
        return moves

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        pick = input(""" Pick One Of them ['rock, paper, scissors'] or
        """  """ To exist press x\n""")
        pick = pick.lower()
        while pick not in moves and pick != 'x':
            pick = input("Enter a valid move! ")
        if pick == 'x':
            print("Thanks For Playing")
            exit()
        return pick

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.x = 1

    def move(self):
        if (self.x == 1):
            self.x += 1
            return 'rock'
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        if (self.x > 1):
            self.x += 1
            self.my_move = my_move
            self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.x = 1

    def move(self):
        if(self.x == 1):
            self.x += 1
            return 'rock'
        elif(self.x == 2):
            self.x += 1
            return 'Paper'
        elif(self.x == 3):
            self.x -= 2
            return 'Scissors'


class Game:
    def __init__(self, HumanPlayer, RandomPlayer):
        self.p1 = HumanPlayer
        self.p2 = RandomPlayer
        self.count_win = 0
        self.count_loss = 0
        self.count_tie = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(self, move1, move2):
            self.count_win += 1
            print(f"wins:{self.count_win}")
        elif move1 == move2:
            self.count_tie += 1
            print(f"ties:{self.count_tie}")
        elif beats(self, move2, move1):
            self.count_loss += 1
            print(f"losses:{self.count_loss}")

        self.score1 = self.count_win
        self.score2 = self.count_win
        print(f"player One Score :{self.count_win}")
        print(f"player Two Score ;{self.count_loss}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        limit = 3
        print("Game start!")
        for round in range(limit):
            print(f"Round {round}:")
            self.play_round()
            if self.count_win > self.count_loss:
                print("Player 1 is winer%")
            elif self.count_win < self.count_loss:
                print("Player 2 is winer%\n")
            else:
                print("No one are win\n")
            print("THE FINAL SCORES ARE " + str(self.count_win) +
                  " To " + str(self.count_loss))
        print("Game over!")
        choo = input("if you want to continue press y or quit x\n ")
        while choo is not 'y' and choo is not 'x':
            choo = input("invalid input....try agin\n")
        if choo == 'y':
            print("good choose ")
            self.play_game()
        elif choo == 'x':
            print("goodby")
            exit()
        return choo

if __name__ == '__main__':
    strategies = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }

    user_input = input("select the player strategy"
                       "you want to play aginst\n"
                       "1- Rock Player\n"
                       "2- Random Player\n"
                       "3- Cycle Player\n"
                       "4- Reflect Player\n")
    if user_input == "1":
        game = Game(HumanPlayer(), Player())
        game.play_game()
    elif user_input == "2":
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif user_input == "3":
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
    else:
        game = Game(HumanPlayer(), ReflectPlayer()) 
        game.play_game()    
        

     



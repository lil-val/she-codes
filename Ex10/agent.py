'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import random

class Agent:
    def getMove(self, moves_other, moves_self):
        pass


class InstructorAgent(Agent):
    def __init__(self):
        p_rock = random.random()
        p_scissors = random.random()
        p_paper = random.random()
        p_total = p_rock + p_scissors + p_paper

        self.p_rock = p_rock / p_total
        self.p_scissors = self.p_rock + p_scissors / p_total

    def getMove(self, moves_other, moves_self):
        random_move = random.random()
        if random_move < self.p_rock:
            return 'r'
        elif random_move < self.p_scissors:
            return 's'
        else:
            return 'p'


class MyAgent(Agent):
    def getMove(self, moves_other, moves_self):

        # YOUR CODE HERE

        counter_r = moves_other.count('r')
        counter_p = moves_other.count('p')
        counter_s = moves_other.count('s')
        if counter_r > counter_p and counter_r > counter_s:
            return 'p'
        if counter_p > counter_r and counter_p > counter_s:
            return 's'
        if counter_s > counter_p and counter_s > counter_r:
            return 'r'


class HumanAgent(Agent):
    def getMove(self, moves_other, moves_self):

        # YOUR CODE HERE
        valid_input = False
        human_input = ''
        while not valid_input:
            human_input = input('please choose r for rock, p for paper or s for scissors: ')
            if human_input != 'r' and human_input != 'p' and human_input != 's':
                print('invalid input!')
                valid_input = True
        return human_input


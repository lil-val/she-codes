'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''
import Ex10.agent as agent

class Game:
    def __init__(self, agent1, agent2):
        self.moves_a1 = []
        self.moves_a2 = []
        self.nround = 0
        self.score_a1 = 0
        self.score_a2 = 0

        self.agent1 = agent1
        self.agent2 = agent2

    def round(self):
        print('Round {}: '.format(self.nround+1))
        # we pass along history so a player can take that into account when
        # deciding the next move
        move_a1 = self.agent1.getMove(self.moves_a2, self.moves_a1)
        move_a2 = self.agent2.getMove(self.moves_a1, self.moves_a2)

        # compare the moves and decide who wins
        outcome = self.compare(move_a1, move_a2)

        # output outcome of current round
        if outcome == 1:
            self.score_a1 += 1
            print('Player 1 wins: {} beats {}'.format(move_a1, move_a2))
        elif outcome == 0:
            print('This round is tied, both players played {}'.format(move_a1))
        else:
            self.score_a2 += 1
            print('Player 2 wins: {} beats {}'.format(move_a2, move_a1))

        # update scores

        # YOUR CODE HERE (see above, part of outcome)

        self.moves_a1.append(move_a1)
        self.moves_a2.append(move_a2)

    def play(self, nrounds):
        for r in range(nrounds):
            self.round()
            self.nround += 1

    def summary(self):
        # print some summary of the games
        print('='*20)
        if self.score_a1 > self.score_a2:
            print('Player 1 wins')
        elif self.score_a1 < self.score_a2:
            print('Player 2 wins')
        else:
            print('The game ends in a tie')

        print('Final score: {} - {}'.format(self.score_a1, self.score_a2))

        # To implement: find the move that was played most often

        # YOUR CODE HERE
        counter_r = self.moves_a1.count('r') + self.moves_a2.count('r')
        counter_p = self.moves_a1.count('p') + self.moves_a2.count('p')
        counter_s = self.moves_a1.count('s') + self.moves_a2.count('s')
        result = None
        if counter_r > counter_p and counter_r > counter_s:
            result = 'r'
        if counter_p > counter_r and counter_p > counter_s:
            result = 'p'
        if counter_s > counter_p and counter_s > counter_r:
            result = 's'
        print('Most played move: {}'.format(result))
        print('='*20)

    def compare(self, move1, move2):
        # returns 1 if move1 wins, 0 if it's a tie, and -1 if move2 wins

        # YOUR CODE HERE
        if move1 == move2:
            return 0
        if (move1 == 'r' and move2 == 's') or (move1 == 'p' and move2 == 'r') or (move1 == 's' and move2 == 'p'):
            return 1
        else:
            return -1


game = Game(agent.InstructorAgent(), agent.MyAgent())
game.play(100)
game.summary()

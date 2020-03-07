import gym_tetris
from gym_tetris.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace

from action import Action
import numpy as np

from util import score_board, parse_blocks


class Model:
    def __init__(self, genes):
        self.genes = genes

    def rank(self, board):
        weights = score_board(board)
        return np.dot(self.genes, weights)

    def best(self, boards):
        min_score = score_board(boards[0])
        best_board_index = 0
        for x in range(1, len(boards)):
            score = self.rank(boards[x])
            if score < min_score:
                min_score = score
                best_board_index = x

        return best_board_index



class Population:
    def __init__(self, size: int):
        self.size = size
        self.gen = 0
        self.models = []
        for x in range(size):
            self.models.append(Model(np.random.rand(5)))

    def iterate(self):
        self.gen += 1

        # Perform selection
        self.rank()

        # Perform crossover


        # Perform mutation


    def rank(self):
        for model in self.models:
            env = gym_tetris.make('TetrisA-v0')
            env = JoypadSpace(env, SIMPLE_MOVEMENT)
            env.reset()
            done = False
            info = None

            while not done:
                # Generate all options
                options = [[Action.DROP]]
                for x in range(1, 5):
                    left_option = [Action.LEFT] * x
                    left_option.append(Action.DROP)
                    options.append(left_option)
                    right_option = [Action.RIGHT] * x
                    right_option.append(Action.DROP)
                    options.append(right_option)

                # Enumerate all choices
                boards = []
                for option in options:
                    # Back-up the environment first
                    env.unwrapped._backup()

                    # Run the sequence of actions
                    state = None
                    for action in option:
                        state, _, _, _ = env.step(action.value)

                    # Now, parse the board from the state
                    board = parse_blocks(state)
                    boards.append(board)
                    env.unwrapped._restore()

                # Choose the best option genetically
                choice = model.best(boards)
                for action in options[choice]:
                    _, _, done, info = env.step(action.value)

            model.fitness = info['score']

        self.models = sorted(self.models, key=lambda model: model.fitness)


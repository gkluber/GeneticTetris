from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import SIMPLE_MOVEMENT
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from action import Action
from model import Population
from util import parse_blocks

num_generations = 10
init_pop_size = 20
max_pop_size = 100

pop = Population(init_pop_size)

for gen in range(num_generations):
    pop.iterate()

    '''if done:
        state = env.reset()

    state, reward, done, info = env.step(env.action_space.sample())

    # Parse input
    piece = info['current_piece']
    nlines = info['number_of_lines']
    score = info['score']
    next_piece = info['next_piece']
    stats = info['statistics']
    bheight = info['board_height']
    blocks = parse_blocks(state)

    # Crop the board so that we don't see the pending piece
    blocks = blocks[(len(blocks) - bheight):len(blocks)]

    # Can always just drop from the initial condition
    options = [[Action.DROP]]
    for x in range(1, 5):
        options.append([[Action.LEFT] * x, Action.DROP])
        options.append([[Action.RIGHT] * x, Action.DROP])

    for option in options:
        pass



    #plt.imsave('raw-board{}'.format(step), state[47:209, 95:176], format='png')

    #env.render()'''

#env.close()
import math

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage.measure
import numpy as np


def draw_array(arr):
    plt.imshow(arr)
    plt.show()


def parse_blocks(raw_state, ind = 1):
    cropped = raw_state[48:208, 95:175]
    blocks = skimage.measure.block_reduce(cropped, (8,8,3), np.max)
    blocks = np.squeeze(blocks, axis=2)
    return blocks

def score_board(blocks):
    # Count number of gaps
    num_gaps = 0
    for y in range(len(blocks)):
        for x in range(len(blocks[y])):
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            neighbors = 0
            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]
                if nx < 0 or ny < 0 or nx >= len(blocks[y]) or ny >= len(blocks):
                    neighbors += 1
                else:
                    if blocks[ny][nx] != 0:
                        neighbors += 1

            if neighbors == 4:
                num_gaps += 1


    # Compute heights
    heights = np.zeros(len(blocks[0]))
    for x in range(len(blocks[0])):
        # Start at the top of the board; as soon as we find a block, we're done
        for y in range(len(blocks)):
            if blocks[y][x] != 0:
                heights[x] = len(blocks[0]) - y - 1

    mean_height = np.mean(heights)
    stddev_height = np.std(heights)
    diff_height = np.max(heights) - np.min(heights)

    # Compute the maximum difference between conseq. columns
    diffs = np.ediff1d(heights)
    max_diff = np.abs(diffs).max()

    return np.array([num_gaps, mean_height, stddev_height, diff_height, max_diff])

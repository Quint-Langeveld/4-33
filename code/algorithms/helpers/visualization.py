import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
import numpy as np
from matplotlib.colors import ListedColormap
import copy
import sys

def visualization(fields):
    """
    Function that visualizes a solution.
    fields: [fiels_as_string]
    return: plotted field
    """

    # copying the startfield
    for field in fields:
        print_field = divide(field)

        # Describing all possible colors for the cars
        all_colors = ['w', 'k', 'r',
                        'green', 'blue', 'magenta',
                        'cyan', 'purple', 'orange',
                        'yellow', 'lime', 'indigo',
                        'violet', 'gray', 'pink',
                        'brown',
                        ]

        list_ids = []
        for i, row in enumerate(print_field):
            for j, cell in enumerate(row):
                if isinstance(cell, int):
                    list_ids.append(cell)
                elif cell == 'R':
                    print_field[i][j] = 2

        colors_needed = len(list_ids) + 3

        # padding around the field
        field = np.pad(print_field, ((1,1), (1,1)), 'constant', constant_values = 1)
        field[(len(field) - 1) // 2][len(field) - 1] = 0


        colors = all_colors[0: colors_needed]
        cmp = ListedColormap(colors)
        plt.matshow(field, cmap=cmp)
        # close and show, thereby creating a movie
        # plt.show(block=True)
        plt.pause(0.25)
        plt.close()
        plt.show()

def divide(field):
    """
    Function that processes a field for visualizing.
    field: field as string
    return: outfield
    """
    print_field = copy.deepcopy(field)
    print_field = print_field.split("\n")
    for i, line in enumerate(print_field):
        line = line.split(" ")
        line.pop()
        print_field[i] = line
    print_field.pop()
    out_field = [[0 for i in range(len(print_field))] for n in range(len(print_field))]
    for i, row in enumerate(print_field):
        for j, cell in enumerate(row):
            if not cell[0].isdigit():
                if cell[0] == 'R':
                    out_field[i][j] = 'R'
                elif cell[0] == 'E':
                    out_field[i][j] = 0
            else:
                if len(cell) == 3:
                    id = cell[0]
                    out_field[i][j] = int(id)
                else:
                    id = cell[:2]
                    out_field[i][j] = int(id)
    return out_field

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
import numpy as np
from matplotlib.colors import ListedColormap
import copy
import sys

def visualization(field):


    # copying the startfield
    print_field = divide(field)

    # Describing all possible colors for the cars
    all_colors = ['w', 'k', 'r',
                    'green', 'blue', 'magenta',
                    'cyan', 'purple', 'orange',
                    'yellow', 'lime', 'indigo',
                    'violet', 'gray', 'pink',
                    'brown'
                    ]

    list_ids = []
    for i, row in enumerate(print_field):
        for j, cell in enumerate(row):
            if isinstance(cell, int):
                list_ids.append(cell)
            elif cell == 'R':
                print_field[i][j] = 10

    colors_needed = len(list_ids) + 3

    # padding around the field
    field = np.pad(print_field, ((1,1), (1,1)), 'constant', constant_values = 1)
    field[(len(field) - 1) // 2][len(field) - 1] = 0


    colors = all_colors[0: colors_needed]
    cmp = ListedColormap(colors)
    plt.matshow(field, cmap=cmp)
    # close and show, thereby creating a movie
    # plt.show(block=True)
    plt.pause(0.000000001)
    plt.close()
    plt.show()

def divide(field):

    print_field = copy.deepcopy(field)
    out_field = [[0 for i in range(len(print_field))] for n in range(len(print_field))]
    for i, row in enumerate(print_field):
        # print_field[i] = [line.strip() for line in print_field.split(',')]
        for j, cell in enumerate(row):
            if not cell.id[0].isdigit():
                if cell.id[0] == 'R':
                    out_field[i][j] = 'R'
                elif cell.id[0] == 'E':
                    out_field[i][j] = 0
            else:
                if len(cell.id) == 3:
                    id = cell.id[0]
                    out_field[i][j] = int(id)
                else:
                    id = cell.id[:2]
                    out_field[i][j] = int(id)
    return out_field
#
#
if __name__ == '__main__':
    #field = [
    #    ["1V3", "2H2", "2H2", "3H2", "3H2", "E"],
    #    ["1V3", "4V2", "5H2", "5H2", "6H2", "6H2"],
    #    ["1V3", "4V2", "7H2", "RH2", "RH2", "8V2"],
    #    ["9V2", "10V2", "7H2", "11H2", "11H2", "8V2"],
    #    ["9V2", "10V2", "12H2", "12H2", "13H2", "13H2"],
    #    ["14V3", "14V3", "14V3", "15H3", "15H3", "15V3"],
            ]
    visualization(field)

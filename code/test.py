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
    print(print_field)
    # print_field = copy.deepcopy(field)
    #
    # #field_data = print_field.readlines()
    # for i, line in enumerate(print_field):
    #     print_field[i] = [line.strip() for line in print_field.split(',')]
    #     new_field = []
    # for row in print_field:
    #     new_field_row = []
    #     for cell in row:
    #         if cell == "E":
    #             new_field_row.append(Cell(cell = 0))
    #         if cell != "E":
    #             new_field_row.append(Cell(cell + 1))
    #     new_field.append(new_field_row)

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
        # print_field[i] = [line.strip() for line in print_field.split(',')]
        for j, cell in enumerate(row):
            if isinstance(cell, int):
                list_ids.append(cell)
            elif cell == 'R':\
                print_field[i][j] = 10

    colors_needed = len(list_ids) + 3
    print()
    # print(print_field)

    # for i in range(len(field)):
    #     for j in range(len(field[i])):
    #         if field[i][j] == "E":
    #             field[i][j] = 0
    #         elif field[j][0] != "E":
    #             field[i][j] = i + 2


    # padding around the field
    field = np.pad(print_field, ((1,1), (1,1)), 'constant', constant_values = 1)
    field[(len(field) - 1) // 2][len(field) - 1] = 0


    # Replacing cell objects in the field with integers to link them to the cars
    # color_id = []
    # for x, style in enumerate(field):
    #        if style == "1H2" or style == "2V1":
    #            color_id.append(style[0])


    print(field)
    colors = all_colors[0: colors_needed]
    cmp = ListedColormap(colors)
    plt.matshow(field, cmap=cmp)
    # close and show, thereby creating a movie
    # plt.show(block=True)
    # plt.pause(0.000001)
    # plt.close()
    plt.show()

def divide(field):

    print_field = copy.deepcopy(field)
    out_field = [[0 for i in range(len(print_field))] for n in range(len(print_field))]
    for i, row in enumerate(print_field):
        # print_field[i] = [line.strip() for line in print_field.split(',')]
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
    print(out_field)
    return out_field

        # new_field = []
        # for row in print_field:
        #     new_field_row = []
        #     for cell in row:
        #         if cell == "E":
        #             new_field_row.append(Cell(cell = 0))
        #             if cell != "E":
        #                 new_field_row.append(Cell(cell + 1))
        # new_field.append(new_field_row)




if __name__ == '__main__':
    field = [
        ["8V3", "7H3", "7H3", "7H3", "6H2", "6H2"],
        ["8V3", "1H3", "1H3", "1H3", "E", "2V2"],
        ["8V3", "3V3", "E", "RH2", "RH2", "2V2"],
        ["9V2", "3V3", "E", "E", "E", "E"],
        ["9V2", "3V3", "9H2", "9H2", "5H2", "5H2"],
        ["E", "E", "4H3", "4H3", "4H3", "E"],
            ]
    visualization(field)

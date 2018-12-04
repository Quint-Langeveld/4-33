import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
import numpy as np
from matplotlib.colors import ListedColormap


def visualization():


    # copying the startfield
    field = [
        ["8V3", "7H3", "7H3", "7H3", "6H2", "6H2"],
        ["8V3", "1H3", "1H3", "1H3", "E", "2V2"],
        ["8V3", "3V3", "E", "RH2", "RH2", "2V2"],
        ["9V2", "3V3", "E", "E", "E", "E"],
        ["9V2", "3V3", "9H2", "9H2", "5H2", "5H2"],
        ["E", "E", "4H3", "4H3", "4H3", "E"],
            ]

    print_field = copy.deepcopy(field)

    field_data = print_field.readlines()
    for i, line in enumerate(field_data):
        field_data[i] = line.strip().split()
    for row in field_data:
        for cell in row:
            if cell == "E":
                cell = 0
            else:
                cell += 1





    # Describing all possible colors for the cars
    # all_colors = ['w', 'k', 'r',
                    # 'green', 'blue', 'magenta',
                    # 'cyan', 'purple', 'orange',
                    # 'yellow', 'lime', 'indigo',
                    # 'violet', 'gray', 'pink',
                    # 'brown'
                    # ]

    # for i in range(len(field)):
    #    for j in range(len(field[i])):
    #        if field[i][j] == "E":
    #            field[i][j] = 0
    #        else:
    #            field[i][j] = i + 1


    # padding around the field
    field = np.pad(field, ((1,1), (1,1)), 'constant', constant_values = 1)


    # Replacing cell objects in the field with integers to link them to the cars
    #color_id = []
    #for x, style in enumerate(field):
    #        if style == "1H2" or style == "2V1":
    #            color_id.append(style[0])


    # colors = all_colors[0: (len(color_id) + 2)]
    # cmp = ListedColormap(colors)
    print(field)
    plt.matshow(field)
    plt.show()

if __name__ == '__main__':
    visualization()

import copy

row0 = ["E", "E", "E", "E", "E", "E"]
row1 = ["E", "E", "ah2", "ah2", "E", "bv2"]
row2 = ["E", "E", "E", "rh2", "rh2", "bv2"]
row3 = ["E", "cv2", "E", "E", "E", "E"]
row4 = ["E", "cv2", "E", "E", "E", "E"]
row5 = ["E", "E", "dh3", "dh3", "dh3", "E"]
field = [row0, row1, row2, row3, row4, row5]
fields = [field]
# for field in fields:
for i, row in enumerate(field):
    for j in range(len(row)):
        if row[j] == row[j - 1]:
            continue
        vakje = row[j]
        if vakje != "E":
            if vakje[1] == "h":
                if vakje[2] == "2":
                    for k in range(1, 5):
                        if j - k >= 0 and row[j - k] == "E":
                            new_field = copy.deepcopy(field)
                            new_field[i][j - k] = vakje
                            new_field[i][j - k + 1] = vakje
                            new_field[i][j - k + 2] = "E"
                            if k >= 2:
                                for l in range(k - 1):
                                    print("l:", l)
                                    new_field[i][j - k + 3 + l] = "E"
                            fields.append(new_field)
                        if j + k <= 5 and row[j + k] == "E":
                            new_field = copy.deepcopy(field)
                            new_field[i][j + k] = vakje
                            new_field[i][j + k - 1] = vakje
                            new_field[i][j + k - 2] = "E"
                            if k >= 2:
                                for l in range(k - 1):
                                    new_field[i][j + k - 3 - l] = "E"
                            fields.append(new_field)
                else: # if vakje[2] == "3"
                    for k in range(1, 5):
                        if j - k >= 0 and row[j - k] == "E":
                            new_field = copy.deepcopy(field)
                            new_field[i][j - k] = vakje
                            new_field[i][j - k + 1] = vakje
                            new_field[i][j - k + 2] = vakje
                            for l in range(3, 5):
                                index_to_check = j - k + l
                                if index_to_check <= 5 and new_field[i][index_to_check] == vakje:
                                    new_field[i][index_to_check] = "E"
                            fields.append(new_field)
                        if j + k <= 5 and row[j + k] == "E":
                            new_field = copy.deepcopy(field)
                            new_field[i][j + k] = vakje
                            new_field[i][j + k - 1] = vakje
                            new_field[i][j + k - 2] = vakje
                            for l in range(3, 5):
                                index_to_check = j + k - l
                                if index_to_check >= 0 and new_field[i][index_to_check] == vakje:
                                    new_field[i][index_to_check] = "E"
                            fields.append(new_field)

for field in fields:
    for row in field:
        print(row)
    print("")

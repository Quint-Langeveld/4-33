def read_distribution(filename):
    """
    Function that processes a raw distribution file.
    filename: name of raw file
    return: distribution as dicitonary
    """
    distribution = {"0-50": 0, "51-100": 0, "101-200" : 0, "201-2000": 0, "2001-4000": 0, "4001-6000": 0, "6001-8000": 0, "8001 ->": 0}
    categories = [51,101, 201, 2001, 4001, 6001, 8001]
    keylist = list(distribution.keys())
    with open(filename, "r") as f:
        data = f.readlines()
        data[0] = data[0].strip(", \n")
        data = data[0].split(",")
        for i, data_item in enumerate(data):
            data[i] = data[i].split(":")
        for i, data_item in enumerate(data):
            for j, item in enumerate(data_item):
                data[i][j] = item.strip(" ")
        for item in data:
            if int(item[0]) >= categories[-1]:
                distribution[keylist[-1]] += int(item[1])
            else:
                item_placed = False
                for i, categorie in enumerate(categories):
                    if item_placed == False:
                        if int(item[0]) < categorie:
                            distribution[keylist[i]] += int(item[1])
                            item_placed = True
        return distribution

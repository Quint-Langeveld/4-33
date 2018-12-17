
def main():
    distribution = {"0-50": 0, "51-100": 0, "101-200" : 0, "201-2000": 0, "2001-4000": 0, "4001-6000": 0, "6001-8000": 0, "8001 ->": 0}
    categories = [51,101, 201, 2001, 4001, 6001, 8001]
    keylist = list(distribution.keys())
    print(keylist)
    filename = "field3_distribution.txt"
    with open(filename, "r") as f:
        data = f.readlines()
        data[0] = data[0].strip()
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


            # if int(item[0]) < 200:
            #     distribution["0-200"] += int(item[1])
            # elif int(item[0]) < 2000 and int(item[0]) > 200:
            #     distribution["200-2000"] += int(item[1])
            # elif int(item[0]) < 4000 and int(item[0]) > 2000:
            #     distribution["2000-4000"] += int(item[1])
            # elif int(item[0]) < 6000  and int(item[0]) > 4000:
            #     distribution["4000-6000"] += int(item[1])
            # elif int(item[0]) < 8000  and int(item[0]) > 6000:
            #     distribution["6000-8000"] += int(item[1])
            # else:
            #     distribution["8000 ->"] += int(item[1])

        print(distribution)






if __name__ == '__main__':
    main()

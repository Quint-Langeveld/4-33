import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from rush_hour import Rush_hour

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py startfield algorithm")
        sys.exit(1)
    startfield = sys.argv[1]
    algorithm = sys.argv[2]
    algorithms = ["breadthfirst", "itterative_deepening_depth_first", "random", "random_and_bound", "branch_and_bound"]
    if algorithm not in algorithms:
        print("Algorithm not supported, please try again")
        print("You can choose between the following:")
        for algorithm in algorithms:
            print(algorithm)
        sys.exit(1)
    rush_hour = Rush_hour(startfield)
    rush_hour.play(algorithm)

if __name__ == "__main__":
    main()

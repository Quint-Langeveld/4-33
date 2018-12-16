import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from classes.rush_hour import Rush_hour

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py startfield algorithm")
        sys.exit(1)
    startfield = sys.argv[1]
    algorithm = sys.argv[2]
    algorithms = ["breadthfirst", "random", "random_and_bound", "branch_and_bound"]
    if algorithm not in algorithms:
        print("Algorithm not supported, please try again")
        print("You can choose between the following:")
        for algorithm in algorithms:
            print(algorithm)
        sys.exit(1)
    iterations, bound = None, None
    if algorithm in ["random", "random_and_bound"]:
        iterations = int(input("How many iterations would you like to do?\n"))
    if algorithm in ["random_and_bound", "branch_and_bound"]:
        bound = int(input("What initial bound would you like to set?\n"))
    rush_hour = Rush_hour(startfield, iterations, bound)
    rush_hour.play(algorithm)

if __name__ == "__main__":
    main()

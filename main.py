import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))

from classes.rush_hour import Rush_hour

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py field#.txt algorithm")
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
    if algorithm == "breadthfirst":
        keep_track = input("Would you like to keep track of the moves made by algoritmh?\n"
                            "Default is NO, Use Yes for keeping track.\n"
                            "WARNING: THIS MAKE THE PROGRAM MUCH SLOWER\n")
        if keep_track.lowercase() in ["yes", "y"]:
            keep_track = True
        else:
            keep_track = False
    rush_hour = Rush_hour(startfield, iterations, bound, keep_track)
    rush_hour.play(algorithm)

if __name__ == "__main__":
    main()

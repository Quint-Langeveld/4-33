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
    keep_track = None
    visualization_wanted = None
    if algorithm in ["random", "random_and_bound"]:
        iterations = int(input("How many iterations would you like to do?\n"))
    if algorithm in ["random_and_bound", "branch_and_bound"]:
        bound = int(input("What initial bound would you like to set?\n"))
        visualization_wanted = ask_visualization()
    if algorithm == "breadthfirst":
        keep_track = input("Would you like to keep track of the moves made by algoritmh?\n"
                            "Default is NO, Use Yes for keeping track.\n"
                            "WARNING: THIS MAKE THE PROGRAM RUN SLOWER\n")
        if keep_track.lower() in ["yes", "y"]:
            keep_track = True
            visualization_wanted = ask_visualization()
        else:
            keep_track = False



    rush_hour = Rush_hour(startfield, iterations, bound, keep_track)
    rush_hour.play(algorithm, visualization_wanted)

def ask_visualization():
    visualization = input("\nWould you like to see a visualization of the best solution found "
                          "by the algorithm at the end of the program?\n"
                          "Default is YES, use No for not seeing visualization.\n"
                          "WARNING: YOU MIGHT NEED TO RUN WITH pythonw INSTEAD OF python\n")
    if visualization.lower() in ["no", "n"]:
        return False
    else:
        return True


if __name__ == "__main__":
    main()

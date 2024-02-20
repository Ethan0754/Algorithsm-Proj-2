###Ethan Pendergraft, Thi Huynh, Hunter Henderson###
import sys


def sorting():
    print("Select the sorting algorithm you want to test.")
    print("-------------------------")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Other Sort")
    print("5. Exit")
    print("Select a sorting algorithm (1-5):")


def case(algorithm):
    print("Case Scenarios for", algorithm)
    print("---------------")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit", algorithm, " test")
    print("Select the case (1-4):")


def results(small, medium, large, case):
    print("In", case, "case,")
    print("For N = 100, it takes ", small, " seconds")
    print("For N = 1000, it takes ", medium, " seconds")
    print("For N = 10000, it takes ", large, " seconds")


def main():

    # If this is gibberish, I do apologize. 
    algorithm = 1
    while(algorithm != "5"):
        sorting()
        algorithm = input()
        choice = 1

        while(choice != "4"):
    
            if (algorithm == "1"):
                case("Bubble Sort")
            elif (algorithm == "2"):
                case("Merge Sort")
            elif (algorithm == "3"):
                case("Quick Sort")
            elif (algorithm == "4"):
                case("Other Sort")
            elif (algorithm == "5"):
                print("Bye!")
                sys.exit()  
                
            choice = input()
            if(choice == "1"):
                # Call functions at these 0's to calculate times; small = sort(algorithm, choice, 100)
                small = 0
                medium = 0
                large = 0
                results(small, medium, large, "best")
                print("Do you want to input another N (Y/N)? ")
                again = input()
                while(again == "Y" or again == "y"):
                    print("What is the N? ")
                    chosenN = input()
                    time = 0  # time = sort(algorithm, choice, chosenN)
                    print("For N = ", chosenN, ", it takes ", time, " seconds")
                    print("Do you want to input another N (Y/N)? ")
                    again = input()
            elif(choice == "2"):
                small = 0
                medium = 0
                large = 0
                results(small, medium, large, "average")
                print("Do you want to input another N (Y/N)? ")
                again = input()
                while(again == "Y" or again == "y"):
                    print("What is the N? ")
                    chosenN = input()
                    time = 0  # time = sort(algorithm, choice, chosenN)
                    print("For N = ", chosenN, ", it takes ", time, " seconds")
                    print("Do you want to input another N (Y/N)? ")
                    again = input()
            elif(choice == "3"):
                small = 0
                medium = 0
                large = 0
                results(small, medium, large, "worst")
                print("Do you want to input another N (Y/N)? ")
                again = input()
                while(again == "Y" or again == "y"):
                    print("What is the N? ")
                    chosenN = input()
                    time = 0  # time = sort(algorithm, choice, chosenN)
                    print("For N = ", chosenN, ", it takes ", time, " seconds")
                    print("Do you want to input another N (Y/N)? ")
                    again = input()


main()

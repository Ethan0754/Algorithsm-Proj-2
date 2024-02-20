###Ethan Pendergraft, Thi Huynh, Hunter Henderson###


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
    print("Case Scenarios for ", algorithm)
    print("---------------")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit ", algorithm, " test")
    print("Select the case (1-4):")
    
def results(small, medium, large, case):
    print("In", case, "case,")
    print("For N = 100, it takes ", small, " seconds")
    print("For N = 1000, it takes ", medium, " seconds")
    print("For N = 10000, it takes ", large, " seconds")
    
    
    
    
    
def main():
    
    
    
    
    
    
    
    
    
    
    #If this is gibberish, I do apologize. I will deal with it later. I commented it out for now, it doesn't work yet.
    """algorithm = 1
    while(algorithm != 5):
        sorting()
        algorithm = input()
        if (algorithm == 1):
            case("Bubble Sort")
        elif (algorithm == 2):
            case("Merge Sort")
        elif (algorithm == 3):
            case("Quick Sort")
        elif (algorithm == 4):
            case("Other Sort")
        elif (algorithm == 5):
            print("Bye!")
            exit()#exit program, idk if this is the right function to call
    
        choice = input()
        if(choice == 1):
            small = 0#Call functions at these 0's to calculate times; small = sort(algorithm, choice, 100)
            medium = 0
            large = 0
            results(small, medium, large, "Best")
            print("Do you want to input another N (Y/N)? ")
            again = input()
            while(again == "Y" or again == "y"):
                print("What is the N? ")
                chosenN = input()
                time = 0#time = sort(algorithm, choice, chosenN)
                print("For N = ", chosenN, ", it takes ", time, " seconds")
                print("Do you want to input another N (Y/N)? ")
                again = input()
        elif(choice == 2):
            small = 0
            medium = 0
            large = 0
            results(small, medium, large, "Average")
            print("Do you want to input another N (Y/N)? ")
            again = input()
            while(again == "Y" or again == "y"):
                print("What is the N? ")
                chosenN = input()
                time = 0#time = sort(algorithm, choice, chosenN)
                print("For N = ", chosenN, ", it takes ", time, " seconds")
                print("Do you want to input another N (Y/N)? ")
                again = input()
        elif(choice == 3):
            small = 0
            medium = 0
            large = 0
            results(small, medium, large, "Worst")
            print("Do you want to input another N (Y/N)? ")
            again = input()
            while(again == "Y" or again == "y"):
                print("What is the N? ")
                chosenN = input()
                time = 0#time = sort(algorithm, choice, chosenN)
                print("For N = ", chosenN, ", it takes ", time, " seconds")
                print("Do you want to input another N (Y/N)? ")
                again = input()
        elif(choice == 4):
            return"""
   
main()



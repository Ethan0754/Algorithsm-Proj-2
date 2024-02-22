### Ethan Pendergraft, Thi Huynh, Hunter Henderson ###
import sys
import random
import time

def generateList(size):
    newList = []
    
    for i in range(size):
        x = random.randint(1, 10)
        newList.append(x)
    
    return newList

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


def bubblesort(myList):
    for i in range (len(myList) - 1):
        for j in range (len(myList) - i -1):
            if myList[j] > myList [j + 1]:
                myList[j], myList [j + 1] =\
                    myList[j + 1], myList[j]
    return myList
    
    
def quicksort(scenario):
    print("quicksort")
    
    
def mergesort(scenario):
    print("mergesort")
    
def othersort(scenario):
    print("othersort")

def fileprint(times):
    print("fileprint")
    
    
def genBestBubble(algorithm):
    print("worstcase")
    newList = []
    
    for i in range (100):
        newList.append(i)
    
    start = time.time()
    bubblesort(newList)
    end = time.time()
    n_hundred = end - start
    n_thou = 0
    n_tenthou = 0
    
    results(n_hundred, n_thou, n_tenthou, "Best Case")
        
    
def genAvgBubble():
    
    start = time.time()
    newList = generateList(100)
    bubblesort(newList)
    end = time.time()
    n_hundred = end - start
    
    start = time.time()
    newList = generateList(1000)
    bubblesort(newList)
    end = time.time()
    n_thou = end - start
        
    start = time.time()
    newList = generateList(10000)
    bubblesort(newList)
    end = time.time()
    n_tenthou = end - start
    
    small = n_hundred
    medium = n_thou
    large = n_tenthou
    
    results(small, medium, large, "average")
    
    
def generatebestcase(algorithm):
    print("bestcase")



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
                genAvgBubble()
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

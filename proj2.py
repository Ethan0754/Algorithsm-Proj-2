### Ethan Pendergraft, Thi Huynh, Hunter Henderson ###
import sys
import random
import time
from datetime import datetime

#----------------------------USER INTER FACE FUNCTIONS------------------------#
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
    # The first argument is the file name that it will be writing to,
    # and the second argument is the writing mode.
    # Here, "a" means append, meaning it will append the written lines
    # to the end of the file.
    # Source: https://www.geeksforgeeks.org/reading-writing-text-files-python/
    log_results = open("log_results.txt","a")
    
    # Uses imported datetime function to give the current date;
    # eg. 2024-02-23 18:45:03.159993
    # Source: https://www.programiz.com/python-programming/datetime/current-datetime
    current_time = datetime.now()
    
    # Prints the results to the console
    print("In", case, "case,")
    print("For N = 100, it takes ", small, " seconds")
    print("For N = 1000, it takes ", medium, " seconds")
    print("For N = 10000, it takes ", large, " seconds")
    
    # Writes the results to the log file
    # Here, the `write` function only takes in one argument; therefore,
    # I wrapped all the variables as strings so that it could perform
    # string concatenation.
    log_results.write("Results for " + str(case) + " Case on " + str(current_time) + "\n")
    log_results.write("---------------\n")
    log_results.write("In " + str(case) + " case,\n")
    log_results.write("For N = 100, it takes " + str(small) + " seconds\n")
    log_results.write("For N = 1000, it takes " + str(medium) + " seconds\n")
    log_results.write("For N = 10000, it takes " + str(large) + " seconds\n")
    log_results.write("---------------\n")
    log_results.write("End of Results for " + str(case) + " Case on " + str(current_time) + "\n")
    log_results.write("\n\n")
    
    # Confirms to the user that the results have been written to the log file
    print("The results have been logged into `log_results.txt` in the same directory as the script.")
    
    

#--------------------------------SORTING FUNCTIONS----------------------------#
def generateList(size):
    newList = []
    
    for i in range(size):
        x = random.randint(1, 10)
        newList.append(x)
    
    return newList

def bubblesort(myList):
    for i in range (len(myList) - 1):
        for j in range (len(myList) - i -1):
            if myList[j] > myList [j + 1]:
                myList[j], myList [j + 1] =\
                    myList[j + 1], myList[j]
    return myList
    

def merge_sort(myList):
    
    if len(myList) <= 1:
        return myList
    middle = len(myList) // 2
    left = myList[:middle]
    right = myList[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result
    
def quicksort(myList):
    print("quicksort")
    
def othersort(scenario):
    print("othersort")

def fileprint(times):
    print("fileprint")
    
#---------------------------RESULTS FUNCTIONS---------------------------------#
def genBestBubble():
    newList = []
    newList2 = []
    newList3 = []
    
  ##Here is what I changed##
    newList = generateList(100)
    merge_sort(newList)
    newList2 = generateList(1000)
    merge_sort(newList2)
    newList3 = generateList(10000)
    merge_sort(newList3)
    ##----------------------##

    
    start = time.time()
    bubblesort(newList)
    end = time.time()
    n_hundred = end - start
    

       
    start = time.time()
    bubblesort(newList2)
    end = time.time()
    n_thou = end - start
    

    start = time.time()
    bubblesort(newList3)
    end = time.time()
    n_tenthou = end - start
        
    results(n_hundred, n_thou, n_tenthou, "Best")
         
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
    
    results(small, medium, large, "Average")
    
def genWorstBubble():
    newList = []
    newList2 = []
    newList3 = []

    ##Here is what I changed##
    newList = generateList(100)
    merge_sort(newList)
    newList2 = generateList(1000)
    merge_sort(newList2)
    newList3 = generateList(10000)
    merge_sort(newList3)
    newList.reverse()
    newList2.reverse()
    newList3.reverse()
##---------------------##


    start = time.time()
    bubblesort(newList)
    end = time.time()
    n_hundred = end - start



    start = time.time()
    bubblesort(newList2)
    end = time.time()
    n_thou = end - start

   

    start = time.time()
    bubblesort(newList3)
    end = time.time()
    n_tenthou = end - start

    results(n_hundred, n_thou, n_tenthou, "Worst")
    
    
def genBestMerge():
    newlist = []
    newlist2 = []
    newlist3 = []
    
    for i in range (1000):
        newlist.append(i)
    
    start = time.time()
    mSort_hund = merge_sort(newlist)
    end = time.time()
    small = float (end - start)
    
    for i in range (10000):
        newlist2.append(i)
    
    start = time.time()
    mSort_thou = merge_sort(newlist)
    end = time.time()
    medium = end - start

    
    for i in range (100000):
        newlist3.append(i)
    
    start = time.time()
    mSort_tenthou = merge_sort(newlist)
    end = time.time()
    large = end - start

    
    results(small, medium, large, "Best")
    
def genWorstMerge():
    newlist = []
    newlist2 = []
    newlist3 = []
    
    for i in range (100):
        newlist.append(i)
    newlist.reverse()
    
    start = time.time()
    mSort_hund = merge_sort(newlist)
    end = time.time()
    small = end - start
    
    for i in range (1000):
        newlist2.append(i)
    newlist2.reverse()
    
    start = time.time()
    mSort_thou = merge_sort(newlist)
    end = time.time()
    medium = float(end - start)

    
    for i in range (10000):
        newlist3.append(i)
    newlist.reverse()
    
    start = time.time()
    mSort_tenthou = merge_sort(newlist)
    end = time.time()
    large = end - start
    
    results(small, medium, large, "Best")
    

        
def sort(choice, algorithm):
    
    if choice == '1':
        if algorithm == '1':
            genBestBubble()
        elif algorithm == '2':
            genBestMerge()
        elif algorithm == '2':
            print ('genbest quick')
        elif algorithm == '3':
            print ('gen best other')
    elif choice == '2':
        if algorithm == '1':
            genAvgBubble()
        elif algorithm == '2':
            print('gen avg merge')
        elif algorithm == '2':
            print ('gen avg quick')
        elif algorithm == '3':
            print ('genavg other')
    elif choice == '3':
        if algorithm == '1':
            genWorstBubble()
        elif algorithm == '2':
            genWorstMerge()
        elif algorithm == '2':
            print ('gen worst quick')
        elif algorithm == '3':
            print ('gen worst other')
            
#------------------------------MAIN (FRONT END)-------------------------------#
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
            brk_cond = int(choice)
            
            if brk_cond < 1 or brk_cond > 3:
                break
            
            sort(choice, algorithm)
            
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

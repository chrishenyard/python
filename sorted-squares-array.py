# import array

"""

Given a sorted array of integers from min to max, square them and return the results sorted
from min to max

"""

def SortedSquaresArray(x = [-10, -8, -3, -1, 4, 6, 12, 13]):

    sorted = ValidateArrayIsSorted(x)

    if sorted == False:
        raise Exception("Array is not sorted")

    sortedSquaredOutput = [0 for _ in range(len(x))]

    minIndex  = 0
    maxIndex = index = len(x) - 1

    for _ in range(len(x)):
        minValue = x[minIndex]
        maxValue = x[maxIndex]
        minValueSquared = minValue ** 2
        maxValueSquared = maxValue ** 2

        if minValueSquared >= maxValueSquared:
            sortedSquaredOutput[index] = minValueSquared
            minIndex += 1
        else:
            sortedSquaredOutput[index] = maxValueSquared
            maxIndex -= 1

        index -= 1

    return sortedSquaredOutput

def ValidateArrayIsSorted(array):
    flag = 0
    
    if(all(array[i] <= array[i + 1] for i in range(len(array)-1))): 
        flag = 1

    return flag


sortedSquaredOutput = SortedSquaresArray()


print(sortedSquaredOutput)


 





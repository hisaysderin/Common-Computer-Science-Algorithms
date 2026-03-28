def linearSearch(inputList, searchedItem):

    index = 0

    for item in inputList:          # Iterate through all items in the list

        if item == searchedItem:    # If we found the item...
            return index            # ...return the index, ending the function

        index += 1                  # Increment the index to keep track

    return -1                       # If we didn't find the item return -1


def binarySearch(inputList, searchedItem):

    first = 0                       # Pointer to the start of the considered list
    last = len(inputList) - 1       # Pointer to the end of the considered list
    middle = (last + first) // 2    # Middle of the considered list

    while (first != last):          # Whilst there is more than one item left...

        if inputList[middle] == searchedItem:       # If the middle is what we're looking for...
            return middle                           # ...return the middle
        
        elif inputList[middle] > searchedItem:      # If what we're looking for is before the middle...
            last = middle - 1                       # ...adjust the last pointer to the value before the middle

        elif inputList[middle] < searchedItem:      # If what we're looking for is after the middle...
            first = middle + 1                      # ...adjust the first pointer to the value after the middle

        middle = (last + first) // 2                # Recalculate the middle

    # When there is one item left...
    if inputList[middle] == searchedItem:           # ...check if it is what we're looking for...
        return middle
    else:
        return -1                                   # ...and if it isn't return -1


def mergeSort(inputList):
    
    print(inputList)

    if len(inputList) > 1:                          # Stop recursively dividing when the lists are size 1

        middle = len(inputList) // 2                # Get the middle of the list
        left = inputList[:middle]                   # Slice the list in two using the middle
        right = inputList[middle:]

        mergeSort(left)                             # Recursively divide the lists
        mergeSort(right)

        # After the lists have been divided, or earlier lists have been merged...

        mergedList = [None]*(len(left) + len(right))    # Create a new list with length the size of the left and right halves

        leftPointer = 0                                 # Create pointers used in merging process
        rightPointer = 0
        newListPointer = 0                              # This is used to add to the new list
        
        # While both lists still have elements...
        while leftPointer < len(left) and rightPointer < len(right):

            # If the left item is smaller...
            if left[leftPointer] < right[rightPointer]:
                mergedList[newListPointer] = left[leftPointer]      # ...add the left item...
                leftPointer += 1                                    # ...and increment the left pointer

            else:
                mergedList[newListPointer] = right[rightPointer]    # ...add the right item...
                rightPointer += 1                                   # ...and increment the right pointer

            newListPointer += 1                                     # Increment the new list pointer

        # In the case that the right list depletes first
        # This gets skipped if the left list is depleted
        while leftPointer < len(left):

            # Add all remaining left-list items
            mergedList[newListPointer] = left[leftPointer]
            leftPointer += 1
            newListPointer += 1

        # Exact same thing but for the right list
        while rightPointer < len(right):
            
            mergedList[newListPointer] = right[rightPointer]
            rightPointer += 1
            newListPointer += 1

        inputList[:] = mergedList                                   # replaces all items in the current input with the merged form

    return inputList


def quickSort(inputList, startIndex, endIndex):                     # startIndex and endIndex determine the scope of the recursion
                                                                    # At the start, startIndex = 0 and endIndex = length of the list - 1

    if startIndex >= endIndex:                                      # If the scope is 0 or under (i.e. recursion should stop)...
        return                                                      # ...return nothing and go back to the previous recursion

    else:
        pivot = inputList[startIndex]                               # Set the pivot to the first item in the list (rule can be changed)
        leftPointer = startIndex + 1                                # Create the left and right pointers
        rightPointer = endIndex

        doneSplitting = False                                       # Used to loop until we have sorted around the pivot

        while not doneSplitting:

            while leftPointer <= rightPointer and inputList[leftPointer] <= pivot:
                leftPointer += 1                                    # Move the left pointer right until it finds an item larger than the pivot...
                                                                    # ...or it has passed the right pointer

            while rightPointer >= leftPointer and inputList[rightPointer] >= pivot:
                rightPointer -= 1                                   # Move the right pointer left until it finds an item smaller than the pivot...
                                                                    # ...or it has passed the left pointer

            if leftPointer < rightPointer:                          # If the pointers have not crossed yet...
                temp = inputList[leftPointer]                       # Swap the left and right pointer values (using a temporary variable)
                inputList[leftPointer] = inputList[rightPointer]
                inputList[rightPointer] = temp

            else:                                                   # If the pointers have crossed...
                doneSplitting = True                                # ...stop looping...

        temp = inputList[startIndex]                                # ...and swap the pivot and right pointer value (using a temporary variable)
        inputList[startIndex] = inputList[rightPointer]
        inputList[rightPointer] = temp

        quickSort(inputList, startIndex, rightPointer-1)            # Perform the same algorithm on the two halves of the list
        quickSort(inputList, rightPointer+1, endIndex)

    return inputList                                                # After all valid recursions, end the program as the list is sorted

def bubbleSort():
    pass

def insertionSort():
    pass
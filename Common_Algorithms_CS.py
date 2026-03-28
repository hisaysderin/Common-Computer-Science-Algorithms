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


def quickSort(inputList):
    pass
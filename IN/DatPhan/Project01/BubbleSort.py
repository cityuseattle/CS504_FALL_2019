def bubble_sort(list, isAscending=True): # Added isAscending argument to determine whether the list should be sorted low to high or high to low.
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        for i in range(len(list) - 1):
            if ((isAscending and sorted_list[i] > sorted_list[i + 1]) or (not isAscending and sorted_list[i] < sorted_list[i + 1])): # Updated the expression to include the isAscending.
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = temp
                swaps += 1
                print(swaps)
        if swaps == 0:
            is_sorted = True
    return sorted_list

print(bubble_sort([2, 1, 3, 9, 8, 2, 5, 7, 1]))
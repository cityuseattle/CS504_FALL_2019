def bubble_sort(list, selectedOrder): #selectedOrder could be either 'lth' (low-to-high) or 'htl' (high-to-low)
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        if (str(selectedOrder) == "lth"): # low-to-high sorting
            for i in range(len(list) - 1):
                if sorted_list[i] > sorted_list[i + 1]: # swap
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swaps += 1
                    print(swaps)
        elif (str(selectedOrder) == "lth"): # high-to-low sorting
            for i in range(len(list) - 1):
                if sorted_list[i] < sorted_list[i + 1]: # swap
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swaps += 1
                    print(swaps)
        else: # for incorrect selectedOrder, user will be prompt with message.
            print("The second argument is incorrect!")
            print("Please select correct order. Either 'lth' for low to high sorting or 'htl' for high to low sorting.")
        if swaps == 0:
            is_sorted = True
    return sorted_list

print(bubble_sort([2, 3, 1], "lth"))  # result: [1, 2, 3] 
print(bubble_sort([2, 3, 1], "lth"))  # result: [3, 2, 1]
print(bubble_sort([2, 5, 0, -2, 3, 1, 6, 6, 7], "lth")) # result: [7, 6, 6, 5, 3, 2, 1, 0, -2] 
print(bubble_sort([2, 3, 1], "lth"))  # result: (message will be displayed)
print(bubble_sort([], "lth"))  # result: [] 

def list_comprehension(input_list):
    output_list = [item for item in input_list if item%2 == 0]
    print(output_list)
test_list = [1,2,3,4,4,5,6,7,7]
list_comprehension(test_list)
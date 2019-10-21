
backpack = ["book", "laptop", "pen", "banana", 2, True]
backpack.append("keys")

print(backpack)

backpack.insert(0, "charger")

print(backpack)

backpack.remove("book")
print(backpack)


def replace_negatives(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 0:
            numbers[i] = abs(numbers[i])

    return numbers


original = [33, 65, -12, 657, 0, -76]
print(replace_negatives(original))

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8]
even_numbers = [item for item in input_list if item % 2  == 0]
print(even_numbers)
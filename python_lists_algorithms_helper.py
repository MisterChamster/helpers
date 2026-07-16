## Traversal
## Counting
## Search
## Min/max
## Del duplicates
# Sort

# Filtering/mapping
# Aggregation (sum, avg, median, product)




# Traversal
if True:
    numbers = [7, 2, 9, 4]
    names = ["Alice", "Bob", "Charlie", "Dominicc"]

    for value in numbers:
        print(value)

    for i in range(len(numbers)):
        print(i, numbers[i])

    for i in range(len(numbers) - 1, -1, -1): # reverse
        print(numbers[i])

    for name, num in zip(names, numbers): # simultaneous
        print(name, num)


# Counting
if True:
    numbers = [4, 2, 4, 5, 4, 8]
    target = 4
    count = 0
    frequency = {}


    for _ in numbers: # Count el
        count += 1

    for value in numbers: # Count conditional
        if value == target:
            count += 1

    for value in numbers: # Count all occurances (to dict)
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1


# Search
if True:
    numbers = [1, 2, 4, 5, 7, 8, 10, 15]
    target = 8
    left = 0
    right = len(numbers) - 1

    while left <= right:     # one occurence, for SORTED!
        middle = (left + right) // 2

        if numbers[middle] == target:
            print("Found at index", middle)
            found = True
            break
        elif target < numbers[middle]:
            right = middle - 1
        else:
            left = middle + 1


# Min/max
if True:
    numbers = [12, 5, 18, 3, 9]
    minimum = numbers[0]
    maximum = numbers[0]

    for value in numbers[1:]:  # Min and max, single traversal
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value


# Del duplicates
if True:
    numbers = [4, 2, 4, 5, 2, 8, 5]
    result = []

    sorted_numbers = [2, 2, 4, 4, 4, 5, 8]
    sorted_result = [numbers[0]]
    write = 1

    consecutive_numbers = [1, 1, 2, 2, 3, 1, 1]
    consecutive_result = [numbers[0]]


    for value in numbers: #preserve order
        if value not in result:
            result.append(value)

    result = list(set(numbers))  #no order

    for value in sorted_numbers[1:]:    #for sorted, order
        if value != sorted_result[-1]:
            sorted_result.append(value)

    for value in consecutive_numbers[1:]:  # for consecutive
        if value != consecutive_result[-1]:
            consecutive_result.append(value)

    for read in range(1, len(sorted_numbers)):   # sorted, in place
        if sorted_numbers[read] != sorted_numbers[write - 1]:
            sorted_numbers[write] = sorted_numbers[read]
            write += 1
    del sorted_numbers[write:]


# Sort




# Filtering/mapping
if True:
    list(map(lambda x: x * 2, [1, 2, 3]))            # Mutate elements
                                                     # [2, 4, 6]
    list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) # Remove elements
                                                     # [2, 4]


# Aggregation (sum, avg, median, product)

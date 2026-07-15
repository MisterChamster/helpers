# Traversal
# Search
# Sort
# Min/max
# Count
# Del duplicates

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

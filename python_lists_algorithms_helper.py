## Filtering/mapping
## Traversal
## Counting
## Search
## Min/max
## Del duplicates
# Sort



# Filtering/mapping
if True:
    list(map(lambda x: x * 2, [1, 2, 3]))            # Mutate elements
                                                     # [2, 4, 6]
    list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) # Remove elements
                                                     # [2, 4]


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




# Sorting
# Bubble sort
# Time: n**2     Space: 1
def bubble_sort(numbers):
    # numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break

    return numbers

# Selection sort
# Time: n**2     Space: 1
def selection_sort(numbers):
    # numbers = numbers.copy()
    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers

# Insertion sort
# Time: n**2     Space: 1
def insertion_sort(numbers):
    # numbers = numbers.copy()

    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current

    return numbers

# Merge sort
# Time: n log n  Space: n
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick sort
# Time: n log n  Space: log n
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    smaller = []
    equal = []
    larger = []

    for value in numbers:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    return quick_sort(smaller) + equal + quick_sort(larger)

# Heap sort
# Time: n log n  Space: 1
def heap_sort(numbers):
    numbers = numbers.copy()
    n = len(numbers)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)

    # Extract largest element one by one
    for i in range(n - 1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, i, 0)

    return numbers

def heapify(numbers, heap_size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and numbers[left] > numbers[largest]:
        largest = left

    if right < heap_size and numbers[right] > numbers[largest]:
        largest = right

    if largest != root:
        numbers[root], numbers[largest] = numbers[largest], numbers[root]
        heapify(numbers, heap_size, largest)

# Timsort
# Time: n log n  Space: n
# Begins with quick sort but switches to heap sort if quick
# sort appears to be heading toward its worst-case behavior
numbers.sort()

# Counting sort
# Time: n + k    Space: k

# Radix sort
# Time: nk       Space: n+k

# Bucket sort
# Time: n + k    Space: n



# sequence[
    # start (inclusive):
    # stop (exclusive):
    # step]

example = "Anorexorcist"

print(example[3])     # r
print(example[-3])    # i

print(example[3:])    # rexorcist
print(example[-3:])   # ist

print(example[:3])    # Ano
print(example[:-3])   # Anorexorc

print(example[::1])   # Anorexorcist
print(example[::-1])  # tsicroxeronA
print(example[::3])   # Aroi
print(example[::-3])  # tcxo



example  = [2, 3, 4, 5, 6, 7]
example2 = ['a','b','c','d','e','f']

# Unpack
var1, var2, var3, var4, var5, var6 = example

first, *middle, last = example  # first  = 2
                                # middle = [3, 4, 5, 6]
                                # last   = 7

# In place
example.append(8)
example.extend([8, 9, 10])
example.insert(0, 1) # [1, 2, 3, 4, 5, 6, 7]
example.remove(3)    # removes only first appearance!
example.pop()        # [2, 3, 4, 5, 6]
example.pop(0)       # [3, 4, 5, 6, 7]
example.sort()
example.sort(reverse=True)
example.sort(key=len)       # Sorts by el length
example.reverse()
example.clear()      # Makes list into []
del example[1]
del example[1:4]
del example



#Constructor
word = "abcd"
letters = list(word)     # ["a", "b", "c", "d"]

numbers = (1, 2, 3)
lst = list(numbers)

# Converts ANY!! iterable to list
list(range(5))                                   # [0, 1, 2, 3, 4]
list(enumerate(["a", "b", "c"]))                 # [(0, 'a'), (1, 'b'), (2, 'c')]
list(map(lambda x: x * 2, [1, 2, 3]))            # [2, 4, 6]
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) # [2, 4]
list(zip([1, 2], ["a", "b"]))                    # [(1, 'a'), (2, 'b')]



# New object
example_cpy = example.copy()
example_sorted = sorted(example)
example_reversed = reversed(example)
example_filtered = list(filter(lambda num: num > 4, example)) # selects
example_transformd = list(map(lambda x: x * 2, example))      # transforms


# Returns
example.index(4)   # Finds first instance
example.count(4)   # Counts all instances
len(example)
min(example)
max(example)
sum(example)
sorted(example)
any(example)   # True if at least one element is truthy
all(example)   # True if every element is truthy
examples_cocat = example + example #[2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]
zeros = [0] * 5   # [0, 0, 0, 0, 0]
if 4 in example:
    print(True)
evens = [x for x in range(10) if x % 2 == 0]
word = "".join(example2)

word = "abc def"
sentence = word.split(" ")  # ["abc", "def"]


# Iterators
for index, value in enumerate(example, start=0):
    print(index, value)         # 0 2
                                # 1 3
                                # 2 4
                                # 3 5  itd

for num, lett in zip(example, example2): # Pairing lists!
    print(num, lett)

for i in range(1, 4, 1):
    print(i)        # start (inclusive) to stop (exclusive)



import copy
a = [[1], [2], [3]]
b = copy.deepcopy(a)

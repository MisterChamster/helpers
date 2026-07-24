# =============== Imports ===============
# import from as
from typing import Literal as lit


# =============== Class/function ===============
# class def lambda
square = lambda x: x * x
print(square(5))

students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda student: student[1])

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))


# =============== Logical Consts ===============
# True (1)
# False (0)
# None (not integer, but when is a condition, returns false)
if True:
    print("Tru")
if False:
    print("Fals")
if None:
    print("Nun")


# =============== Logic ===============
# and or not is in
if True and True:
    print("Truu")
if True or False:
    print("Still tru")
if not False and not False:
    print("Also tru")

# Ref to same object in memory
a = [1, 2]
b = a
c = [1, 2]
if a is b:
    print("True")
if a is c:
    print("False")


# =============== Control flow ===============
# if elif else
# match case
# for while break continue
# pass
# return yield
note_freq = 440
match note_freq:
    case 440:
        print("Note is A4")
    case 415:
        print("Note is A4 in baroque pitch")
    case _:
        print("Unknown note freq!")

def count_to_three():
    yield 1
    yield 2
    yield 3
for number in count_to_three():
    print(number)

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()
print(next(fib))


# =============== Errors ===============
# try except finally raise assert


# =============== Vars/scope ===============
# global nonlocal del
# global - global (module-level) variable inside a function
count = 0
def increment():
    global count
    count += 1

increment()
print(count)  # 1

# nonlocal - nearest enclosing function, not the global scope
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
outer()  # 1

# del - deletes a variable or removes an item
x = 10
del x

numbers = [10, 20, 30]
del numbers[1]


# =============== With ===============
# with - context managers.
# (objects that automatically set something up and clean it up afterward)
with open("data.txt", "r") as file:
    text = file.read()

import threading
lock = threading.Lock()
with lock:
    print("Only one thread can execute this block.")

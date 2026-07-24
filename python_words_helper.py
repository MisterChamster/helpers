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
# for while break continue
# pass
# return yield
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


# =============== With ===============
# with - context managers.
# (objects that automatically set something up and clean it up afterward)
with open("data.txt", "r") as file:
    text = file.read()

import threading
lock = threading.Lock()
with lock:
    print("Only one thread can execute this block.")


# =============== Async ===============
# async await


# =============== Patterns ===============
# match case


# =============== Imports ===============
# import from as
from typing import Literal as lit


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



# =============== Class/function ===============
# class def lambda

# =============== Errors ===============
# try except finally raise assert

# =============== Vars/scope ===============
# global nonlocal del

# =============== With ===============
# with

# =============== Async ===============
# async await

# =============== Patterns ===============
# match case


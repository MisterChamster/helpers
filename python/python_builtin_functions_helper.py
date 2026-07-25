# ================= Math =================
# abs divmod float int pow round sum complex hex oct 
q, r = divmod(17, 5)
print(q)  # 3
print(r)  # 2

print(pow(2, 3, 5))   # (2 ** 3) % 5

print(round(3.14159))   # .5 values round to the nearest even number

z = complex(2, 3)
print(z)       # (2+3j)
print(z.real)  # 2.0
print(z.imag)  # 3.0

print(complex("4+5j"))  # (4+5j)

print(hex(16))   # 0x10
print(oct(8))    # 0o10
print(bin(5))    # 0b101


# ================= Booleans =================
# bool all any


# ================= Text =================
# ascii chr format ord print repr str
# print(*objects, sep=' ', end='\n', file=None, flush=False)
with open("out.txt", "w") as f:
    print("Saved text", file=f)


# ================= Type / object inspection =================
# callable hasattr isinstance issubclass type id hash


# ================= Sequence / iteration =================
# iter next len list tuple set frozenset dict range slice enumerate reversed sorted zip map filter


# ================= Attribute / scope =================
# getattr setattr delattr dir globals locals vars help


# ================= Files =================
# input open


# ================= Execution / runtime =================
# compile eval exec breakpoint __import__


# ================= OOP =================
# classmethod staticmethod property super object


# ================= Binary data =================
# bytes bytearray memoryview


# ================= Async =================
# aiter anext



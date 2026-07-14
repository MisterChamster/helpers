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




example = [2, 3, 4, 5, 6, 7]

# In place
example.append(8)
example.extend([8, 9, 10])
example.insert(0, 1) # [1, 2, 3, 4, 5, 6, 7]
example.remove(3)    # removes only first appearance!
example.pop()        # [2, 3, 4, 5, 6]
example.pop(0)       # [3, 4, 5, 6, 7]



# New object


# Returns


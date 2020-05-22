from itertools import count, cycle

for el in count():
    if el > 10:
        break
    else:
        print(el)

z = 0
for i in cycle("Kostya"):
    if z > 11:
        break
    print(i)
    z += 1

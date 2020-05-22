from functools import reduce

a = [i for i in range(100, 1001) if i % 2 == 0]


def func(el_1, el_2):
    return el_1 * el_2


print(a)
print("Произведение всех элементов списка:\n", reduce(func, a))

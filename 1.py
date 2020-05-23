from sys import argv

result, arg_1, arg_2, arg_3 = argv
""" 
    arg_1 - Выработка в часах 
    arg_2 - Ставка в час
    arg_3 - Премия
"""
try:
    def my_func(a, b, c):
        return (float(a) * float(b)) + float(c)


    print(f"Ваша заработная плата: {my_func(arg_1, arg_2, arg_3)} рублей!")
except ValueError:
    print("Один из параметров введен некорректно! Необходимо вводить числа!")

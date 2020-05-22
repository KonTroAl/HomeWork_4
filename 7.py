try:
    n = int(input("Введите число, д котрого необходимо найти факторил: "))


    def fact(n):
        z = 1
        a = [i for i in range(1, n + 1)]
        for el in a:
            z *= a[el - 1]
        yield z


    f = fact(n)
    print(f)

    for el in f:
        print(el)

except ValueError:
    print("Недопустимый формат вводимого значения!")

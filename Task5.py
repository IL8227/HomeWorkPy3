# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))
fib = [0, 1]
for i in range(k - 1):
    fib.append(fib[-1] + fib[-2])
neg_fib = [0, 1]
for n in range(k - 1):
    neg_fib.append(neg_fib[-2] - neg_fib[-1])
neg_fib.reverse()
print(neg_fib + fib[1:])        
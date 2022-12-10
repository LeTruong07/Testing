num = int(input('Nhap so n : '))


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(num):
    print(fibonacci(i))

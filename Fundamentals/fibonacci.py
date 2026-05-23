"""
n = int(input("Enter the number till which you want the Fibonacci sequence: "))
a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])
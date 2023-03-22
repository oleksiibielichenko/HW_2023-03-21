import random

arr = []
n = int(input('number: '))
for i in range(n):
    a = random.randint(0, 10000)
    b = random.randint(0, 100)
    c = {'a': a, 'b': b}
    print(c)
    arr.append(c)
print(arr)

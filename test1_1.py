import random

x = [random.randint(0, 100) for i in range(1000)]

y = set(x)

for i in y:
    print(i, "出现次数", x.count(i))

    
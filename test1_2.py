import random

x = [random.randint(0, 100) for i in range(20)]
print(x)
first_half = x[:11]
second_half = x[11:]
first_half.sort()
second_half.sort(reverse=True)
sorted_list = first_half + second_half
print(sorted_list)

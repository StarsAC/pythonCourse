def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_prime(start, end):
    sum1 = sum(n for n in range(start, end+1) if is_prime(n))  # 生成器表达式
    return sum1


sum_1 = sum_prime(1, 10000)
print(sum_1)

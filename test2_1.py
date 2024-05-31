def count_chars(x):
    result = [0, 0, 0, 0]
    for char in x:
        if char.isdigit():
            result[0] += 1
        elif char.isupper():
            result[1] += 1
        elif char.islower():
            result[2] += 1
        else:
            result[3] += 1

    return tuple(result)


print(count_chars(input('Enter a string: ')))

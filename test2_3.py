def my_sorted(iterable, key=None, reverse=False):
    raw_list = list(iterable)

    for i in range(len(raw_list)):
        for j in range(len(raw_list) - i - 1):
            if key:
                key1 = key(raw_list[j])
                key2 = key(raw_list[j + 1])
            else:
                key1 = raw_list[j]
                key2 = raw_list[j + 1]
            if key1 > key2:
                raw_list[j], raw_list[j + 1] = raw_list[j + 1], raw_list[j]
    return raw_list

# print(my_sorted([1,2,4,3,5,6,8,7]))

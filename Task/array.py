def maxarray(some_list):
    x = 0
    list_1 = []
    for i in range(len(some_list)-1):
        if some_list[x] + some_list[x + 1] < some_list[x + 1] + some_list[x + 2]:
            list_1.append(some_list[x + 1])
            list_1.append(some_list[x + 2])
            print(list_1)
            x += 1
        else:
            list_1 = []
    # if max(some_list) > sum(list_1):
    #     return (list_1.clear(), list_1.append(max(some_list)))
    return list_1


print(maxarray([1, -2, 3, -1, 5, -6]))

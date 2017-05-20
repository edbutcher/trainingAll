# def Game(some_list):
#     a = 0
#     if some_list[0][0] == some_list[0][1] == some_list[0][2]: #by X axis
#         a += 3
#     if some_list[1][0] == some_list[1][1] == some_list[1][2]:
#         a += 3
#     if some_list[2][0] == some_list[2][1] == some_list[2][2]:
#         a += 3
#
#     if some_list[0][0] == some_list[1][0] == some_list[2][0]: #by Y axis
#         a += 5
#     if some_list[0][1] == some_list[1][1] == some_list[2][1]:
#         a += 5
#     if some_list[0][2] == some_list[1][2] == some_list[2][2]:
#         a += 5
#
#     if some_list[0][0] == some_list[1][1] == some_list[2][2]: #by diagonal
#         a += 10
#     if some_list[2][0] == some_list[1][1] == some_list[0][2]:
#         a += 10
#     return a
#
#x = [[1,1,1],[1,1,1],[1,1,1]]
# print(Game(x))


def GameFast(sl):
    a = 0
    for i in sl:
        if sl[0] == sl[1] == sl[2]:
            for j in i:
                print(j)
                if i[0] == i[1] == i[2]:
                    a += 3
                    #print(a)

    return print(a)

GameFast(x)

#!/usr/bin/env python3
# a = 3
# b = 5
# r = 0 # Чтобы было, чем заполнять
# mas = []
# for i in range(a):
# mas.append([])
# for j in range(b):
# mas[i].append(r)
# r += 1 # Чтобы заполнялось не одно и тоже
#
# print(mas)
# # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

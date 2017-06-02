def find_num(somelist):
    for i in somelist:
        if i % 2 > 0:
            return i

somelist = [0, 8, 2, 50, 13, 6, 34]
print(find_num(somelist))

#____________________________________________
def sum_all_ab(a, b):
    x = []
    for i in range(a, b + 1):
        x.append(i)
    return sum(x)

a = int(input('a:'))
b = int(input('b:'))
print(sum_all_ab(a, b))


#____________________________________________

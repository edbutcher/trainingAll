#____________________________________________
a = int(input('A side:'))
b = int(input('B side:'))

for _ in range(a):
    print('* ' * b)
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
n = int(input('n!:'))
fac = 1
i = 0
while i < n:
    i += 1
    fac = fac * i
    print (fac)
print ('factorial n!=', fac)


#____________________________________________
n = int(input('input hight of side:'))
i = 0
while i < n:
    i += 1
    print ('* ' * i)

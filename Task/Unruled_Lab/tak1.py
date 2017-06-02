def sorte_list(a):
    b = []
    c = []
    x = int(len(a)/2)

    for _ in range(x):
        if a != []:
            b.extend(a[0:2])
            a.pop(0)
            a.pop(0)
        if a != []:
            c.extend(a[0:2])
            a.pop(0)
            a.pop(0)

    b.sort()
    c.sort()

    for _ in range(x):
        if b != []:
            a.extend(b[0:2])
            b.pop(0)
            b.pop(0)
        if c != []:
            a.extend(c[0:2])
            c.pop(0)
            c.pop(0)
    return a

a = ['yellow', 'white', '2', '5', 'green', 'red', '6', '1']
print(sorte_list(a))

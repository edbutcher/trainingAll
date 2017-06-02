def camel1(s):
    zlist = []
    if s.find('-') > 0:
        a = s.split('-')

        n = 0
        for i in a:
            y = i[0].upper() + i[1:]
            zlist.append(y)
            n += 1

        b = ''
        n = 1
        for x in range(len(zlist)-1):
            b = b + zlist[n]
            n += 1
        return (a[0] + b)
    else:
        a = s.split('_')

        n = 0
        for i in a:
            y = i[0].upper() + i[1:]
            zlist.append(y)
            n += 1

        b = ''
        n = 1
        for x in range(len(zlist)-1):
            b = b + zlist[n]
            n += 1
        return (a[0] + b)

s = 'the_phantom_menace'
#s = 'The-Phantom-Menace'

print(camel1(s))

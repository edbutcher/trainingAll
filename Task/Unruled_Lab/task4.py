def sorted1(somelist):
    ls = []
    for i in somelist:
        ls.append((i['name']))
    s = ''
    n = 0
    if len(ls) == 1:
        s = ls[0]
        return s
    else:

        for i in range(int(len(ls)) - 1):
            s = s + (ls[n] + ', ')
            n += 1

        a = len(s) - 2
        s = s[:a] + ' & ' + ls[-1]
    return s

somelist = [{'name': 'John'}]
somelist = [{'name': 'John'}, {'name': 'Jack'}]
somelist = [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}]

print(sorted1(somelist))

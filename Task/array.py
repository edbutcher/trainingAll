def maxarray(some_list):
    ls = some_list[:]
    x = max(ls)
    a = ls.index(max(ls))
    ls.remove(x)
    b = ls.index(max(ls))
    if a > b:
        ls = some_list[b:a+1]
    else:
        ls = some_list[a:b+1]
    if sum(ls) > x:
        answer = ls
    else:
        answer = x
    return answer

print(maxarray([1, -2, 3, -1, 5, -6]))
print(maxarray([-1, 7, -5, 2]))

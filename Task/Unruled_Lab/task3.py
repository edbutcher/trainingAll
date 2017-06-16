# li_int = [70, 8, 20, 1, 13]            #first try
# li_str = ([str(i) for i in li_int])
# li_str.sort(reverse=True)
# print(''.join(li_str))

from functools import reduce
def max_num_from_array(num_array):
    string_array = map(lambda x: str(x), num_array)
    sorted_array = sorted(string_array, key=str, reverse=True)
    return int(reduce(lambda x,y: x+y, sorted_array))

num_array = [70, 8, 20, 1, 13]
print(max_num_from_array(num_array))

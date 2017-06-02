from functools import reduce
def max_num_from_array(num_array):
    string_array = map(lambda x: str(x), num_array)
    sorted_array = sorted(string_array, key=str, reverse=True)
    return int(reduce(lambda x,y: x+y, sorted_array))

num_array = [70, 8, 20, 1, 13]
print(max_num_from_array(num_array))

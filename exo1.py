def find_min_array(array):
    min_array = array[0]
    # 1 2 3 4 5 -6
    # array[i] element
    for element in array:
        if element < min_array:
            min_array = element
    print(min_array)
    return min_array


array = [1, 3, 4, 5, -8, -123]

find_min_array(array)

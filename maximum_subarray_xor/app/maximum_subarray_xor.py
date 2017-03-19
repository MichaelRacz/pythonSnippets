from functools import reduce

def maximum_subarray_xor(array):
    """
    Return the subarray of a given array whose elements yield the maximum value
    when reduced with xor.
    argument:
    array -- List of elements that are xored.
    result:
    subarray -- Slice of the given array.
    maximum -- Xored elements of the subarray.
    """
    subarray = []
    maximum = 0
    n = len(array)
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            current_slice = array[i:j]
            value = reduce(lambda x, y: x ^ y, current_slice)
            if value > maximum:
                subarray = current_slice
                maximum = value
    return subarray, maximum

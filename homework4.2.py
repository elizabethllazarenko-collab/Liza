def even_index_sum(arr):
    if not arr:
        return 0
    s = sum(arr[::2])
    return s * arr[-1]

print(even_index_sum([0, 1, 7, 2, 4, 8]))
print(even_index_sum([1, 3, 5]))
print(even_index_sum([6]))
print(even_index_sum([]))
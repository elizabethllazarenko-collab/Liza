def split_list(lst):
    n = len(lst)
    mid = (n + 1) // 2
    first = lst[:mid]
    second = lst[mid:]
    return [first, second]
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
#забула запушити тому пишу це щоб змінити:)

import random

arr = [random.randint(1, 9) for _ in range(random.randint(3, 10))]
print("Початковий список:", arr)

new_list = [arr[0], arr[2], arr[-2]]
print("Новий список:", new_list)
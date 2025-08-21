a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

operation = input("Введіть операцію (+, -, *, /): ")
if operation == "+":
    print("Результат:", a + b)
elif operation == "-":
    print("Результат:", a - b)
elif operation == "*":
    print("Результат:", a * b)
elif operation == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Помилка: ділення на нуль!")
else:
    print("Невідома операція")

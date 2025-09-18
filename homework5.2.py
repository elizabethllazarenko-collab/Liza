while True:
    expr = input("Введіть вираз (наприклад: 2 + 3): ")

    try:
        result = eval(expr)
        print("Результат:", result)
    except Exception as e:
        print("Помилка:", e)

    cont = input("Продовжити? (y/yes для так): ").strip().lower()
    if cont not in ("y", "yes"):
        print("Роботу калькулятора завершено.")
        break
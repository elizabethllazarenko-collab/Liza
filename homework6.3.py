def multiply_digits_until_single(num: int) -> int:
    while num > 9:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
    return num

n = int(input("Введіть ціле число: "))
print(multiply_digits_until_single(n))
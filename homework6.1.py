import string

def letters_range(inp: str) -> str:
    start, end = inp.split("-")
    letters = string.ascii_letters
    i1 = letters.index(start)
    i2 = letters.index(end)
    return letters[i1:i2+1]

print(letters_range("a-c"))
print(letters_range("a-a"))
print(letters_range("s-H"))
print(letters_range("a-A"))
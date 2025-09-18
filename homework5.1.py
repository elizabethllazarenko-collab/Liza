import string
import keyword


def is_valid_variable(name: str) -> bool:
    if not name:
        return False

    if name.count("_") == len(name) and len(name) > 1:
        return False

    if name[0].isdigit():
        return False

    if any(ch.isupper() for ch in name):
        return False

    for ch in name:
        if ch in string.punctuation and ch != "_":
            return False
        if ch.isspace():
            return False

    if name in keyword.kwlist:
        return False

    return True


tests = ["_", "", "_", "x", "get_value", "get value", "get!value",
         "some_super_puper_value", "Get_value", "get_Value", "getValue",
         "3m", "m3", "assert", "assert_exception"]

for t in tests:
    print(t, "=>", is_valid_variable(t))
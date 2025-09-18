def format_time(seconds: int) -> str:
    day_seconds = 24 * 60 * 60
    days, rem = divmod(seconds, day_seconds)
    hours, rem = divmod(rem, 3600)
    minutes, secs = divmod(rem, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"

print(format_time(0))
print(format_time(224930))
print(format_time(466289))
print(format_time(950400))
print(format_time(1209600))
print(format_time(1900800))
print(format_time(8639999))
print(format_time(22493))
print(format_time(7948799))
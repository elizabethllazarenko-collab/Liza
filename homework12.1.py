import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"Файл {html_file} не знайдено! Переконайся, що він у тій же папці, де запускаєш скрипт.")
        return
    except UnicodeDecodeError:
        with open(html_file, 'r', encoding='cp1251') as f:
            html = f.read()

    text = re.sub(r'<.*?>', '', html)

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    with open(result_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

    print(f"Готово. Файл збережено як {result_file}")

delete_html_tags("draft.html")
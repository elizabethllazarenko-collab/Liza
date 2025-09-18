import string

def make_hashtag(text: str) -> str:
    clean_text = "".join(ch if ch not in string.punctuation else " " for ch in text)

    words = clean_text.split()
    hashtag = "#" + "".join(word.capitalize() for word in words)

    return hashtag[:140]

print(make_hashtag("Python Community"))
print(make_hashtag("i like python community!"))
print(make_hashtag("Should, I. subscribe? Yes!"))
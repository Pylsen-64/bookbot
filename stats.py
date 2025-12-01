def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()

    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_chars(char_count):
    char_list = []

    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    char_list.sort(key=sort_on, reverse=True)

    return char_list
from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(file_path):
    with open (file_path, 'r', encoding = 'utf-8') as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    words = count_words(book_text)
    chars = count_chars(book_text)
    sorted_chars_list = sort_chars(chars)

    return book_path, words, chars, sorted_chars_list

book_path, word_count, char_count, sorted_chars = main()

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")

for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")

print("============= END ===============")
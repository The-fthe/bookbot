def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    char_list = get_alpha_count_list(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for c in char_list:
        print(c)

    print("--- End repot ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_alpha_count_list(chars):
    alpha_list = []
    for c in chars:
        if c.isalpha():
            alpha_list.append(f"The '{c} character was found {chars[c]} times.")
    alpha_list.sort()
    return alpha_list


main()

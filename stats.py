import sys

def word_count(output):
    count = len(output.split())
    print("----------- Word Count ----------")
    print(f"Found {count} total words")

def char_count(chars):
    letter_dict = {}
    print("--------- Character Count -------")
    for letter in chars:
        if not letter.isalpha():
            continue
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    sorted_items = sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)
    for letters in sorted_items:
        print(f"{letters[0]}: {letters[1]}")
    print("============= END ===============")






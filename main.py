from stats import word_count, char_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    path = sys.argv[1]

    def get_book_text(filepath):
        with open(filepath) as f:
            return f.read()
    input_text = get_book_text(path)
    output = input_text.lower()
    chars = list(output)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    word_count(output)
    char_count(chars)

if __name__ == "__main__":
    main()

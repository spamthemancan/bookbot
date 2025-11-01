def get_book_text (filepath):
    with open (filepath) as f:
        file = f.read()
    return file

def sort_on(item):
    return item[1]

def main():

    import sys
    from stats import get_num_words
    from stats import count_characters

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    character_counts = {} 
    character_counts = count_characters(get_book_text(sys.argv[1]))
    sorted_characters = sorted(character_counts.items(), reverse=True, key=sort_on)

    num_words = get_num_words(get_book_text(sys.argv[1]))

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_characters[1:]:
        print(f"{char}: {count}")
    print("============= END ===============")

main()
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) >= 2:
        from stats import num_words
        from stats import dict_sort
        word_count = num_words(sys.argv[1])
        data = dict_sort()

        def report():
            print("============ BOOKBOT ============")
            print("Analyzing book found at ...")
            print("----------- Word Count ----------")
            print(f"Found {word_count} total words")
            print("--------- Character Count -------")
            for i in range(len(data)):
                if data[i]["char"].isalpha() is True:
                    print(f"{data[i]["char"]}: {data[i]["num"]}")
            print("============= END ===============")
        report()

main()

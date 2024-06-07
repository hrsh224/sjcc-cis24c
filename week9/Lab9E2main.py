
import sys
import helper

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <search_word>")
        return

    search_word = sys.argv[1]

    # Get the count of similar words and total lines using helper.py
    count_of_similar_words = helper.getCountOfSimilarWords(search_word)
    total_lines = helper.getTotalLines(search_word)

    if count_of_similar_words is not None and total_lines is not None:
        print("Total Words:", count_of_similar_words)
        print("Total lines:", total_lines)

if __name__ == "__main__":
    main()

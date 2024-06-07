
### YOUR CODE GOES BELOW
import requests

def getCountOfSimilarWords(search_word):
    try:
        response = requests.get("https://en.wikipedia.org/wiki/India")

        text = response.text.lower()
        words = text.split()
        count = words.count(search_word.lower())
        return count
    except Exception as e:
        print("Error:", e)
        return None

def getTotalLines(search_word):
    try:
        response = requests.get("https://en.wikipedia.org/wiki/India")
        lines = response.text.split("\n")
        total_lines = len(lines)
        return total_lines
    except Exception as e:
        print("Error:", e)
        return None


### END CODE

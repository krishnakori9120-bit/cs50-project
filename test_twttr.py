def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_capitalized():
    assert shorten("Twitter") == "Twttr"

def test_numbers():
    assert shorten("1234") == "1234"
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("What's up?") == "Wht's p?"

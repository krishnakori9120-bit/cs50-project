def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    result = ""

    for letter in word:
        if letter.lower() not in "aeiou":
            result += letter

    return result


if __name__ == "__main__":
    main()

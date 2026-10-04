def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Must be 2 to 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Only letters and numbers are allowed
    if not s.isalnum():
        return False

    # Numbers must be at the end, and first number can't be 0
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


main()

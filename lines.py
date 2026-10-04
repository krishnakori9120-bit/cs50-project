import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as file:
            count = 0

            for line in file:
                line = line.strip()

                if line == "" or line.startswith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

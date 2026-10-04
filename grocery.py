def main():
    grocery_list = {}

    while True:
        try:
            # Prompt the user for an item and convert it to uppercase
            item = input().strip().upper()

            # If the item is already in the dictionary, increment its count
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            # When control-d (EOF) is caught, print a newline and break the loop
            print()
            break

    # Sort the grocery list alphabetically by its keys (item names)
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()

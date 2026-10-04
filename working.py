import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regex pattern to match both 12-hour formats with/without minutes and AM/PM
    pattern = r"^([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    groups = match.groups()

    # Extract start time components
    start_hour = int(groups[0])
    start_min = int(groups[1]) if groups[1] else 0
    start_meridiem = groups[2]

    # Extract end time components
    end_hour = int(groups[3])
    end_min = int(groups[4]) if groups[4] else 0
    end_meridiem = groups[5]

    # Convert to 24-hour format
    start_24 = convert_to_24(start_hour, start_min, start_meridiem)
    end_24 = convert_to_24(end_hour, end_min, end_meridiem)

    return f"{start_24} to {end_24}"

def convert_to_24(hour, minute, meridiem):
    if meridiem == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()

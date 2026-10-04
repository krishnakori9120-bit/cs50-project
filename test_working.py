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
import pytest
from working import convert

def test_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_time():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"

def test_value_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")

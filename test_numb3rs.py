import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # This regular expression checks for 4 groups of numbers separated by dots.
    # Each group strictly accepts 0-255 and blocks invalid leading zeros (like 001).
    regex = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    if re.search(regex, ip):
        return True
    return False

if __name__ == "__main__":
    main()
from numb3rs import validate

def test_format():
    assert validate(r"127.0.0.1") == True
    assert validate(r"127.0.0") == False
    assert validate(r"127.0") == False
    assert validate(r"127") == False
    assert validate(r"127.0.0.1.5") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    # Explicitly test each byte position to catch faulty functions that only check the first byte
    assert validate(r"1.512.1.1") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.1.1.512") == False

def test_non_numeric():
    assert validate(r"cat") == False
    assert validate(r"192.168.0.cat") == False

def test_leading_zeros():
    # As per the problem's updated guidelines, leading zeros shouldn't be accepted
    assert validate(r"192.168.001.1") == False

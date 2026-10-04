import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Matches 'um' as a standalone word, case-insensitively
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
    import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_um_in_words():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("um...") == 1
    assert count("hello, um, world") == 1

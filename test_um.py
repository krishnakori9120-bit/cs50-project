from um import count

def test_case_insensitivity():
    # Catches if code doesn't handle case-insensitivity
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1

def test_word_boundaries():
    # Catches if code matches "um" inside other words
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0

def test_punctuation():
    # Catches if code strictly requires spaces instead of handling punctuation
    assert count("um?") == 1
    assert count("um,") == 1
    assert count("hello, um, world") == 1

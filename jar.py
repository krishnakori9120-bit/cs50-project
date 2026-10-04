class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0 or (self._size + n) > self._capacity:
            raise ValueError("Exceeds capacity or invalid deposit amount.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 or (self._size - n) < 0:
            raise ValueError("Cannot withdraw more cookies than available.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    custom_jar = Jar(5)
    assert custom_jar.capacity == 5

    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("abc")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)  # Exceeds capacity of 5

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(5)  # Trying to withdraw more than available size

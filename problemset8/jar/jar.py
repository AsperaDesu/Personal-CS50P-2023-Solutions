class Jar:
    def __init__(self, capacity = 12):
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        return f'{"🍪" * self._size}'

    def deposit(self, n):
        self._size += n
        if self._size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if self._size >= n:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

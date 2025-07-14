# oop_and_utils.py

from collections import Counter
from itertools import permutations
from functools import lru_cache

# ---------- OOP BASICS ----------

class Animal:
    def __init__(self, name):
        self.name = name      # Public attribute
        self._type = "animal" # Protected attribute
        self.__id = 123       # Private attribute

    def speak(self):
        return f"{self.name} makes a sound."

    def get_id(self):  # Accessing private attribute
        return self.__id


# ---------- INHERITANCE / POLYMORPHISM / ENCAPSULATION ----------

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# ---------- MIXIN EXAMPLE ----------

class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Service(Dog, LoggerMixin):  # Multiple Inheritance
    def run(self):
        self.log(self.speak())


# ---------- SPECIAL METHODS ----------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return len(self.title)


# ---------- COLLECTIONS / PERMUTATIONS EXAMPLE ----------

def analyze_words(words):
    counter = Counter(words)
    print("Word count:", counter)

    perms = list(permutations(words, 2))
    print("Word permutations (2):", perms[:5])  # Limit output


# ---------- LRU CACHE EXAMPLE ----------

@lru_cache(maxsize=3)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # OOP & Mixins
    dog = Service("Buddy")
    dog.run()

    book = Book("Python Tricks", "Dan Bader")
    print(book, "Length of title:", len(book))
    print("Private ID access:", dog.get_id())

    # Data structures and stdlib
    analyze_words(["apple", "banana", "apple", "cherry", "banana"])
    print("Fibonacci(10):", fibonacci(10))

    # Escape Character Example
    print("He said, \"Learning Python is fun!\"\nLet's keep going!\t🚀")

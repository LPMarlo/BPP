"""
Implementa un Script con un conjunto de funciones y crea un mínimo de 5
test para cada una de las librerías de test vistasen la clase (unittest y pytest)
"""

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_palindrome(self):
        n = 'solos'
        self.assertEqual(n, n[::-1])

    def test_email_regex(self):
        email_regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        self.assertRegex('lpmarlo72@gmail.com', email_regex)


if __name__ == '__main__':
    unittest.main()


import pytest


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1


@pytest.fixture
def input_total():
    total = 100
    return total


def test_str_replace():
    string = "Hello, World!"
    assert string.replace("H", "J") == "Jello, World!"


def test_str_split():
    string = "Hello,World"
    assert string.split(",") == ["Hello", "World"]


def test_str_strip():
    string = " Hello, World! "
    assert string.strip() == "Hello, World!"


def test_str_concat():
    string1 = "Hello"
    string2 = "World"
    assert string1 + string2 == "HelloWorld"

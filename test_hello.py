import pytest
from hello import greet, main


def test_greet_default():
    """Test greeting with default name."""
    assert greet() == "Hello, World!"


def test_greet_with_name():
    """Test greeting with custom name."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_main_function():
    """Test the main function returns correct message."""
    result = main()
    assert result == "Hello, World!"


def test_greet_empty_string():
    """Test greeting with empty string."""
    assert greet("") == "Hello, !"
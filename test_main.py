import pytest
from main import hello_world

def test_hello():
    assert hello_world() == "Hello, World!"
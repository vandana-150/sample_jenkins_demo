import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5  
    assert add(-1, 1) == 0  

def test_subtract():
    assert subtract(5, 3) == 2  
    assert subtract(2, 2) == 0  

def test_multiply():
    assert multiply(4, 3) == 12  
    assert multiply(2, 0) == 0   

def test_divide():
    assert divide(10, 2) == 5  
    with pytest.raises(ValueError):
        divide(5, 0)  

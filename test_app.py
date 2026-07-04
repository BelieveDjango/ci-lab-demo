from app import add, multiply
def test_add_basic():
    assert add(2, 3) == 5
 
def test_add_zero():
    assert add(0, 5) == 5
 
def test_add_negative():
    assert add(-1, 1) == 0
 
def test_multiply_basic():
    assert multiply(4, 5) == 20
 
def test_multiply_zero():
    assert multiply(0, 9) == 0

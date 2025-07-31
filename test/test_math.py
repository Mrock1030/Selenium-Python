import pytest


def add_two_numbers(a,b):
    return a + b
      
@pytest.mark.math_test   
def test_small_numbers():
    assert add_two_numbers(1,2) == 3
    
def test_large_two_numbers():
    assert add_two_numbers(100,400) #The sun of 100 and 300 should be 400
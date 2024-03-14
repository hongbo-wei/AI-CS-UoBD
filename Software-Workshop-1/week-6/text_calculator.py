import pytest
import calculator


def test_add():
    assert calculator.add(1, 3) == 4


def test_substract():
    assert calculator.substract(1, 3) == -2


def test_multiply():
    assert calculator.multiply(1, 3) == 3


def test_divide():
    assert calculator.divide(1, 3) == 1/3


'''
If you include pytest.main() directly in your test script, it will indeed run all test files in the current directory and its subdirectories. 
'''
# if __name__ == '__main__':
#     pytest.main()
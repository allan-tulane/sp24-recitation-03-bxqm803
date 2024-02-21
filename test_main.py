from main import *


def test_multiply():
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
  assert quadratic_multiply(BinaryNumber(100), BinaryNumber(100)) == 100*100
  assert quadratic_multiply(BinaryNumber(326), BinaryNumber(128)) == 326*128
  assert quadratic_multiply(BinaryNumber(912), BinaryNumber(456)) == 912*456

#one of the question is when I use pytest test_main.py, it says one pass and one error but I only test one function. Only when I type pytest test_main.py::test_multiply, it says pass.



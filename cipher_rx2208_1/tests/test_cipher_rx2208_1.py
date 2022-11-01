from cipher_rx2208_1 import cipher_rx2208_1
import pytest
def test_cipher_a():
  example = "a"
  expected = "b"
  actual = cipher_rx2208_1.cipher("a",1)
  assert actual == expected

def test_cipher_b():
  example = "b"
  expected = "a"
  actual = cipher_rx2208_1.cipher("b",-1)
  assert actual == expected

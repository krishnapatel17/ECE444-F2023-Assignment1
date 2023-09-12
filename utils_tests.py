import unittest 
from utils import Utils 

class UtilsTests(unittest.TestCase):
  
  def test_reversed_int(self):
    self.AssertEqual(Utils.reversed(17), 71)

  def test_reversed_string(self):
    with self.assertRaises(TypeError):
            Utils.reversed("17")

  def test_reversed_float(self):
    with self.assertRaises(TypeError):
            Utils.reversed(17.1)

  def test_formatter_int(self):
    self.AssertEqual(Utils.formatter(17), (bin(17), oct(17)))

  def test_formatter_string(self):
    with self.assertRaises(TypeError):
            Utils.formatter("17")

  def test_formatter_float(self):
    with self.assertRaises(TypeError):
            Utils.formatter(17.1)
      
    

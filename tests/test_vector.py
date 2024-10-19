import unittest
import random

from source.vector import *

class TestVector(unittest.TestCase):
    
    def test_addition(self):
        x,y,u,v = [random.randint(-9999,9999) for x in range(4)]
        # test general
        self.assertEqual(addi((x,y), (u,v)), (x+u,y+v))
        # test commutativity
        self.assertEqual(addi((x,y), (u,v)), addi((u,v), (x,y)))
        # test associativity
        self.assertEqual(addi(addi((x,y), (u,v)), (x,u)), addi((x,y), addi((u,v), (x,u))))
        pass
    
    def test_subtractio(self):
        x,y,u,v = [random.randint(-9999,9999) for x in range(4)]
        # test general
        self.assertEqual(subi((x,y), (u,v)), (x-u,y-v))
        pass
    
    def test_multiplication(self):
        x,y,u,v = [random.randint(-9999,9999) for x in range(4)]
        # test general
        self.assertEqual(muli((x,y), u), (x*u,y*u))
        pass
    
    def test_division(self):
        x,y,u,v = [random.randint(-9999,9999) for x in range(4)]
        # test general
        self.assertEqual(divi((x,y), u), (x/u,y/u))
        pass
    
    def test_dotproduct(self):
        x,y,u,v = [random.randint(-9999,9999) for x in range(4)]
        # test general
        self.assertEqual(doti((x,y), (u,v)), x*u+y*v)
        pass
    
    pass

if __name__ == "__main__":
    unittest.main()
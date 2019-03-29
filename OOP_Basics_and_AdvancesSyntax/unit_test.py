import unittest
def triangle_area (b,h):
    return 0.5 * b * h

class TestTriangleArea (unittest.TestCase):
    def test_area (self):
        self.assertAlmostEqual (triangle_area(1,1), 0.5)
        self.assertAlmostEqual (triangle_area(0,0), 0.0)
        self.assertAlmostEqual (triangle_area(2.1*3.5), 0.5*2.1*3.5)
        
    def test_values (self):
        self.assertRaises (ValueError, triangle_area, -5)
        self.assertRaises (TypeError, triangle_area, j)
        self.assertRaises (TypeError, triangle_area, "Vivek")
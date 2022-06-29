import unittest
import areas
from math import pi

class testers(unittest.TestCase):
    def test_circle(self):
        # Test for normal valid value
        circle_area = areas.circle_area(5)
        self.assertEqual(circle_area, (pi*25))
        # Test for negative value
        circle_area =  areas.circle_area(-5)
        self.assertEqual(circle_area, 0)
        # Testing for 0 radius
        circle_area = areas.circle_area(0)
        self.assertEqual(circle_area, 0)

        # Test for string numerical value
        circle_area = areas.circle_area("8")
        self.assertEqual(circle_area, (pi*64))
        # Test for string non numeric value
        circle_area = areas.circle_area("F")
        self.assertEqual(circle_area, 0)

if __name__ ==  '__main__':
    unittest.main()
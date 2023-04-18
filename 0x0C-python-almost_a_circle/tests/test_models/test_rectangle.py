#!/usr/bin/python3
"""Rectangle testing"""
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_width(self):
        """Test rectangle width"""
        rec = Rectangle(8,9)
        self.assertEqual(8, self.rec.width)

    def test_height(self):
        """Test rectangle height"""
        rec = Rectangle(8,9)
        self.assertEqual(9, self.rec.height)

     def test_x(self):
        """Test rectangle x val"""
        rec = Rectangle()
        rec.x = 10
        self.assertEqual(10, self.rec.x )

     def test_y(self):
        """Test rectangle y val"""
        rec = Rectangle(8,9)
        self.assertEqual(8, self.rec.width)


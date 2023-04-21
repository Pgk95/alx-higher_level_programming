import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_instance_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

        b4 = Base()
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()

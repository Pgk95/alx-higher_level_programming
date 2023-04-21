import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_string = Base.to_json_string(list_dicts)
        self.assertIsInstance(json_string, str)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},' \
                      ' {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertIsInstance(list_dicts, list)
        self.assertEqual(len(list_dicts), 2)
        for d in list_dicts:
            self.assertIsInstance(d, dict)
        expected_output = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
                           {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}]
        self.assertCountEqual(list_dicts, expected_output)

    def test_create(self):
        r1_dict = {'id': 10, 'width': 3, 'height': 5, 'x': 1, 'y': 1}
        r1 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 1/1 - 3/5')

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles, list)
        self.assertEqual(len(list_rectangles), 2)
        for r in list_rectangles:
            self.assertIsInstance(r, Rectangle)
        r1_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r2_dict = {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        expected_output = [Rectangle.create(**r1_dict), Rectangle.create(**r2_dict)]
        self.assertCountEqual(list_rectangles, expected_output)


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_validators(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 2)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

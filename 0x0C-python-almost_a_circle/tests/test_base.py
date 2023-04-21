import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        """Test creating a new instance with a given ID"""
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        
        """Test creating a new instance with an ID of None"""
        b2 = Base()
        self.assertEqual(b2.id, 2)
        
        """Test creating a new instance with a negative ID"""
        b3 = Base(-5)
        self.assertEqual(b3.id, -5)
        
        """Test creating a new instance with a string ID"""
        with self.assertRaises(TypeError):
            b4 = Base("hello")
            
    def test_to_json_string(self):
        """Test converting a list of dictionaries to a JSON string"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(1, 2)
        r2_dict = r2.to_dictionary()
        expected_output = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"width": 1, "id": 2, "height": 2, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([r1_dict, r2_dict]), expected_output)
        
        """Test converting an empty list to a JSON string"""
        self.assertEqual(Base.to_json_string([]), "[]")
        
        """Test converting None to a JSON string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        
    def test_from_json_string(self):
        """Test converting a JSON string to a list of dictionaries"""
        json_string = '[{"y": 8, "height": 7, "width": 10, "x": 2, "id": 1}, {"y": 0, "height": 2, "width": 1, "x": 0, "id": 2}]'
        expected_output = [{'y': 8, 'height': 7, 'width': 10, 'x': 2, 'id': 1}, {'y': 0, 'height': 2, 'width': 1, 'x': 0, 'id': 2}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)
        
        """Test converting an empty JSON string to an empty list"""
        self.assertEqual(Base.from_json_string(""), [])
        
        """Test converting None to an empty list"""
        self.assertEqual(Base.from_json_string(None), [])
        
    def test_create(self):
        """Test creating a new instance from a dictionary"""
        r1_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        r1 = Rectangle.create(**r1_dict)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 8)
        
    def test_load_from_file(self):
        """Test creating a list of instances from a JSON file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

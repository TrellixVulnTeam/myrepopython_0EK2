import unittest

from app.routes import men

class TestMen(unittest.TestCase):
    def test_two_int(self):
        data = [2, 1]
        result = men(data[0],data[1])
        self.assertEqual(result, 1)

    def test_two_float(self):
        data = [2.02, 1.01]
        result = men(data[0],data[1])
        self.assertEqual(result, 1.01)
        
    def test_list_with_negative_value(self):
        data = [-2, 1]
        result = men(data[0],data[1])
        self.assertEqual(result, -3)

    def test_fail_with_string(self):
        data = ['2', 1]
        result = men(data[0],data[1])
        self.assertEqual(result, 1)
        self.assertEqual(result[0], "Error occured!") 
        self.assertEqual(result[1], 500) 

    def test_fail_with_single_value(self):
        data = [2, 1]
        result = men(data[0],data[1])
        self.assertEqual(result, 1)
        self.assertEqual(result[0], "Error occured!") 
        self.assertEqual(result[1], 500) 

# test_mongooseos.py
"""
Tests for MongooseOs module.
"""

import unittest
from mongooseos import MongooseOs

class TestMongooseOs(unittest.TestCase):
    """Test cases for MongooseOs class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MongooseOs()
        self.assertIsInstance(instance, MongooseOs)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MongooseOs()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

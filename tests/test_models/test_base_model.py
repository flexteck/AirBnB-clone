import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """unit test for BaseModel"""
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsinstance(obj.updated_at, datetime)


    def test_unique_ids(self):
        """ Test that each instance has a unique ID """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)


    def test_to_dict(self):
        """ Test if to_dict() returns a correct dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())


    def test_recreate_from_dict(self):
        """ Test if an instance can be recreated from to_dict() """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = obj(**obj_dict)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_)
        self.assertFalse(hasattr(new_obj, '__class__'))

if __name__ == "__main__":
    unittest.main()

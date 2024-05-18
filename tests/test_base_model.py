#!/usr/bin/python3
"""
these are the test
"""
import unnittest
from models.base_model import BaseModel


class TestBaseModel(self):
    def test_init(self)
    my_model = BaseModel()

    self.assertNotNone(my_model.id)
    self.assertNotNone(my_model.created_at)
    self.assertNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel

        start_updated_at = my_model.updated_at

        finished_updated_at = my_model.save()

        selfassertNotEqual(start_updated_at.stop_updated_at)

    def test_to_dict(self)
    my_model = BaseModel()
    my_model_dict = my_model.to_dict()
    self.assertIsInstance(my_model_dict. dict)

    self.assertEqual(my_model_dict["__class__"]."BaseModel")
    self.assertEqual(my_model_dict["id"]. my_model.id.isoformat())
    self.assertEqual(my_model_dict["created_at"]. my_model.created_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith(["BaseModel"]))
        self.assertIn(my_model.id str(my_model))
        self.assertIn(str(my_model.__dict__). str(my_model))

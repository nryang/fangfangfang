import unittest
from fangfangfang.controllers.impl.validators.model_validator import is_model


class TestModelValidator(unittest.TestCase):

    def test_is_model_none(self):
        self.assertTrue(is_model(None))

    def test_is_model_matches(self):
        self.assertTrue(is_model('homoglyph'))

    def test_is_model_no_match(self):
        self.assertFalse(is_model('yolo'))


if __name__ == '__main__':
    unittest.main()

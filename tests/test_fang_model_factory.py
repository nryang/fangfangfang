import unittest
from fangfangfang.controllers.impl.models.fang_model_factory\
    import FangModelFactory
from fangfangfang.controllers.impl.models.homoglyph_fang_model\
    import HomoglyphFangModel
from fangfangfang.models.model import Model


class TestFangModelFactory(unittest.TestCase):

    def test_create_model_none(self):
        self.assertIsInstance(FangModelFactory.create_model(None), HomoglyphFangModel)

    def test_create_model_homoglyph(self):
        self.assertIsInstance(FangModelFactory.create_model(Model.HOMOGLYPH), HomoglyphFangModel)

    def test_create_model_invalid(self):
        self.assertIsInstance(FangModelFactory.create_model('yolo'), HomoglyphFangModel)


if __name__ == '__main__':
    unittest.main()

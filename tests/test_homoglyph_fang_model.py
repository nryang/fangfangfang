import unittest
from fangfangfang.controllers.impl.models.homoglyph_fang_model\
    import HomoglyphFangModel
from parameterized import parameterized


class TestHomoglyphFangModel(unittest.TestCase):

    _ioc_to_defanged = [
        ('https://somewebsite.com', 'ℎ𝐭𝐭⍴ƽː᜵᜵ƽᴏm℮ɯ℮Ƅƽı𝐭℮․ᴄᴏm'),
        ('http://192.168.1.1', 'ℎ𝐭𝐭⍴ː᜵᜵IꝮƧ․I𝟔Ȣ․I․I'),
        ('ftp://user:password@host:port/path', 'ſ𝐭⍴ː᜵᜵ʋƽ℮ꭇː⍴ɑƽƽɯᴏꭇⅆ@ℎᴏƽ𝐭ː⍴ᴏꭇ𝐭᜵⍴ɑ𝐭ℎ'),
        ('clickonmyemail@gotcha.com', 'ᴄlıᴄ𝐤ᴏ𝐧mɣ℮mɑıl@ƍᴏ𝐭ᴄℎɑ․ᴄᴏm')
    ]
    _homoglyph_model = HomoglyphFangModel()

    def test_translation_dict(self):
        self.assertEqual(len(self._homoglyph_model.homoglyph_to_ascii), len(self._homoglyph_model.ascii_to_homoglyph))

        for char in self._homoglyph_model.homoglyph_to_ascii:
            self.assertTrue(char in self._homoglyph_model.ascii_to_homoglyph.values())

        for char in self._homoglyph_model.ascii_to_homoglyph:
            self.assertTrue(char in self._homoglyph_model.homoglyph_to_ascii.values())

    @parameterized.expand(_ioc_to_defanged)
    def test_defang_ioc_substitutions(self, ioc, defanged):
        self.assertEqual(self._homoglyph_model.defang(ioc), defanged)

    @parameterized.expand(_ioc_to_defanged)
    def test_defang_defang(self, ioc, defanged):
        self.assertEqual(self._homoglyph_model.defang(
            self._homoglyph_model.defang(ioc)), defanged)

    @parameterized.expand(_ioc_to_defanged)
    def test_refang_defang(self, ioc, defanged):
        self.assertEqual(self._homoglyph_model.refang(
            self._homoglyph_model.defang(ioc)), ioc)

    @parameterized.expand(_ioc_to_defanged)
    def test_refang_refang(self, ioc, defanged):
        self.assertEqual(self._homoglyph_model.refang(
            self._homoglyph_model.refang(ioc)), ioc)

    @parameterized.expand(_ioc_to_defanged)
    def test_defang_refang(self, ioc, defanged):
        self.assertEqual(self._homoglyph_model.defang(
            self._homoglyph_model.refang(ioc)), defanged)


if __name__ == '__main__':
    unittest.main()

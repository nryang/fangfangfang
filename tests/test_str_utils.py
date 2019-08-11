import unittest
from fangfangfang.str_utils import replace_all


class TestStrUtils(unittest.TestCase):

    def test_replace_all_no_substitutions(self):
        self.assertEqual(replace_all('foo', {}), 'foo')

    def test_replace_all_substitution_no_matches(self):
        self.assertEqual(replace_all('foo', {'apple': 'banana'}), 'foo')

    def test_replace_all_multiple_substitutions(self):
        self.assertEqual(replace_all(
            'zzz Iafooz1 zzz', {'f': 'o', 'o': 'f', '1': 'I', 'I': '1'}), 'zzz 1aoffzI zzz')


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from parameterized import parameterized
from fangfangfang.controllers.impl.models.homoglyph_fang_model\
    import HomoglyphFangModel
from fangfangfang.controllers.impl.default_controller_impl import defang, refang
from fangfangfang.models.defang_request import DefangRequest
from fangfangfang.models.refang_request import RefangRequest


class TestDefaultControllerImpl(unittest.TestCase):

    @parameterized.expand([
        'test.com',
        'TEST.COM',
        'smtp://aa',
        'ftp://11',
        'ssh://foobar.example.org/',
        'asfasf.org\nasfafafa.wwwww.org\n'
        'http://192.168.1.1',
        'HttP://localhosT/kekeke',
        'gg@norm.com',
        'https://example.org/test?target=bad@test.com',
        'meow.com:80/.well-known/acme-challenge/mxr.pdf',
        'https://mee.host/ Email: aef.fbf@frtt.com, moo2018@evil.ru',
        'xxxx://example.com/test.php',
        'http:// example.com/test.php',
        'https&://example.com/test.php',
    ])
    @patch('fangfangfang.controllers.impl.models.homoglyph_fang_model.HomoglyphFangModel.defang')
    def test_defang_is_ioc(self, not_ioc, mock_for_defang):
        mock_for_defang.return_value = 'this_is_a_mocked_defang_result'
        defang_request = DefangRequest(contents=[not_ioc])
        defang_response = defang(defang_request)
        self.assertTrue('this_is_a_mocked_defang_result' in defang_response.defanged_contents[0])

    @parameterized.expand([
        'magnet:?xt=urn:btih:c12fe1c06bba254a9dc9f519b335aa7c1367a88a',
        '192.168.1.1',
        '1.com',
        'test.a',
        'wee.a',
        'yo.123',
        'sftp:/',
        'sftp://',
        'sftp://a',
        'a.c',
        'һｔｔｐ：⁄⁄ｅⅹａⅿｐⅼｅ．ｃｏⅿ'
    ])
    def test_defang_not_ioc(self, not_ioc):
        defang_request = DefangRequest(contents=[not_ioc])
        defang_response = defang(defang_request)
        self.assertEqual(defang_response.defanged_contents, [not_ioc])

    @patch('fangfangfang.controllers.impl.models.fang_model_factory.FangModelFactory.create_model')
    @patch('iocextract.extract_urls')
    @patch('iocextract.extract_emails')
    @patch('fangfangfang.controllers.impl.models.homoglyph_fang_model.HomoglyphFangModel.defang')
    def test_defang_replace(self, mock_for_defang, mock_for_extract_emails, mock_for_extract_urls, mock_for_create_model):
        mock_for_create_model.return_value = HomoglyphFangModel()
        mock_for_extract_urls.return_value = [
            'http://localhost:56732/api/ui',
            'https://192.168.1.1'
        ]
        mock_for_extract_emails.return_value = [
            'nryang@users.noreply.github.com'
        ]
        mock_for_defang.return_value = 'this_is_a_mocked_defang_result'

        defang_request = DefangRequest(contents=['yo http://localhost:56732/api/ui https://192.168.1.1',
                                                 'second_text_no_urls nryang@users.noreply.github.com'])
        defang_response = defang(defang_request)
        self.assertEqual(defang_response.defanged_contents,
            ['yo this_is_a_mocked_defang_result this_is_a_mocked_defang_result',
             'second_text_no_urls this_is_a_mocked_defang_result'])

    @patch('fangfangfang.controllers.impl.models.fang_model_factory.FangModelFactory.create_model')
    @patch('fangfangfang.controllers.impl.models.homoglyph_fang_model.HomoglyphFangModel.refang')
    def test_refang(self, mock_for_refang, mock_for_create_model):
        mock_for_create_model.return_value = HomoglyphFangModel()
        mock_for_refang.return_value = 'this_is_a_mocked_refang_result'

        refang_request = RefangRequest(
            contents=['refang_me', 'refang_me2'])
        refang_response = refang(refang_request)
        self.assertEqual(refang_response.refanged_contents,
            ['this_is_a_mocked_refang_result',
             'this_is_a_mocked_refang_result'])


if __name__ == '__main__':
    unittest.main()

import unittest
from Yandex_API import YaUploader

token = ''


class TestYandex_Api(unittest.TestCase):

    def setUp(self):
        self.yandex = YaUploader(token)

    def test_create_folder(self):
        self.assertEqual(self.yandex.create_folder('backup'), (201, 200))

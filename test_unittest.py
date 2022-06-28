import unittest
from parameterized import parameterized
from main import check_document_existance, get_doc_owner_name, \
    add_new_shelf, get_doc_shelf, delete_doc


class TestFunctions(unittest.TestCase):

    @parameterized.expand([
        ["2207 876234", True],
        ["11-2", True],
        ["10006", True],
        ["45-867", False]
    ])
    def test_check_document_existance(self, document, doc_founded):
        self.assertEqual(check_document_existance(document), doc_founded)

    @parameterized.expand([
        ["2207 876234", 'Василий Гупкин'],
        ["11-2", 'Геннадий Покемонов'],
        ["10006", 'Аристарх Павлов'],
        ["6543", None]
    ])
    def test_get_doc_owner_name(self, document_number, doc_owner):
        self.assertEqual(get_doc_owner_name(document_number), doc_owner)

    @parameterized.expand([
        ["1", ("1", False)],
        ["2", ("2", False)],
        ["3", ("3", False)],
        ["4", ("4", True)]
    ])
    def test_add_new_shelf(self, shelf_number, result):
        self.assertEqual(add_new_shelf(shelf_number), result)

    @parameterized.expand([
        ["2207 876234", "1"],
        ["11-2", "1"],
        ["10006", "2"],
        ['12345', None]
    ])
    def test_get_doc_shelf(self, user_doc_number, result):
        self.assertEqual(get_doc_shelf(user_doc_number), result)


#   'test_delete_doc' не работает вмессте с другими тестами, так как удаляет документ.

    # @parameterized.expand([
    #     ["2207 876234", ("2207 876234", True)],
    #     ["11-2", ("11-2", True)],
    #     ["10006", ("10006", True)],
    #     ["45-867", None]
    # ])
    # def test_delete_doc(self, user_doc_number, result):
    #     self.assertEqual(delete_doc(user_doc_number), result)

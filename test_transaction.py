import unittest
from core.library import Library
class TestLibrarySystem(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.library = Library()

    def test1a_add_book(self):
        book = self.library.add_book("Test Book", "Test Author", "1234567890")
        available = self.library.track_availability("Test Book")
        self.assertTrue(available)

    def test1b_search_book(self):
        book = self.library.search_books("Test Book")
        self.assertEqual(book["_Book__isbn"],"1234567890")

    def test1c_update_book(self):
        status = self.library.update_book("Test Book",False)
        self.assertTrue(status)

    def test2a_add_user(self):
        status = self.library.add_user("Test User", "001")
        self.assertTrue(status)

    def test2b_update_user(self):
        status = self.library.update_user("001","Test User 2")
        self.assertTrue(status)
    
    def test2c_serch_user(self):
        data = self.library.search_users("001")
        self.assertEqual(data["_User__name"], "Test User 2")


    def test3_check_out_book(self):
        status = self.library.checkout_book("001", "Test Book")
        self.assertTrue(status)

    def test4_delete_book(self):
        status = self.library.delete_book("Test Book","1234567890")
        self.assertTrue(status)

    def test5_delete_user(self):
        status = self.library.delete_user("001")
        self.assertTrue(status)
        

    # def test_check_in_book(self):
    #     self.library.check_in_book("002", "0987654321")
    #     book = self.storage.read_books()[0]
    #     user = self.storage.read_users()[0]
    #     self.assertFalse(book['is_checked_out'])
    #     self.assertEqual(len(user['borrowed_books']), 0)


if __name__ == '__main__':
    unittest.main()

from django.test import TestCase
from .services import PasswordService, Complexity, Length

class PasswordDataTests(TestCase):
    def test_generate_easy_password(self):
        pwd = PasswordService.generate_password(Complexity.easy, Length.easy)
        
        self.assertEqual(len(pwd), Length.easy.value)

        for char in pwd:
            self.assertIn(char, Complexity.easy.value)

    def test_generate_medium_password(self):
        pwd = PasswordService.generate_password(Complexity.medium, Length.medium)
        
        self.assertEqual(len(pwd), Length.medium.value)

        for char in pwd:
            self.assertIn(char, Complexity.medium.value)

    def test_generate_hard_password(self):
        pwd = PasswordService.generate_password(Complexity.hard, Length.hard)
        
        self.assertEqual(len(pwd), Length.hard.value)

        for char in pwd:
            self.assertIn(char, Complexity.hard.value)

    def test_hash_password_and_check(self):
        pwd = 'dummyPassword'
        hashed_pwd = PasswordService.hash_password(pwd)

        self.assertNotEqual(pwd, hashed_pwd)
        self.assertTrue(hashed_pwd.startswith('$2'))
        self.assertTrue(PasswordService.check_password(pwd, hashed_pwd))
        self.assertFalse(PasswordService.check_password('dummy', hashed_pwd))

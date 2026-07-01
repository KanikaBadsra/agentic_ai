import unittest

from app.auth.auth import get_current_user


class AuthTests(unittest.TestCase):
    def test_get_current_user_defaults_to_admin_when_no_token_is_provided(self):
        user = get_current_user(None)

        self.assertEqual(user["username"], "anonymous")
        self.assertEqual(user["role"], "Admin")


if __name__ == "__main__":
    unittest.main()

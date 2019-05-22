import unittest
from HelloClearShark import create_string


class TestStringMethod(unittest.TestCase):
    """
    Main unittest class
    """

    def test_string(self):
        """
        Test Create String fom HelloClearShark
        :return:
        """
        cs_str = create_string()
        self.assertEqual(cs_str, "Hello, ClearShark!")


if __name__ == '__main__':
    unittest.main()

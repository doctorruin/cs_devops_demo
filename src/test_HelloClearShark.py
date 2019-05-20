import unittest
import HelloClearShark as cs


class TestStringMethod(unittest.TestCase):

    def test_string(self):
        cs_str = cs.create_string()
        self.assertEquals(cs_str, "Hello ClearShark!")


if __name__ == '__main__':
    unittest.main()

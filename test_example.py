import unittest

class TestTrue(unittest.TestCase):
    def test_true_is_true(self):
        self.assertTrue(True == True)

if __name__ == '__main__':
    unittest.main()

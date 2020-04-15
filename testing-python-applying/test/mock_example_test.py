import unittest
from mock import Mock


class TestMocking(unittest.TestCase):
    def test_mock_method_returns(self):
        myMock = Mock()
        myMock.method.return_value = "hello"
        self.assertEqual("hello", myMock.method())


if __name__ == "__main__":
    unittest.main()

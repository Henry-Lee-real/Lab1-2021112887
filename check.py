import unittest
from lab import queryBridgeWords

class TestMathModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(queryBridgeWords("to", "new"), 
                         "The bridge words from \"to\" to \"new\" are: seek, and day")

if __name__ == '__main__':
    unittest.main()

# self.assertEqual(queryBridgeWords("to", ""), "No \"\" in the graph!")
        # self.assertEqual(queryBridgeWords("got", "new"), "No \"got\" in the graph!")
        # self.assertEqual(queryBridgeWords("got", "sad233"), "No \"got\" and \"sad233\" in the graph!")
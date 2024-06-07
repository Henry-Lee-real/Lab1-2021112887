import unittest
from lab import queryBridgeWords

class TestMathModule(unittest.TestCase):
    def test_add(self):
        print("test1")
        self.assertEqual(queryBridgeWords("to", "new"), 
                         "The bridge words from \"to\" to \"new\" are: seek, and day")
        print("test2")
        self.assertEqual(queryBridgeWords("to", ""), "No \"\" in the graph!")
        print("test3")
        self.assertEqual(queryBridgeWords("got", "new"), "No \"got\" in the graph!")
        print("test4")
        self.assertEqual(queryBridgeWords("got", "sad233"), "No \"got\" and \"sad233\" in the graph!")

if __name__ == '__main__':
    unittest.main()

    """
Liam Byrne (byrneliam2)
PyVUW
"""

import unittest


class AllTests(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_foo(self):
        self.assertEqual(1, 1)
        
if __name__ == "__main__":
    unittest.main()

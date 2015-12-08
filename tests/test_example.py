import unittest
from sequence_database import sequence_database

class Test(unittest.TestCase):
    def test_returns_true(self):
        self.assertEquals(True, sequence_database.returns_true())
        self.assertTrue(sequence_database.returns_true())

    def test_will_pass(self): 
        self.assertTrue(True)   

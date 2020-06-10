import unittest
from balanced import balanced_smiles


class MyTestCase(unittest.TestCase):
    def test_something(self):
        #self.assertEqual("NO", balanced_smiles(":(("))
        #self.assertEqual("YES", balanced_smiles("i am sick today (:()"))
        self.assertEqual("YES", balanced_smiles("(:)"))
        #self.assertEqual("YES", balanced_smiles("hacker cup: started :):)"))
        #self.assertEqual("NO", balanced_smiles(")("))


if __name__ == '__main__':
    unittest.main()

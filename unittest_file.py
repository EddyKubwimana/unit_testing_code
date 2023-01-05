import unittest
import calcul_function as cf

class UniTest( unittest.TestCase):
    def test_add(self):
        """ Test the add function in calcul_function module"""
        result = cf.add(10,5)
        true_result = 10+5
        self.assertEqual(result, true_result)

if __name__ == '__main__':
    unittest.main()

        

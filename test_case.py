import unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('abc'.upper(), 'ABC')

    def test_isupper(self):
        self.assertTrue('ABC'.isupper())
        self.assertFalse('Abc'.isupper())

    def test_spilt(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
'''
if __name__ =='__main__':
    unittest.main()
'''
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(sui
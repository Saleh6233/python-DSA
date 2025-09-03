import unittest
import main


class Testmain(unittest.TestCase):

    def setUp(self):
        print(""" Testing the 'do_stuff' function  in main """)

    def test_do_stuff1(self):
        """
        Testing for integar input

        """
        result = main.do_stuff(10)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        """
        Testing for invalid string

        """
        result = main.do_stuff('avghxgdsjh')
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        """
        Testing for 'None' input

        """
        result = main.do_stuff(None)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        """
        Testing for empty input

        """
        result = main.do_stuff("")
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print("Cleaning up variables")


if __name__ == '__main__':
    unittest.main()

import unittest

from app import Superhero


class TestSuperHero(unittest.TestCase):

    def setUp(self):
        self.superhero = Superhero(name="Batman", strength_level=50)

    def test_stringify(self):

        self.assertEqual(str(self.superhero), "Batman")

    def test_is_stronger_than_other(self):
        other_superhero = Superhero(name="Batman", strength_level=35)

        self.assertTrue(self.superhero.is_stronger_than(other_superhero))
        self.assertFalse(other_superhero.is_stronger_than(self.superhero))

from django.test import TestCase

from .templatetags.blog_tags import pl_genitiv


class PlPluralizeFilterTest(TestCase):

    def test_1(self):
        self.assertEqual(pl_genitiv("post", 1), "post")

    def test_2(self):
        self.assertEqual(pl_genitiv("post", 2), "posty")

    def test_3(self):
        self.assertEqual(pl_genitiv("post", 3), "posty")

    def test_15(self):
        self.assertEqual(pl_genitiv("post", 15), "postów")

    def test_22(self):
        self.assertEqual(pl_genitiv("post", 22), "posty")

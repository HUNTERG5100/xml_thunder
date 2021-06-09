import unittest

from src.xml_thunder import Lightning

xml_parser = Lightning()


@xml_parser.route("foo")
def foo(element):
    print("foo")


class TestLightning(unittest.TestCase):
    def test_getitem(self):
        """
        Tests that the __getitem__ method returns an object or None
        """

        self.assertEqual(xml_parser["foo"], foo)


if __name__ == '__main__':
    unittest.main()

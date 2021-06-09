import unittest

from src.xml_thunder import Lightning

xml_parser = Lightning()


@xml_parser.route("foo")
def foo(element):
    pass


def bar(element):
    pass


class TestLightning(unittest.TestCase):
    def test_get_all_routes(self):
        """
        Tests that the get_all_routes method
        returns all routes with intended items
        """

        # Checks routes before adding extra route
        self.assertEqual(xml_parser.get_all_routes(), {"foo": foo})

        # Adds a route
        xml_parser["bar"] = bar

        # Checks routes after adding extra route
        self.assertEqual(xml_parser.get_all_routes(), {"foo": foo, "bar": bar})

        # Deletes added route
        del xml_parser["bar"]

        # Checks routes after deleting extra route
        self.assertEqual(xml_parser.get_all_routes(), {"foo": foo})

    def test_route(self):
        """
        Tests that the route decorator registers a route
        """

        # Checks routes before changes
        self.assertEqual(xml_parser.get_all_routes(), {"foo": foo})

        # Adds a new route through decoration
        @xml_parser.route("foobar")
        def foobar(element):
            pass

        # Checks routes after changes
        self.assertEqual(
            xml_parser.get_all_routes(), {"foo": foo, "foobar": foobar})

        # Deletes newly added route
        del xml_parser["foobar"]

        # Checks routes after deleting extra route
        self.assertEqual(xml_parser.get_all_routes(), {"foo": foo})


if __name__ == '__main__':
    unittest.main()

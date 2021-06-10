from src.xml_thunder import Lightning


xml_parser = Lightning()


@xml_parser.route("foo")
def foo(element):
    print("Foo element!")


@xml_parser.route("bar")
def bar(element):
    print("Bar element!")


xml_parser.parse("<name-of-xml-document>")

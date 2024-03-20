import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_paragraph(self):
        node = HTMLNode("p", "This is a paragraph", None, None)
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_ahref_target(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, " href=\"https://www.google.com\" target=\"_blank\"")

    def test_repr_paragraph(self):
        node = HTMLNode("p", "This is a paragraph", None, None)
        self.assertEqual("HTMLNode(p, This is a paragraph, None, None)", repr(node))

    def test_repr_href(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        self.assertEqual("HTMLNode(a, None, None, {'href': 'https://www.google.com'})", repr(node))

if __name__ == "__main__":
    unittest.main()
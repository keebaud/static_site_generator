import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_rawtext_leafnode(self):
        node = LeafNode(None, "This is raw text")
        result = node.to_html()
        self.assertEqual(result, "This is raw text")

    def test_p_leafnode(self):
        node = LeafNode("p", "This is a paragraph of text")
        result = node.to_html()
        self.assertEqual(result, "<p>This is a paragraph of text</p>")

    def test_a_leafnode(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        self.assertEqual(result, "<a href=\"https://www.google.com\">Click me!</a>")

    def test_repr_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("HTMLNode(a, Click me!, {'href': 'https://www.google.com'})", repr(node))

if __name__ == "__main__":
    unittest.main()
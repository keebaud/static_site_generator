import unittest

from textnode import TextNode
from textnode import text_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_num(self):
        node = TextNode("Common place text", 3, "https://common.com")
        node2 = TextNode("Common place text", 3, "https://common.com")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("", "italic")
        node2 = TextNode("No", "italic", None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test text", "type text", "url text")
        self.assertEqual("TextNode(Test text, type text, url text)", repr(node))

class TestHTMLNode(unittest.TestCase):
    def test_text_type(self):
        node = TextNode("This is plain text", "text")
        result = text_to_html_node(node)
        self.assertEqual(result, LeafNode(None, "This is plain text", None))

    def test_bold_type(self):
        node = TextNode("This is bold text", "bold")
        result = text_to_html_node(node)
        self.assertEqual(result, LeafNode("b", "This is bold text", None))

    def test_italic_type(self):
        node = TextNode("This is italic text", "italic")
        result = text_to_html_node(node)
        self.assertEqual(result, LeafNode("i", "This is italic text", None))

    def test_code_type(self):
        node = TextNode("This is inline code", "code")
        result = text_to_html_node(node)
        self.assertEqual(result, LeafNode("code", "This is inline code", None))

    def test_link_type(self):
        node = TextNode("This is an HTML link", "link", "https://www.google.com")
        result = text_to_html_node(node)
        self.assertEqual(result, LeafNode("a", "This is an HTML link", {"href": "https://www.google.com"}))

    def test_image_type(self):
        node = TextNode("This is alt text for an image", "image", "image.jpg")
        result = text_to_html_node(node)
        self.assertEqual(result, LeafNode("img", None, {"src": "image.jpg", "alt": "This is alt text for an image"}))

    def test_exception(self):
        node = TextNode("This should break it", "break")
        with self.assertRaises(Exception):
            text_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode

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

if __name__ == "__main__":
    unittest.main()
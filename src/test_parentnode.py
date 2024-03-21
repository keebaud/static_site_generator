import unittest

from htmlnode import ParentNode
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_rawtext_leafnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = node.to_html()
        self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_repr_href(self):
        node = ParentNode("p", [ LeafNode("b", "Bold text")])
        self.assertEqual("ParentNode(p, [HTMLNode(b, Bold text, None)], None)", repr(node))

if __name__ == "__main__":
    unittest.main()
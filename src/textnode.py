from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return (
            self.text == other_node.text and
            self.text_type == other_node.text_type and
            self.url == other_node.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    raise Exception(f"text type {text_node.text_type} not recognised")
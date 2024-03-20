from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
    proplist = HTMLNode.props_to_html(node)
    print(proplist)

main()
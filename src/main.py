from textnode import TextNode
from htmlnode import HTMLNode
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links
)

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    node = HTMLNode("a", None, None, {"href": "https://www.google.com", "target": "_blank"})
    proplist = HTMLNode.props_to_html(node)
    print(proplist)

    print("Testing markdown image extraction")
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))

main()
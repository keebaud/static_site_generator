from textnode import TextNode
from htmlnode import HTMLNode
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    text_to_textnodes
)
from markdown_blocks import markdown_to_blocks

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

    node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            "text",
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)

    test_text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    print(text_to_textnodes(test_text))

    test_string = "This is **bolded** paragraph\n\nThis is another paragraph with *italic text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
    print(markdown_to_blocks(test_string))

main()
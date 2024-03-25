import re

from textnode import (
    TextNode,
    text_type_text
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for process_node in old_nodes:
        if process_node.text_type == text_type_text:
            split_node_text = process_node.text.split(delimiter)
            if len(split_node_text) % 2 == 0:
                raise Exception(f"Unmatched delimiter located in text - {process_node.text}")
            for index, value in enumerate(split_node_text):
                if value == "":
                    continue
                if index % 2 == 0:
                    new_nodes.append(TextNode(value, text_type_text))
                else:
                    new_nodes.append(TextNode(value, text_type))
        else:
            new_nodes.append(process_node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)]\((.*?)\)", text)
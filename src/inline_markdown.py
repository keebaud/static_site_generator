import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic,
    text_type_code
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for process_node in old_nodes:
        if process_node.text_type == text_type_text:
            split_node_text = process_node.text.split(delimiter)
            if len(split_node_text) % 2 == 0:
                raise ValueError(f"Unmatched delimiter located in text - {process_node.text}")
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for process_node in old_nodes:
        if process_node.text_type == text_type_text:
            text_extract = process_node.text
            image_extract = extract_markdown_images(process_node.text)
            if not image_extract:
                new_nodes.append(process_node)
            else:
                for image in image_extract:
                    sections = text_extract.split(f"![{image[0]}]({image[1]})", 1)
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown. Image section not closed")
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                    new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                    text_extract = sections[1]
                if text_extract != "":
                    new_nodes.append(TextNode(text_extract, text_type_text))
        else:
            new_nodes.append(process_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for process_node in old_nodes:
        if process_node.text_type == text_type_text:
            text_extract = process_node.text
            link_extract = extract_markdown_links(process_node.text)
            if not link_extract:
                new_nodes.append(process_node)
            else:
                for link in link_extract:
                    sections = text_extract.split(f"[{link[0]}]({link[1]})", 1)
                    if len(sections) != 2:
                         raise ValueError("Invalid markdown. Link section not closed")                       
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                    new_nodes.append(TextNode(link[0], text_type_link, link[1]))
                    text_extract = sections[1]
                if text_extract != "":
                    new_nodes.append(TextNode(text_extract, text_type_text))
        else:
            new_nodes.append(process_node)
    return new_nodes

def text_to_textnodes(text):
    output = [TextNode(text, text_type_text)]
    output = split_nodes_delimiter(output, "**", text_type_bold)
    output = split_nodes_delimiter(output, "*", text_type_italic)
    output = split_nodes_delimiter(output, "`", text_type_code)
    output = split_nodes_image(output)
    output = split_nodes_link(output)
    return output
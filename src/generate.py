import os

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    markdown_lines = markdown.split("\n")
    if not markdown_lines[0].startswith("# "):
        raise Exception("Invalid markdown. Must begin with header")
    return markdown_lines[0][2:].strip()

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()

    markdown_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_src = os.path.join(dir_path_content, item)
        if os.path.isfile(item_src):
            if item_src.endswith(".md"):
                dest_filepath = os.path.join(dest_dir_path, item[:-3] + ".html")
                generate_page(item_src, template_path, dest_filepath)
        elif os.path.isdir(item_src):
            subdir_dst = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_src, template_path, subdir_dst)
        
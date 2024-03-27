import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    return_list = []
    addto_list = []
    for line in markdown.splitlines():
        stripped_line = line.strip()
        if stripped_line == "":
            if len(addto_list) > 0:
                return_list.append("\n".join(addto_list))
            addto_list = []
        else:
            addto_list.append(stripped_line)
    if len(addto_list) > 0:
        return_list.append("\n".join(addto_list))
    return return_list

def block_to_block_type(block):
    lines = block.split("\n")
    if re.match(r"^#{1,6}\s", block):
        return block_type_heading
    if len(lines) > 1 and lines[0].strip() == "```" and lines[-1].strip() == "```":
                return block_type_code
    if re.match(r"^>", block, re.MULTILINE):
        return block_type_quote
    if re.match(r"^[*-]\s", block, re.MULTILINE):
        return block_type_ulist
    if re.match(r"^\d+\.\s", block, re.MULTILINE):
        valid = True
        for index, line in enumerate(lines):
            if not line.startswith(f"{index + 1}"):
                valid = False
        if valid:
            return block_type_olist
    return block_type_paragraph
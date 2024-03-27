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
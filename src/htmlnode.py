class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        # A string representing the HTML tag name (eg. "p", "a", "h1", etc.)
        # None represents raw text
        self.tag = tag
        # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        # None will assume it has children
        self.value = value
        # A list of HTMLNode objects representing the children of the node
        # None will assume to have a value
        self.children = children
        # A dictionary of key-value pairs representing the attributes of the html tag.
        # For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        # None won't have any attributes
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")
        # Child classes will override this method
    
    def props_to_html(self):
        # Return empty string if self.props is None
        if self.props is None:
            return ""
        # Return a string that represents the HTML attributes of the node
        return_props = ""
        for key, value in self.props.items():
            return_props += f" {key}=\"{value}\""
        return return_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    # A leaf has no children, so leaves are not defining children
    def __init__(self, tag, value, props = None):
        # x=x inherits the definition in HTMLNode. Self is not required
        super().__init__(tag=tag, props=props)
        # value is added separately. This isolates value within the LeafNode for processing
        self.value = value

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, props=props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node requires a tag")
        if self.children is None:
            raise ValueError("Parent node requires children")
        return_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            return_string += child.to_html()
        return_string += f"</{self.tag}>"
        return return_string

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
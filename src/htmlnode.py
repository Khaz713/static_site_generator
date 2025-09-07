

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  #string, HTML tag
        self.value = value  #string, value of the HTML tag
        self.children = children    #list, HTMLNode objects
        self.props = props  #dict, attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError("Not implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""
        html = ""
        for prop in self.props.items():
            html += f' {prop[0]}="{prop[1]}"'
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"




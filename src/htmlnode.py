

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


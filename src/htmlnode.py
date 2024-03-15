class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = []
        for key in self.props:
            value = self.props[key]
            attributes.append(f" {key}=\"{value}\"")
        return ''.join(attributes)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if value == None:
            raise ValueError ("All leaf nodes require a value.")
        if tag == None:
            return self.value
        else: 
            return f"<{self.tag}{self.props_to_html}>{self.value}</{self.tag}"
        
    def __repr__(self):
        return f"LeadNode({self.tag}, {self.value}, {self.props})"
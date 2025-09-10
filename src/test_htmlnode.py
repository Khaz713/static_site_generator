import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        html_node1 = HTMLNode(
            "div",
            "test",
            None,
            None,
        )
        self.assertEqual(html_node1.tag, "div")
        self.assertEqual(html_node1.value, "test")
        self.assertEqual(html_node1.children, None)
        self.assertEqual(html_node1.props, None)

    def test_props_to_html(self):
        html_node1 = HTMLNode(
            "div",
            "test",
            None,
            {"class": "test", "href": "https://test.com"}
        )
        self.assertEqual(html_node1.props_to_html(), ' class="test" href="https://test.com"')

    def test_repr(self):
        html_node1 = HTMLNode(
            "div",
            "test",
            None,
            {"class": "test"}
        )
        self.assertEqual(html_node1.__repr__(), "HTMLNode(div, test, None, {'class': 'test'})")

    def test_leaf_to_html(self):
        leaf_node = LeafNode("p", "Hello World!")
        self.assertEqual(leaf_node.to_html(), "<p>Hello World!</p>")

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
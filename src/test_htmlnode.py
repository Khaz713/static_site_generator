import unittest

from htmlnode import HTMLNode

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


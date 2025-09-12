import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        text_node1 = TextNode('text', TextType.BOLD)
        text_node2 = TextNode('text', TextType.BOLD)
        text_node3 = TextNode('text', TextType.BOLD, None)
        text_node4 = TextNode('text', TextType.BOLD, "https://docs.python.org/3/library/enum.html")
        text_node5 = TextNode('text', TextType.BOLD, "https://docs.python.org/3/library/enum.html")
        self.assertEqual(text_node1, text_node2, "Same text and type")
        self.assertEqual(text_node1, text_node3, "Same text and type and url correctly defaulted to None")
        self.assertEqual(text_node4, text_node5, "Same text, type and url")

    def test_neq(self):
        text_node1 = TextNode('text', TextType.BOLD)
        text_node2 = TextNode('text1', TextType.BOLD)
        text_node3 = TextNode('text', TextType.ITALIC)
        text_node4 = TextNode('text', TextType.BOLD, "https://docs.python.org/3/library/enum.html")
        text_node5 = TextNode('text2', TextType.ITALIC, "https://www.markdownguide.org/cheat-sheet")
        self.assertNotEqual(text_node1, text_node2, "Different text")
        self.assertNotEqual(text_node1, text_node3, "Different type")
        self.assertNotEqual(text_node2, text_node3, "Different text and type")
        self.assertNotEqual(text_node1, text_node4, "Different url")
        self.assertNotEqual(text_node4, text_node5, "Different text, type and url")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")



if __name__ == '__main__':
    unittest.main()

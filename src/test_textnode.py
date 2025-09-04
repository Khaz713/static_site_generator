import unittest

from textnode import TextNode, TextType

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


if __name__ == '__main__':
    unittest.main()
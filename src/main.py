from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("This is text with a **bold** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
    print(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    print(new_nodes)


if __name__ == "__main__":
    main()

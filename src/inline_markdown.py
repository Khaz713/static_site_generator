from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in ["**", "_", "`"]:
        raise ValueError(f"{delimiter} is not a valid delimiter")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text.split(delimiter)
            if len(node_text) % 2 == 1:
                for i in range(len(node_text)):
                    if node_text[i] == "":
                        continue
                    if i % 2 == 0:
                        new_nodes.append(TextNode(node_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(node_text[i], text_type))
            else:
                raise ValueError("invalid markdown, formatted section not closed")

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_url(old_nodes, text_type):
    new_nodes = []
    node_urls = None
    for node in old_nodes:
        match text_type:
            case TextType.IMAGE:
                node_urls = extract_markdown_images(node.text)
            case TextType.LINK:
                node_urls = extract_markdown_links(node.text)
        if len(node_urls) <= 0:
            new_nodes.append(node)
        else:
            node_text = node.text
            for i in range(len(node_urls)):
                text_split = None
                match text_type:
                    case TextType.IMAGE:
                        text_split = node_text.split(f"![{node_urls[i][0]}]({node_urls[i][1]})", 1)
                    case TextType.LINK:
                        text_split = node_text.split(f"[{node_urls[i][0]}]({node_urls[i][1]})", 1)
                new_nodes.append(TextNode(text_split[0], TextType.TEXT))
                new_nodes.append(TextNode(node_urls[i][0], text_type, node_urls[i][1]))
                if len(text_split) > 1:
                    node_text = text_split[1]
                else:
                    node_text = ""
            if node_text != "":
                new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    text_nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_url(text_nodes, TextType.IMAGE)
    text_nodes = split_nodes_url(text_nodes, TextType.LINK)
    return text_nodes




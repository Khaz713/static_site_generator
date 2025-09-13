from htmlnode import *
from textnode import *
from inline_markdown import text_to_textnodes
from block_markdown import markdown_to_blocks, BlockType, block_to_block_type
import re


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    header_value = len(re.findall(r"#+ ", block)[0].strip())
    if header_value > 6:
        raise ValueError("Heading too high")
    return ParentNode(f"h{header_value}", text_to_children(block[header_value + 1:]))

def quote_to_html_node(block):
    lines = block.split('\n')
    text = []
    for line in lines:
        text.append(line.strip('>').strip())
    text = " ".join(text)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split('\n')
    list_points = []
    for line in lines:
        list_points.append(ParentNode("li", text_to_children(line.strip('-').strip())))
    return ParentNode("ul", list_points)

def ordered_list_to_html_node(block):
    lines = block.split('\n')
    list_points = []
    for idx, line in enumerate(lines, start=1):
        list_points.append(ParentNode("li", text_to_children(line.strip(f'{idx}. ').strip())))
    return ParentNode("ol", list_points)

def code_to_html_node(block):
    text_node = TextNode(block[4:-3], TextType.TEXT)
    child = text_node_to_html_node(text_node)
    return ParentNode("pre", [ParentNode("code", [child])])

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        block_node = None
        match block_type:
            case BlockType.PARAGRAPH:
                block_node = paragraph_to_html_node(block)
            case BlockType.HEADING:
                block_node = heading_to_html_node(block)
            case BlockType.QUOTE:
                block_node = quote_to_html_node(block)
            case BlockType.UNORDERED:
                block_node = unordered_list_to_html_node(block)
            case BlockType.ORDERED:
                block_node = ordered_list_to_html_node(block)
            case BlockType.CODE:
                block_node = code_to_html_node(block)
        html_blocks.append(block_node)

    return ParentNode("div", html_blocks)

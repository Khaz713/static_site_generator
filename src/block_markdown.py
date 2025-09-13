import textwrap
import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED = 5
    ORDERED = 6

def markdown_to_blocks(markdown):
    markdown = textwrap.dedent(markdown).strip()
    markdown = re.sub(r'\n{2,}", "\n\n', '', markdown)
    blocks = markdown.split('\n\n')
    blocks_final =[]
    for block in blocks:
        block = block.strip()
        if block != '':
            blocks_final.append(block)
    return blocks_final

RE_HEADING = re.compile(r'^#{1,6} [^\n]+$')
RE_CODE = re.compile(r'^```[\s\S]*?```$', re.DOTALL)
RE_QUOTE = re.compile(r'^(?:> [^\r\n]+(?:\r?\n)?)+$')
RE_UNORDERED = re.compile(r'^(?:- [^\n]+\n?)+$', re.MULTILINE)
RE_ORDERED = re.compile(r'^(?:\d+\. [^\n]+\n?)+$', re.MULTILINE)

def block_to_block_type(block):

    if RE_HEADING.match(block):
        return BlockType.HEADING
    if RE_CODE.match(block):
        return BlockType.CODE
    if RE_QUOTE.fullmatch(block):
        return BlockType.QUOTE
    if RE_UNORDERED.match(block):
        return BlockType.UNORDERED
    if RE_ORDERED.match(block):
        lines = block.splitlines()
        for idx, line in enumerate(lines, start=1):
            if not line.startswith(f'{idx}. '):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED
    return BlockType.PARAGRAPH
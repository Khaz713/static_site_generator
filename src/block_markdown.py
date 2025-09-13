import textwrap
import re

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks_final =[]
    for block in blocks:
        block = textwrap.dedent(block)
        if block != '':
            blocks_final.append(block.strip())
    return blocks_final
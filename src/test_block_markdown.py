import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
    This is **bolded** paragraph




    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

# Heading
    def test_heading_basic(self):
        self.assertEqual(block_to_block_type("# Title"), BlockType.HEADING)

    def test_heading_levels_1_to_6(self):
        for n in range(1, 7):
            self.assertEqual(block_to_block_type("#" * n + " Heading"), BlockType.HEADING)

    def test_heading_reject_no_space(self):
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)

    def test_heading_reject_too_many_hashes(self):
        self.assertEqual(block_to_block_type("####### too many"), BlockType.PARAGRAPH)

    # Code
    def test_code_block_simple(self):
        block = "```\ncode line\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_multiline(self):
        block = "```\nline1\nline2\nline3\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_reject_unclosed(self):
        block = "```\nno close"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_with_language_hint(self):
        block = "```python\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    # Quote
    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> wisdom"), BlockType.QUOTE)

    def test_quote_multi_line_all_prefixed(self):
        block = "> one\n> two\n> three"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_reject_missing_prefix_on_any_line(self):
        block = "> good\nbad"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_allow_empty_quoted_lines(self):
        block = "> line\n> \n> next"
        # If you disallow empty lines in your impl, change expected to PARAGRAPH
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Unordered list
    def test_unordered_basic(self):
        block = "- item1\n- item2\n- item3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED)

    def test_unordered_single_line(self):
        self.assertEqual(block_to_block_type("- item"), BlockType.UNORDERED)

    def test_unordered_reject_wrong_bullet(self):
        block = "+ item\n- item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_reject_missing_space(self):
        block = "-item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Ordered list
    def test_ordered_basic(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED)

    def test_ordered_single_line(self):
        self.assertEqual(block_to_block_type("1. only"), BlockType.ORDERED)

    def test_ordered_reject_bad_start_number(self):
        block = "2. first\n3. second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_reject_non_incrementing(self):
        block = "1. one\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_reject_missing_space(self):
        block = "1.one"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Paragraph / fallback
    def test_paragraph_simple(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph."), BlockType.PARAGRAPH)

    def test_paragraph_multiple_lines_no_list_markers(self):
        block = "Line one\nLine two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

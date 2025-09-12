from textnode import TextNode, TextType

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
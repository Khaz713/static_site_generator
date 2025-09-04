from textnode import TextNode, TextType

def main():
    test = TextNode("Anchor text", TextType.link, "https://docs.python.org/3/library/enum.html")
    print(test)


if __name__ == "__main__":
    main()

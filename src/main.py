from textnode import TextNode
from textnode import TextType


def main():
    node = TextNode("anchor", TextType.LINK, "http://127.0.0.1")
    print(f"created TextNode with {node.text}, etc.")
    print(node.__repr__())


main()

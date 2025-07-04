from enum import Enum

class TextNode(Enum):
    TEXT = 1
    TYPE = 2
    URL = 3

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

def __repr__(self):
        return (f"TextNode(text={self.text!r}, "
                f"text_type={self.text_type!r}, "
                f"url={self.url!r})")
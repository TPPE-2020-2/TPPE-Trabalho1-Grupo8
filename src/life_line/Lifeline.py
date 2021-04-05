import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Lifeline(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<Lifeline %s />'
        self.terminal = True
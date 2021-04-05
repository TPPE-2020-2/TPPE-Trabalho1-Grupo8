import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Message(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<Message %s/>'
        self.terminal = True
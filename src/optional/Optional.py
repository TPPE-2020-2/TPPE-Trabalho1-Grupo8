import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Optional(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<Optional %s/>'
        self.terminal = True
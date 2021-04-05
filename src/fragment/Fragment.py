import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Fragment(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<Fragment %s/>'
        self.terminal = True
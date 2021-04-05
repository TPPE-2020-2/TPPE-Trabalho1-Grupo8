import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class StartNode(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<StartNode %s/>'
        self.terminal = True
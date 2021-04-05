import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class FinalNode(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<FinalNode %s/>'
        self.terminal = True 
import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class ActivityNode(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<ActivityNode %s/>'
        self.terminal = True
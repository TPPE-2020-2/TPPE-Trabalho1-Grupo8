import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class DecisionNode(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<DecisionNode %s/>'
        self.terminal = True
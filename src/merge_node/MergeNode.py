import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class MergeNode(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<MergeNode %s/>'
        self.terminal = True
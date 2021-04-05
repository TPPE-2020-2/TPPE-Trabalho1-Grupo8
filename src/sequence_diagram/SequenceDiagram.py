import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class SequenceDiagram(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<SequenceDiagram %s>'
        self.close_tag = '</SequenceDiagram>'
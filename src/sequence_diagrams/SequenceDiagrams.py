import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class SequenceDiagrams(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<SequenceDiagrams>'
        self.close_tag = '</SequenceDiagrams>'
import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Fragments(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<Fragments>'
        self.close_tag = '</Fragments>'
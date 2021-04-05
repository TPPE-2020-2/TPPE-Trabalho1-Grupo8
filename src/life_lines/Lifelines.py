import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Lifelines(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<Lifelines >'
        self.close_tag = '</Lifelines>'
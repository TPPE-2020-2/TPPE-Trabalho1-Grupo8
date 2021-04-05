import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class ActivityDiagram(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<ActivityDiagram %s>'
        self.close_tag = '</ActivityDiagram>'
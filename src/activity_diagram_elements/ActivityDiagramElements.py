import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class ActivityDiagramElements(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<ActivityDiagramElements %s>'
        self.close_tag = '</ActivityDiagramElements>'
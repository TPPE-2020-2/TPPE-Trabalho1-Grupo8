import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class ActivityDiagramTransitions(TypeTag):
    def __init__(self):
        super().__init__()
        self.open_tag = '<ActivityDiagramTransitions %s>'
        self.close_tag = '</ActivityDiagramTransitions>'
import sys
sys.path.append("..")
from type_tag.TypeTag import TypeTag

class Transition(TypeTag):
    def __init__(self, source, target):
        super().__init__()
        self.open_tag = '<Transition %s/>'
        self.terminal = True
        self.source = []
        self.target = []
        
class TransitionFromDecisionNode(Transition):
    def __init__(self, source, target):
        super().__init__(source, target)
        self.create_transition(source, target)

    def create_transition(self, source, target):
            if(len(source)==1):
                for t in target:
                    self.target.append(t.id)
            else:
                raise Exception("ActivityDiagramRuleException")
class TransitionToMergeNode(Transition):
    def __init__(self, source, target):
        super().__init__(source, target)
        self.create_transition(source, target)

    def create_transition(self, source, target):
        if (len(target) == 1):
            for s in source:
                self.source.append(s.id)
        else:
            raise Exception("ActivityDiagramRuleException")
class TransitionFromStartNode(Transition):
    def __init__(self, source, target):
        super().__init__(source, target)
        self.create_transition(target)

    def create_transition(self, target):
        if (len(target) == 1):
            self.target = target[0].id
        else:
            raise Exception("ActivityDiagramRuleException")

class TransitionToFinalNode(Transition):
    def __init__(self, source, target):
        super().__init__(source, target)
        self.create_transition(target)

    def create_transition(self, target):
        if (len(target) == 1):
            self.target = target[0].id
        else:
            raise Exception("ActivityDiagramRuleException")

class CommonTransition(Transition):
    def __init__(self, source, target):
        super().__init__(source, target)
        self.create_transition(target)

    def create_transition(self, target):
        for t in target:
            self.target.append(t.id)

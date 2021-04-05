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
        self.create_transition(source, target)
    def create_transition(self, source, target):
        from decision_node.DecisionNode import DecisionNode
        from merge_node.MergeNode import MergeNode
        from start_node.StartNode import StartNode
        from final_node.FinalNode import FinalNode
        if(isinstance(source[0], DecisionNode)):
            if(len(source)==1):
                for t in target:
                    self.target.append(t.id)
            else:
                raise Exception("ActivityDiagramRuleException")
        elif(isinstance(target[0], MergeNode)):
            if(len(target) == 1):
                for s in source:
                    self.source.append(s.id)
            else:
                raise Exception("ActivityDiagramRuleException")
        elif(isinstance(source[0], StartNode)):
            if(len(target)==1):
                self.target = target[0].id
            else:
                raise Exception("ActivityDiagramRuleException")
        elif(isinstance(target[0], FinalNode)):
            if(len(target)==1):
                self.target = target[0].id
            else:
                raise Exception("ActivityDiagramRuleException")
import sys
sys.path.append("..")
from seq.seq import Seq
sequence = Seq()

class TypeTag:
    def __init__(self):
        self.children = []
        self.attr = {}
        self.open_tag = ''
        self.close_tag = ''
        self.terminal = False
        self.id = str(sequence.next_id())
    def add_child(self, child):
        self.check_start_node(child)
        self.children.append(child)

    def check_start_node(self, child):
        from start_node.StartNode import StartNode
        if (isinstance(child, StartNode)):
            for self_child in self.children:
                if (isinstance(self_child, StartNode)):
                    raise Exception("ActivityDiagramRuleException")

    def set_attr(self, attr):
        self.attr = attr


def add_children(current_children, children):
    from start_node.StartNode import StartNode
    for child in children:
        if(isinstance(child, StartNode)):
            for current_children_iterated in current_children:
                if(isinstance(current_children_iterated, StartNode)):
                    raise Exception("ActivityDiagramRuleException")
    current_children += children
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
        from start_node.StartNode import StartNode
        if(isinstance(child, StartNode)):
            for self_child in self.children:
                    if(isinstance(self_child, StartNode)):
                        raise Exception("ActivityDiagramRuleException")
        self.children.append(child)

    def set_attr(self, attr):
        self.attr = attr
    def get_child_xml(self):
        attributes = []
        if (self.terminal):
            attributes = ['id='+self.id]
        for attr in self.attr:
            attributes.append(attr+"='"+self.attr[attr]+"'")
        if(self.terminal):
            return self.open_tag.replace('%s', ' '.join(attributes))
        else:
            xml = [self.open_tag.replace('%s', ' '.join(attributes))]
            for child in self.children:
                xml.append(child.get_child_xml())
            xml.append(self.close_tag)
            return '\n'.join(xml)


def add_children(current_children, children):
    from start_node.StartNode import StartNode
    for child in children:
        if(isinstance(child, StartNode)):
            for current_children_iterated in current_children:
                if(isinstance(current_children_iterated, StartNode)):
                    raise Exception("ActivityDiagramRuleException")
    current_children += children
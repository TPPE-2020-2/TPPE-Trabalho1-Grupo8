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
    def add_children(self, children):
        from start_node.StartNode import StartNode
        for child in children:
            if(isinstance(child, StartNode)):
                for self_child in self.children:
                    if(isinstance(self_child, StartNode)):
                        raise Exception("ActivityDiagramRuleException")
        self.children += children
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
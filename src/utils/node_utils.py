class NodeUtils:
    def get_child_xml(self, terminal, id1, attr1, open_tag, children, close_tag):
        attributes = []
        if (terminal):
            attributes = ['id=' + id1]
        for attr in attr1:
            attributes.append(attr +"='" + attr1[attr] + "'")
        if(terminal):
            return open_tag.replace('%s', ' '.join(attributes))
        else:
            xml = [open_tag.replace('%s', ' '.join(attributes))]
            for child in children:
                xml.append(
                    self.get_child_xml(child.terminal, child.id, child.attr, child.open_tag, child.children, child.close_tag))
            xml.append(close_tag)
            return '\n'.join(xml)
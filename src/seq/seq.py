class Seq:
    def __init__(self):
        self.next = 0
    def next_id(self):
        self.next+=1
        return self.next
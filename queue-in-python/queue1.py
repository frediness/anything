class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        max = 0
        for i in range(len(self.qlist)):
            x = self.qlist[max].priority
            if self.qlist[i].priority < max:
                max = self.qlist[i].priority
        item = self.qlist[max]
        del self.qlist[max]
        return item
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[-1]

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        
S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)

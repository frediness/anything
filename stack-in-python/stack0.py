class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

def cetakBiner(d):
    f = Stack()

    if d == 0:
        f.push(0)

    while d != 0:
        sisa = d % 2
        d = d // 2
        f.push(sisa)

    st = ""

    for i in range(len(f)):
        st = st + str(f.pop())

    return st
print("================================")
#1
print("1.")
def cetakHex(d):
    f = Stack()
    div = "0123456789ABCDEF"

    while d > 0:
        rem = d % 16
        f.push(rem)
        d = d // 16

    st = ""
    while not f.isEmpty():
        st = st + div[f.pop()]

    return st
print(cetakHex(55))
print("================================")
#2
print("2.")
for i in range(16):
	if i%3 == 0:
		print(i,'push')		
print("================================")
#3
print("3.")
for i in range(16):
	if i%3 == 0:
		print(i,'push')
	elif i%4 == 0:
		print('pop')

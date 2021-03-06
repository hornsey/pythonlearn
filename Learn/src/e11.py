class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName

    def __repr__(self):
        return "<Node '{}'>".format(self.sName)

    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)

    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()

    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)


oRoot = Node('root')
oChild1 = Node('child1')
oChild2 = Node('child2')
oChild3 = Node('child3')
oChild4 = Node('child4')
oChild5 = Node('child5')
oChild6 = Node('child6')
oChild7 = Node('child7')
oChild8 = Node('child8')


oRoot.append(oChild1)
oRoot.append(oChild2)
oChild1.append(oChild3)
oChild1.append(oChild4)
oChild2.append(oChild5)
oChild2.append(oChild6)
oChild2.append(oChild7)
oChild2.append(oChild8)


oRoot.print_all_1()

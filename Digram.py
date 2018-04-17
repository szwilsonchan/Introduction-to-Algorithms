import random
import math

class MyQueue(object):

    def __init__(self,qlen):
        self.a = [None]*qlen
        self.qhead=0
        self.qtail=0
        self.isfull=False
        self.isempty=True
   
    def enqueue(self,v):
        if self.isfull:
            return "isfull"
        self.a[self.qtail]=v
        if (self.qtail+1)==len(self.a):
            self.qtail=0
        else:
            self.qtail=self.qtail+1

        self.isempty=False
        
        if self.qhead==self.qtail:
            self.isfull=True

    def dequeue(self):
        if self.isempty:
            return "isempty"
        else:
            v=self.a[self.qhead]
            
        if (self.qhead+1)==len(self.a):
            self.qhead=0
        else:
            self.qhead=self.qhead+1

        self.isfull=False
        
        if self.qhead==self.qtail:
            self.isempty=True

        return v

class MyList(object):

    def __init__(self):
        self.lhead=None
    def insert(self,v):
        if self.lhead==None:
           self.lhead=v
        else:
           v.lnext=self.lhead
           (self.lhead).lprev=v
           self.lhead=v
    def delete(self,v):
        if self.lhead==v:
            if v.lnext!=None:
                (v.lnext).lprev=None
            self.lhead=v.lnext
        else:
            if (v.lprev)!=None:
                (v.lprev).lnext=v.lnext
            if (v.lnext)!=None:    
                (v.lnext).lprev=v.lprev
    def search(self,k):
        a=self.lhead
        if a==None:
            return a
        
        if a.key==k:
            return a

        while a.lnext!=None:
            a=a.lnext
            if a.key==k:
                return a

        return None
    
    def getList(self):
        l=[]
        a=self.lhead
        if a!=None:
            l.append(a)
        else:
            return None
        
        while a.lnext!=None:
            a=a.lnext
            l.append(a)
            
        return l

    def printList(self):
        a=self.lhead
        if a!=None:
            print(a.key)
        else:
            print("isempty")
            return
        while a.lnext!=None:
            a=a.lnext
            print(a.key)

    @staticmethod
    def test():
        print("begin test list")
        myList = MyList()
        v = MyListNode(1)
        myList.insert(v)
        v = MyListNode(2)
        myList.insert(v)
        v = MyListNode(3)
        myList.insert(v)
        if myList.search(1)!=None:
            myList.delete(myList.search(1))
        myList.delete(myList.search(2))
        myList.delete(myList.search(3))
        v = MyListNode(4)
        myList.insert(v)
        myList.printList()
        
class MyListNode(object):
    def __init__(self,k):
        self.lprev=None
        self.lnext=None
        self.key=k
        
#广度搜索
class BFSSearch(object):
    def __init__(self):
    
        self.nlist=[]
        self.nlist=['s','r','v','w','t','x','u','y']
        self.elist=[]
        self.elist.append([0,1,0,1,0,0,0,0])
        self.elist.append([1,0,1,0,0,0,0,0])
        self.elist.append([0,1,0,0,0,0,0,0])
        self.elist.append([1,0,0,0,1,1,0,0])
        self.elist.append([0,0,0,1,0,1,1,0])
        self.elist.append([0,0,0,1,1,0,1,1])
        self.elist.append([0,0,0,0,1,1,0,1])
        self.elist.append([0,0,0,0,0,1,1,0])

        self.nodes=[]
        for i in range(len(self.nlist)):
            self.nodes.append(BFSNode(self.nlist[i]))

        self.edges=[[0 for i in range(2)] for j in range(len(self.nodes))]
        for i in range(len(self.edges)):
            self.edges[i][0]=self.nodes[i]
            myList = MyList()
            for j in range(len(self.elist[i])-1,-1,-1):
                if self.elist[i][j]==1:
                    myList.insert(MyListNode(self.nodes[j]))
            self.edges[i][1]= myList
        
    def getnextedges(self,u):
        for i in range(len(self.edges)):
            if self.edges[i][0].k==u.k:
                return (self.edges[i][1]).getList()

    def isedges(self,u,v):
        for i in range(len(self.edges)):
            if self.edges[i][0].k==u.k:
                t = (self.edges[i][1]).list()
                for j in range(len(t)):
                    if (t[j]).k==v.k:
                        return True

        return False

    def search(self):
        self.nodes[0].color="gray"
        self.nodes[0].d=0
        myQueue=MyQueue(100)
        myQueue.enqueue(self.nodes[0])
        while myQueue.isempty!=True:
            u=myQueue.dequeue()
            vs=self.getnextedges(u)
            for i in range(len(vs)):
                if vs[i].key.color=="white":
                    vs[i].key.color="gray"
                    vs[i].key.parent=u
                    vs[i].key.d=u.d+1
                    myQueue.enqueue(vs[i].key)
            u.color="black"

    def print(self):
        for i in range(len(self.nodes)):
            if self.nodes[i].parent!=None:
                print(str(self.nodes[i].k) + " c:" + str(self.nodes[i].color)+ " d:" + str(self.nodes[i].d)+ " p:" + str(self.nodes[i].parent.k)) 
            else:
                print(str(self.nodes[i].k) + " c:" + str(self.nodes[i].color)+ ":" + str(self.nodes[i].d)) 

    @staticmethod                
    def test():
        bfsSearch=BFSSearch()
        bfsSearch.search()
        bfsSearch.print()
        
class BFSNode(object):
    def __init__(self,k):
        self.d=None
        self.k=k
        self.color="white"
        self.parent=None

#BFSSearch.test()

#广度搜索
class DFSSearch(object):
    def __init__(self):
    
        self.nlist=[]
        self.nlist=['u','v','w','x','y','z']
        self.elist=[]
        self.elist.append([0,1,0,1,0,0])
        self.elist.append([0,0,0,0,1,0])
        self.elist.append([0,0,0,0,1,1])
        self.elist.append([0,1,0,0,0,0])
        self.elist.append([0,0,0,1,0,0])
        self.elist.append([0,0,0,0,0,1])

        self.time=0
        self.sortlist=[]

        self.nodes=[]
        for i in range(len(self.nlist)):
            self.nodes.append(DFSNode(self.nlist[i]))

        self.edges=[[0 for i in range(2)] for j in range(len(self.nodes))]
        for i in range(len(self.edges)):
            self.edges[i][0]=self.nodes[i]
            myList = MyList()
            for j in range(len(self.elist[i])-1,-1,-1):
                if self.elist[i][j]==1:
                    myList.insert(MyListNode(self.nodes[j]))
            self.edges[i][1]= myList
            
        self.strong_nodes=[]
        self.strong_elist=[]
        self.strong_edges=[]

    def strong_digram(self):

        for i in range(len(self.nodes)):
            self.nodes[i].color="white"
            self.nodes[i].d=None
            self.nodes[i].f=None
            self.nodes[i].parent=None

        self.search(None);

        for i in range(len(self.nodes)):
            self.strong_nodes.append(self.nodes[i])

        #转置
        self.trans_elist=[[0 for i in range(len(self.nodes))] for j in range(len(self.nodes))]
        for i in range(len(self.elist)):
            for j in range(len(self.elist)):
                self.trans_elist[i][j]=self.elist[j][i]
                
        self.trans_edges=[[0 for i in range(2)] for j in range(len(self.nodes))]
        for i in range(len(self.trans_edges)):
            self.trans_edges[i][0]=self.nodes[i]
            myList = MyList()
            for j in range(len(self.trans_elist[i])-1,-1,-1):
                if self.trans_elist[i][j]==1:
                    myList.insert(MyListNode(self.nodes[j]))
            self.trans_edges[i][1]= myList

        for i in range(len(self.nodes)):
            self.nodes[i].color="white"
            self.nodes[i].d=None
            self.nodes[i].f=None
            self.nodes[i].parent=None
            
        for i in range(len(self.sortlist)-1,-1,-1):
            self.strong_search(self.sortlist[i])

        self.strong_elist=[[0 for i in range(len(self.strong_nodes))] for j in range(len(self.strong_nodes))]
        for i in range(len(self.strong_nodes)):
            for j in range(len(self.strong_nodes)):
                if self.strong_isedges(self.strong_nodes[i],self.strong_nodes[j]):
                    self.strong_elist[i][j]=1

        self.strong_edges=[[0 for i in range(2)] for j in range(len(self.strong_nodes))]
        for i in range(len(self.strong_edges)):
            self.strong_edges[i][0]=self.strong_nodes[i]
            myList = MyList()
            for j in range(len(self.strong_elist[i])-1,-1,-1):
                if self.strong_elist[i][j]==1:
                    myList.insert(MyListNode(self.strong_nodes[j]))
            self.strong_edges[i][1]= myList

        for i in range(len(self.strong_nodes)):
            self.strong_nodes[i].color="white"
            self.strong_nodes[i].d=None
            self.strong_nodes[i].f=None
            self.strong_nodes[i].parent=None

        self.nodes=self.strong_nodes
        self.edges=self.strong_edges
        self.elist=self.strong_elist

        self.sortlist=[]
        self.search(None)
        self.print()
        
    def getnextedges(self,u):
        for i in range(len(self.edges)):
            if self.edges[i][0].k==u.k:
                return (self.edges[i][1]).getList()
            
    def strong_getnextedges(self,u):
        for i in range(len(self.trans_edges)):
            if self.trans_edges[i][0].k==u.k:
                return (self.trans_edges[i][1]).getList()
            
    def isedges(self,u,v):
        for i in range(len(self.edges)):
            if self.edges[i][0].k==u.k:
                t = (self.edges[i][1]).getList()
                if t!=None:
                    for j in range(len(t)):
                        if (t[j]).key.k==v.k:
                            return True
        return False

    def strong_search(self,u):

        u.color="gray"
        vs=self.strong_getnextedges(u)
        if vs!=None:
            for i in range(len(vs)):
                if vs[i].key.color=="white":
                    vs[i].key.parent=u
                    self.strong_search(vs[i].key)
                    u.child.append(vs[i].key)
                    self.strong_nodes.remove(vs[i].key)
        u.color="black"

    def search(self,u):

        if u==None:
            self.time=0
            for i in range(len(self.nodes)):
                if self.nodes[i].color=="white":
                    self.search(self.nodes[i])
            return

        u.color="gray"
        self.time=self.time+1
        u.d=self.time
        vs=self.getnextedges(u)
        if vs!=None:
            for i in range(len(vs)):
                if vs[i].key.color=="white":
                    vs[i].key.parent=u
                    self.search(vs[i].key)
        u.color="black"
        self.time=self.time+1
        u.f=self.time
        self.sortlist.append(u)

    def strong_getchilds(self,u):
        l=[]
        l.append(u)
        for i in range(len(u.child)):
            l.extend(self.strong_getchilds(u.child[i]))
        
        return l
    
    def strong_isedges(self,u,v):
        ci=self.strong_getchilds(u)
        cj=self.strong_getchilds(v)
        for ii in range(len(ci)):
            for ij in range(len(cj)):
                if self.isedges(ci[ii],cj[ij]):
                    return True
        return False
    
    def print(self):
        for i in range(len(self.nodes)):
            if self.nodes[i].parent!=None:
                print(str(self.nodes[i].k) + " c:" + str(self.nodes[i].color)+ " d:" + str(self.nodes[i].d)+ " f:" + str(self.nodes[i].f)+ " p:" + str(self.nodes[i].parent.k)) 
            else:
                print(str(self.nodes[i].k) + " c:" + str(self.nodes[i].color)+ " d:" + str(self.nodes[i].d)+ " f:" + str(self.nodes[i].f)) 

        for i in range(len(self.sortlist)-1,-1,-1):
            print(self.sortlist[i].k)

        print(self.strong_elist)
            
    @staticmethod                
    def test():
        dfsSearch=DFSSearch()
        dfsSearch.search(None)
        dfsSearch.print()
        dfsSearch.strong_digram()
        
class DFSNode(object):
    def __init__(self,k):
        self.d=None
        self.f=None
        self.k=k
        self.color="white"
        self.parent=None
        self.child=[]             

#DFSSearch.test()

#不相几何森林
class MySetTree(object):
    def makeset(self,x):
        s=MySetTreeNode(x)
        s.parent=s
        s.rank=0
        return s

    def unionset(self,u,v):
        x=self.findset(u)
        y=self.findset(v)
        if x==y:
            return
        
        if x.rank<y.rank:
            x.parent=y
        elif x.rank>y.rank:
            y.parent=x
        else:
            x.parent=y
            y.rank=y.rank+1

    def findset(self,x):
        if x.parent==x:
            return x
        x.parent=self.findset(x.parent)
        return x.parent
        
class MySetTreeNode(object):
    def __init__(self,k):
        self.key=k
        self.parent=None
        self.rank=None

#构建最小生成树
class MSTKruskal(object):
    def __init__(self):
        self.nlist=[]
        self.nlist=['a','b','c','d','e','f','g','h','i']
        self.elist=[]
        self.elist.append([0,4,0,0,0,0,0,8,0])
        self.elist.append([4,0,8,0,0,0,0,11,0])
        self.elist.append([0,8,0,7,0,4,0,0,2])
        self.elist.append([0,0,7,0,9,14,0,0,0])
        self.elist.append([0,0,0,9,0,10,0,0,0])
        self.elist.append([0,0,4,14,10,0,2,0,0])
        self.elist.append([0,0,0,0,0,2,0,1,6])
        self.elist.append([8,11,0,0,0,0,1,0,7])
        self.elist.append([0,0,2,0,0,0,6,7,0])
        
        self.nodes=[]
        self.mySetTree=MySetTree()
        for i in range(len(self.nlist)):
            k=MSTKruskalNode(self.nlist[i])
            self.nodes.append(k)
            k.s=self.mySetTree.makeset(k)
            
        self.a=[]
        self.edges=[]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.elist[i][j]!=0:
                    self.edges.append([self.nodes[i],self.nodes[j],self.elist[i][j]])
                    
    def maketree(self):
        self.a=[]
        for i in range(len(self.nodes)):
            self.nodes[i].s.rank=0
            self.nodes[i].s.parent=self.nodes[i].s

        self.sortqck1(self.edges,0,len(self.edges)-1)
        for i in range(len(self.edges)):
            if self.mySetTree.findset(self.edges[i][0].s)!=self.mySetTree.findset(self.edges[i][1].s):
                self.a.append([self.edges[i][0],self.edges[i][1]])
                self.mySetTree.unionset(self.edges[i][0].s,self.edges[i][1].s)

    def print(self):
        for i in range(len(self.a)):
            print(str(self.a[i][0].k) + "-" + str(self.a[i][1].k))
   
    def sortqck1(self,a,q,r):
        if q<r:
            m = self.sortquick_split(a,q,r)              
            if q<m-1:                               
                self.sortqck1(a,q,m-1)
            if m+1<r:                               
                self.sortqck1(a,m+1,r)
    
    def sortquick_split(self,a,q,r):
        number=a[r]                                 
        tmp=0                                       
        i=q                                         
        j=q-1                                       
        while i<r:
            if a[i][2]<number[2]:                                                                
                j=j+1
                tmp=a[j]
                a[j]=a[i]
                a[i]=tmp
            i=i+1
        a[r]=a[j+1]                                 
        a[j+1]=number
        return j+1
    
    @staticmethod                
    def test():
        mstKruskal=MSTKruskal()
        mstKruskal.maketree()
        mstKruskal.print()
        
class MSTKruskalNode(object):
    def __init__(self,k):
        self.k=k
        self.s=None

#MSTKruskal.test()

#最小生成树，Prime算法,利用到了斐波堆
                
#实现斐波堆
class MyFIBHeap(object):

    def __init__(self):
        self.miniH=None
        self.n=0

    def insert(self,v):

        if self.miniH==None:
            self.miniH=v
            v.left=v
            v.right=v
            v.parent=None
            v.isMark=False
            self.n=1
            return

        v.right=self.miniH
        v.left=self.miniH.left
        
        self.miniH.left.right=v
        self.miniH.left=v
        v.isMark=False
        
        self.n=self.n+1
        
        if v.k.value<self.miniH.k.value:
            self.miniH=v
            
    def popmini(self):
        l=self.miniH
        x=self.miniH.child
        n=self.miniH.degree
        i=0
        while i<n:
            x.parent=None
            x.isMark=False
            tmp=x.right
            self.insert(x)
            x=tmp
            i=i+1

        if self.n==1:
            self.miniH=None
            self.n=0
        else:
            self.miniH.left.right=self.miniH.right
            self.miniH.right.left=self.miniH.left
            self.miniH=self.miniH.right
            self.n=self.n-1
            self.rebuild()
        return l
    
    def rebuild(self):
        d=int(math.log(self.n+1,2))+1                     
        dl=[None]*(d+1)
        x=self.miniH
        n=self.n
        i=0
        while x!=None and i<n:
            de=x.degree
            xr=x.right
            while dl[de]!=None:
                y=dl[de]
                if y.k.value>x.k.value:
                    if y==self.miniH:
                        self.miniH=x
                    m=x
                    x=y
                    y=m

                x.left.right=x.right
                x.right.left=x.left

                if y.child!=None:
                    x.left=y.child.left
                    x.right=y.child
                    y.child.left.right=x
                    y.child.left=x
                else:
                    y.child=x
                    x.left=x
                    x.right=x

                x.parent=y
                x.isMark=False
                y.degree=y.degree+1
                dl[de]=None
                de=de+1
                x=y
            
            dl[de]=x
            x=xr
            i=i+1

        self.miniH=None
        self.n=0
        for i in range(len(dl)):
            if dl[i]!=None:
                self.insert(dl[i])
                
    def searchnode(self,v,k):
        if v!=None and v==k:
            return v

        if v==None:
            x=self.miniH
            n=self.n
        else:
            x=v.child
            n=v.degree

        i=0
        while i<n:
            tmp=x.right
            r=self.searchnode(x,k)
            if r!=None:
                return r
            x=tmp
            i=i+1
            
        return None
        
    def search(self,v,kvalue):

        if v!=None and v.k.value==kvalue:
            return v

        if v==None:
            x=self.miniH
            n=self.n
        else:
            x=v.child
            n=v.degree

        i=0
        while i<n:
            r=self.search(x,kvalue)
            if r!=None:
                return r
            x=x.right
            i=i+1
            
        return None
    
    def pnt(self,v):

        if v==None:
            x=self.miniH
            n=self.n
        else:
            x=v.child
            n=v.degree
            if v.parent!=None:
                print(str(v.parent.k.value)+":"+str(v.k.value))
            else:
                print(v.k.value)

        i=0

        while i<n:
            self.pnt(x)
            x=x.right
            i=i+1
            
    def decrease(self,v,kvalue):

        if kvalue>=v.k.value:
            return False

        v.k.value=kvalue
        if v.parent!=None and v.k.value<v.parent.k.value:
            self.cut(v,v.parent)

        x=self.miniH
        n=self.n
        i=0
        while i<n:
            if x.k.value<self.miniH.k.value:
                self.miniH=x
            x=x.right
            i=i+1
        

    def cut(self,v,p):

        v.left.right=v.right
        v.right.left=v.left
        v.parent=None
        if p.degree>1:
            p.child=v.right
        else:
            p.child=None
            
        self.insert(v)
            
        p.degree=p.degree-1
        if p.parent!=None:
            if p.isMark==False:
                p.isMark=True
            else:
                self.cut(p,p.parent)
                
    def delete(self,v):
        self.decrease(v,-99999)
        self.popmini()
        
    @staticmethod
    def test():
        myFIBHeap1.pnt(None)

    def combine(h1,h2):
        myFIBHeap=MyFIBHeap();

        i=0
        n=h1.n
        x=h1.miniH
        while i<n:
            y=x.right
            myFIBHeap.insert(x)
            x=y
            i=i+1
        
        i=0
        n=h2.n
        x=h2.miniH
        while i<n:
            y=x.right
            myFIBHeap.insert(x)
            x=y
            i=i+1
            
        myFIBHeap.pnt(None)


class MyFIBNode(object):

    def __init__(self,k):
        self.k=k
        self.left=self
        self.right=self
        self.child=None
        self.parent=None
        self.isMark=False
        self.degree=0

#再实现MSTPrime算法       
class MSTPrime(object):
    def __init__(self):
        self.nlist=[]
        self.nlist=['a','b','c','d','e','f','g','h','i']
        self.elist=[]
        self.elist.append([0,4,0,0,0,0,0,8,0])
        self.elist.append([4,0,8,0,0,0,0,11,0])
        self.elist.append([0,8,0,7,0,4,0,0,2])
        self.elist.append([0,0,7,0,9,14,0,0,0])
        self.elist.append([0,0,0,9,0,10,0,0,0])
        self.elist.append([0,0,4,14,10,0,2,0,0])
        self.elist.append([0,0,0,0,0,2,0,1,6])
        self.elist.append([8,11,0,0,0,0,1,0,7])
        self.elist.append([0,0,2,0,0,0,6,7,0])
        
        self.nodes=[]
        for i in range(len(self.nlist)):
            k=MSTPrimeNode(self.nlist[i])
            self.nodes.append(k)
            
        self.edges=[]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.elist[i][j]!=0:
                    self.edges.append([self.nodes[i],self.nodes[j],self.elist[i][j]])

    def maketree(self):

        myFIBHeap = MyFIBHeap()
        
        for i in range(len(self.nodes)):
            if i==0:
                self.nodes[i].value=0
            else:
                self.nodes[i].value=float('inf')
            self.nodes[i].parent=None
            self.nodes[i].f=MyFIBNode(self.nodes[i])
            myFIBHeap.insert(self.nodes[i].f)

        while myFIBHeap.miniH!=None:
            v=myFIBHeap.popmini()
            vs=self.getnextedges(v.k)
            for i in range(len(vs)):
                v=myFIBHeap.searchnode(None,vs[i][1].f)
                if v!=None and vs[i][2]<v.k.value:
                    myFIBHeap.decrease(v,vs[i][2])
                    vs[i][1].parent=vs[i][0]
                    
    def print(self):
        for i in range(len(self.nodes)):
            if self.nodes[i].parent!=None:
                print(str(self.nodes[i].k)+"-"+str(self.nodes[i].parent.k))
            
    def getnextedges(self,u):
        l=[]
        for i in range(len(self.edges)):
            if self.edges[i][0]==u:
                l.append(self.edges[i])
        return l
            
    @staticmethod                
    def test():
        mstPrime=MSTPrime()
        mstPrime.maketree()
        mstPrime.print()
                               
class MSTPrimeNode(object):
    def __init__(self,k):
        self.k=k
        self.value=float('inf')
        self.parent=None
        self.f=None                    

#MSTPrime.test()

#单源最短路径，Bellman-Ford算法
class SSRBellmanFord(object):
    def __init__(self):
        self.nlist=[]
        self.nlist=['s','t','x','y','z']
        self.elist=[]
        self.elist.append([None,6,None,7,None])
        self.elist.append([None,None,5,8,-4])
        self.elist.append([None,-2,None,None,None])
        self.elist.append([None,None,-3,None,9])
        self.elist.append([2,None,7,None,None])
        
        self.nodes=[]   
        self.edges=[]
        
    def makeroute(self):

        self.nodes=[] 
        for i in range(len(self.nlist)):
            k=SSRNode(self.nlist[i])
            self.nodes.append(k)

        self.edges=[[] for i in range(len(self.nodes))]
        for i in range(1,len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.elist[i][j]!=None:
                    self.edges[i].append([self.nodes[i],self.nodes[j],self.elist[i][j]])
        i=0
        for j in range(len(self.nodes)):
            if self.elist[i][j]!=None:
                self.edges[i].append([self.nodes[i],self.nodes[j],self.elist[i][j]])

        self.nodes[0].value=0
        
        for j in range(len(self.nodes)-1):
            for i in range(len(self.edges)):
                vs=self.edges[i]
                for k in range(len(vs)):
                    if vs[k][0].value+vs[k][2]<vs[k][1].value:
                        vs[k][1].value=vs[k][0].value+vs[k][2]
                        vs[k][1].parent=vs[k][0]
                    
        for i in range(len(self.edges)):
            vs=self.edges[i]
            for k in range(len(vs)):
                if vs[k][0].value+vs[k][2]<vs[k][1].value:
                    return False
        return True

    def print(self):
        for i in range(len(self.nodes)):
            print(str(self.nodes[i].k)+"-"+str(self.nodes[i].value))
            
    def getnextedges(self,u):
        i=-1
        i=self.nodes.index(u)
        if i!=-1:
            return self.edges[i]
        else:
            return []

        
    @staticmethod                
    def test():
        ssrBellmanFord=SSRBellmanFord()
        print(ssrBellmanFord.makeroute())
        ssrBellmanFord.print()
                               
class SSRNode(object):
    def __init__(self,k):
        self.k=k
        self.value=float('inf')
        self.parent=None
        self.f=None

#SSRBellmanFord.test()

#单源最短路径，Dijkstra算法
class SSRDijkstra(object):
    def __init__(self):
        self.nlist=[]
        self.nlist=['s','t','x','y','z']
        self.elist=[]
        self.elist.append([None,10,None,5,None])
        self.elist.append([None,None,1,2,None])
        self.elist.append([None,None,None,None,4])
        self.elist.append([None,3,9,None,2])
        self.elist.append([7,None,6,None,None])

        self.nodes=[]
        self.edges=[]
        
    def makeroute(self,start):

        self.nodes=[]
        for i in range(len(self.nlist)):
            k=SSRNode(self.nlist[i])
            self.nodes.append(k)
            
        self.edges=[[] for i in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.elist[i][j]!=None:
                    self.edges[i].append([self.nodes[i],self.nodes[j],self.elist[i][j]])
                    
        myFIBHeap = MyFIBHeap()
        
        for i in range(len(self.nodes)):
            if i==start:
                self.nodes[start].value=0
            else:
                self.nodes[i].value=float('inf')
                
            self.nodes[i].parent=None
            self.nodes[i].f=MyFIBNode(self.nodes[i])
            myFIBHeap.insert(self.nodes[i].f)

        while myFIBHeap.miniH!=None:
            u=myFIBHeap.popmini()
            vs=self.getnextedges(u.k)
            for i in range(len(vs)):
                v=myFIBHeap.searchnode(None,vs[i][1].f)
                if v!=None and u.k.value+vs[i][2]<v.k.value:
                    myFIBHeap.decrease(v,u.k.value+vs[i][2])
                    v.k.parent=u.k
                    
    def print(self):
        for i in range(len(self.nodes)):
            print(str(self.nodes[i].k)+"-"+str(self.nodes[i].value))
            
    def getnextedges(self,u):
        i=-1
        i=self.nodes.index(u)
        if i!=-1:
            return self.edges[i]
        else:
            return []
            
    @staticmethod                
    def test():
        ssrDijkstra=SSRDijkstra()
        ssrDijkstra.makeroute(0)
        ssrDijkstra.print()
                               
#SSRDijkstra.test()

#差分约束,用到关联矩阵    
class DiffConstraints(object):
    def __init__(self):
        self.m=[]
        self.m.append([1,-1,0,0,0])
        self.m.append([1,0,0,0,-1])
        self.m.append([0,1,0,0,-1])
        self.m.append([-1,0,1,0,0])
        self.m.append([-1,0,0,1,0])
        self.m.append([0,0,-1,1,0])
        self.m.append([0,0,-1,0,1])
        self.m.append([0,0,0,-1,1])

        self.b=[]
        self.b=[0,-1,1,5,4,-1,-3,-3]
        self.nlist=[]

        mi=len(self.m)
        mj=len(self.m[0])
        a=[[0 for i in range(mi)] for j in range(mj)]

        self.elist=[[None for i in range(mj)] for j in range(mj)]
        self.edges=[]
        for i in range(mi):
            self.edges.append([None,None,self.b[i]])

        for i in range(mj):
            for j in range(mi):
                a[i][j]=self.m[j][i]

        for i in range(mj):
            for j in range(mi):
                k=-1
                if a[i][j]==1:
                    self.edges[j][1]=i
                    k=i
                    
                if a[i][j]==-1:
                    self.edges[j][0]=i
                    k=i

                if k>-1 and self.edges[j][0]!=None and self.edges[j][1]!=None:
                    self.elist[self.edges[j][0]][self.edges[j][1]]=self.edges[j][2]
        
        for i in range(mj+1):
            self.nlist.append(i)

        self.elist.insert(0,[0]*mj)
        for i in range(len(self.elist)):
            self.elist[i].insert(0,None)
            
    def makeroute(self):
        ssrBellmanFord=SSRBellmanFord()
        ssrBellmanFord.nlist=self.nlist
        ssrBellmanFord.elist=self.elist
        print(ssrBellmanFord.makeroute())
        ssrBellmanFord.print()
        
    @staticmethod                
    def test():
        diffConstraints=DiffConstraints()
        diffConstraints.makeroute()
        
#DiffConstraints.test()

#构建多源最短路径,矩阵乘法
class MSRMatric(object):
    def __init__(self):
        self.elist=[]
        self.elist.append([0,3,8,float('inf'),-4])
        self.elist.append([float('inf'),0,float('inf'),1,7])
        self.elist.append([float('inf'),4,0,float('inf'),float('inf')])
        self.elist.append([2,float('inf'),-5,0,float('inf')])
        self.elist.append([float('inf'),float('inf'),float('inf'),6,0])
        
        self.rlist=[[None for i in range(len(self.elist))] for j in range(len(self.elist))]
        for i in range(len(self.elist)):
            for j in range(len(self.elist)):
                if i==j or self.elist[i][j]==float('inf'):
                    self.rlist[i][j]=None
                else:
                    self.rlist[i][j]=i

    def matric_makeroute_qck(self):      #快速矩阵乘法
        m=1
        h=self.elist
        while m<len(h)-1:
            h=self.matric_cal(h,h,0)
            m=2*m
        return h

    def matric_makeroute(self):          #矩阵乘法
        m=1
        h=self.elist
        while m<len(h)-1:
            h=self.matric_cal(h,self.elist,1)
            m=m+1
        print(self.rlist)
        return h
 
    def matric_cal(self,h,w,f):

        l=[[float('inf') for i in range(len(h))] for j in range(len(h))]
        for i in range(len(l)):
            for j in range(len(l)):
                l[i][j]=h[i][j]
                minik=-1
                for k in range(len(l)):
                    if l[i][j]>h[i][k]+w[k][j]:
                        l[i][j]=h[i][k]+w[k][j]
                        minik=k
                if f==1 and minik!=-1:
                    self.rlist[i][j]=minik

        return l
    
    def floyd_warshall_makeroute(self):     #floyd算法
                    
        l=list(self.elist)
        for k in range(len(l)):            
            for i in range(len(l)):
                for j in range(len(l)):
                    if l[i][j]>l[i][k]+l[k][j]:
                        if i==0 and j==1:
                            print("l[i][j]:"+str(l[i][j]) + " l[i][k]:"+str(l[i][k]) + " l[k][j]:"+str(l[k][j]) + " k:"+str(k)) 
                        l[i][j]=l[i][k]+l[k][j]
                        self.rlist[i][j]=self.rlist[k][j]
        return l
    
    def getroute(self,i,j,f):
        if f==0:
            print("end")
            print(str(j))
            
        if i==j:
            print("start")
        else:
            if self.rlist[i][j]==None:
                print("nopath: i:"+str(i)+" to j:"+str(j))
            else:
                print(self.rlist[i][j])
                self.getroute(i,self.rlist[i][j],1)
        
    @staticmethod                
    def test():
        msrMatric=MSRMatric()
        #print(msrMatric.matric_makeroute_qck())
        print(msrMatric.matric_makeroute())
        #print(msrMatric.floyd_warshall_makeroute())
        msrMatric.getroute(0,1,0)
        
#MSRMatric.test()

#构建多源路径传递闭包
class MSRClose(object):
    def __init__(self):
        self.nlist=[1,2,3,4]
        self.elist=[]
        self.elist.append([0,float('inf'),float('inf'),float('inf')])
        self.elist.append([float('inf'),0,1,1])
        self.elist.append([float('inf'),1,0,float('inf')])
        self.elist.append([1,float('inf'),1,0])
        self.l=[]

    def makeroute(self):
        self.l=[[None for i in range(len(self.nlist))] for j in range(len(self.nlist))]
        for i in range(len(self.nlist)):
            for j in range(len(self.nlist)):
                if self.elist[i][j]<float('inf'):
                    self.l[i][j]=1
                else:
                    self.l[i][j]=0

        for k in range(len(self.nlist)):
            for i in range(len(self.nlist)):
                for j in range(len(self.nlist)):
                    self.l[i][j]=(self.l[i][j] or (self.l[i][k] and self.l[k][j]))

    def isroute(self,i,j):
        return self.l[i][j]

    @staticmethod                
    def test():
        msrClose=MSRClose()
        msrClose.makeroute()
        print(msrClose.isroute(1,3))

#MSRClose.test()

#构建多源路径jason算法，适用于稀疏矩阵（不适合矩阵算法，速度太慢）
class MSRJohnson(object):
    def __init__(self):
        self.nlist=[]
        self.nlist=['1','2','3','4','5']
        self.elist=[]
        self.elist.append([None,3,8,None,-4])
        self.elist.append([None,None,None,1,7])
        self.elist.append([None,4,None,None,None])
        self.elist.append([2,None,-5,None,None])
        self.elist.append([None,None,None,6,None])

        self.nlisttmp=list(self.nlist)
        self.nlisttmp.insert(0,'0')
        self.nlistvalue=[0 for i in range(len(self.nlisttmp))]
        
        self.elisttmp=list(self.elist)
        self.elisttmp.insert(0,[0]*(len(self.nlist)))
        for i in range(len(self.elisttmp)):
            self.elisttmp[i].insert(0,None)

    def makeroute(self):
        
        ssrBellmanFord=SSRBellmanFord()
        ssrBellmanFord.nlist=self.nlisttmp
        ssrBellmanFord.elist=self.elisttmp
        if ssrBellmanFord.makeroute():
            d=[[float('inf') for i in range(len(self.nlist))] for j in range(len(self.nlist))]
            
            for i in range(len(ssrBellmanFord.edges)):
                vs=ssrBellmanFord.edges[i]
                for k in range(len(vs)):
                    if vs[k][0]==ssrBellmanFord.nodes[0]:
                        ei=ssrBellmanFord.nodes.index(vs[k][1])
                        self.nlistvalue[ei]=vs[k][1].value

            for i in range(len(ssrBellmanFord.edges)):
                vs=ssrBellmanFord.edges[i]
                for k in range(len(vs)):
                    ei=ssrBellmanFord.nodes.index(vs[k][0])
                    ej=ssrBellmanFord.nodes.index(vs[k][1])
                    self.elisttmp[ei][ej]=vs[k][2]+(self.nlistvalue[ei]-self.nlistvalue[ej])

            ssrDijkstra=SSRDijkstra()
            ssrDijkstra.nlist=self.nlisttmp
            ssrDijkstra.elist=self.elisttmp

            for i in range(1,len(ssrDijkstra.nlist)):
                ssrDijkstra.makeroute(i)
                for j in range(len(ssrDijkstra.nlist)):
                    d[i-1][j-1]=ssrDijkstra.nodes[j].value-self.nlistvalue[i]+self.nlistvalue[j]
            return d

    @staticmethod                
    def test():
        msrJohnson=MSRJohnson()
        print(msrJohnson.makeroute())

MSRJohnson.test()

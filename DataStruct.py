import random
import math
import ctypes,sys 

#构建栈

class MyStack(object):
    def __init__(self):
        self.tops=-1
        self.a=[]
    def push(self,v):
        self.a.append(v)
        self.tops=self.tops+1
    def pop(self):
        if self.tops>-1:
            self.tops=self.tops-1
            return self.a[self.tops]
        else:
            return "isempty"
    def isempty(self):
        if self.tops==-1:
            return True
        else:
            return False
    @staticmethod
    def test():
        print("begin test stack")
        myStack = MyStack()
        myStack.push(6)
        myStack.push(4)
        print(myStack.pop())
        print(myStack.pop())
        print(myStack.isempty())
        print(myStack.pop()) 

#MyStack.test()

#构建队列

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

        if (self.qhead+1)==len(self.a):
            self.qhead=0
        else:
            self.qhead=self.qhead+1

        self.isfull=False
        
        if self.qhead==self.qtail:
            self.isempty=True
            
    def printQueue(self):
        print(self.a)
        print(self.qhead)
        print(self.qtail)
        
    @staticmethod
    def test():
        print("begin test queue")
        myQueue = MyQueue(3)
        myQueue.enqueue("a")
        myQueue.enqueue("b")
        myQueue.enqueue("c")
        myQueue.enqueue("d")
        myQueue.dequeue()
        myQueue.enqueue("d")
        myQueue.printQueue()  

#MyQueue.test()

#构建双向链表

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
        
#MyList.test()

#构造散列-链接法
class MyHash(object):

    def __init__(self,m):
        self.a=[]
        self.i=0
        self.m=m
        while self.i<self.m:
            self.b=MyList()
            self.a.append(self.b)
            self.i = self.i+1
         
    def put(self,k):
        self.t=self.h(k)
        (self.a[self.t]).insert(MyListNode(k))
        
    def get(self,k):
        self.t=h(k)
        return (a[self.t]).search(k)
    
    def remove(self,k):
        self.t=self.h(k)
        v=(self.a[self.t]).search(k)
        (self.a[self.t]).delete(v)
        
    def h(self,k):
        #return k%self.getprime(self.m)     #除法哈希

        self.s=2654435769                   #乘法哈希
        return (self.s*k%(2**32))>>(32-2)

    def getprime(self,n):
        if n<=1:
            return 2;
        
        while n>1:
            if self.isprime(n):
                return n
            else:
                n=n-1
    def isprime(self,n): 
        if n <= 1: 
            return False
        self.i = 2
        while self.i*self.i <= n: 
            if n % self.i == 0: 
              return False
            self.i=self.i+1
        return True
    def printHash(self):
        self.i=0
        while self.i<self.m:
            print("第:%s"%(self.i))
            (self.a[self.i]).printList()
            self.i = self.i+1
    
    @staticmethod
    def test():
        print("beigin test hash")
        myHash = MyHash(6)
        myHash.put(1)
        myHash.put(2)
        myHash.put(3)
        myHash.put(4)
        myHash.put(5)
        myHash.put(6)
        myHash.put(7)
        myHash.remove(7)
        myHash.put(8)
        myHash.put(9)
        myHash.put(10)
        myHash.put(13)
        myHash.printHash()
        
#MyHash.test()

#构造散列-开放寻址-线性探查-待补充
#构造散列-开放寻址-二次探查-待补充
#构造散列-开放寻址-双重探查-待补充


#构建二叉树
class MyTree(object):

    def __init__(self):
        self.root=None;

    def insert(self,v):
        if self.root==None:
            self.root=v
            return
        self.x=self.root
        while self.x!=None:
            if v.key<self.x.key:
                if self.x.left==None:
                    self.y=self.x
                    break
                else:
                    self.x=self.x.left
            else:
                if self.x.right==None:
                    self.y=self.x
                    break
                else:
                    self.x=self.x.right
        v.parent=self.y
        if v.key<self.y.key:
            self.y.left=v
        else:
            self.y.right=v

            
    def getnext(self,v):
        if v.right!=None:
            return self.getmini(v.right)
        
        self.x=v
        self.y=v.parent
        while self.y!=None:
            if self.x==self.y.left:
                break
            else:
                self.x=self.y
                self.y=self.x.parent
                
        return self.y

    def getmini(self,v):
        self.x=v
        while self.x!=None:
            if self.x.left!=None:
                self.x=self.x.left
            else:
                break
        return self.x
    
    def search(self,k):
        if self.root==None:
            return None

        self.x=self.root
        self.y=None
        while self.x!=None:
            if k<self.x.key:
                self.x=self.x.left
            elif k>self.x.key:
                self.x=self.x.right
            else:
                self.y=self.x
                break

        return self.y
            
    def delete(self,v):

        if v.left==None or v.right==None:
            self.y=v
        else:
            self.y=self.getnext(v)
             
        if self.y.left!=None:
            self.x=self.y.left
        else:
            self.x=self.y.right

        if self.x!=None:
            self.x.parent=self.y.parent

        if self.y.parent!=None:
            if self.y.parent.left==self.y:
                self.y.parent.left=self.x
            else:
                self.y.parent.right=self.x
        else:
            self.root=self.x

        if self.y!=v:
            self.tkey=v.key
            v.key=self.y.key
            self.y.key=self.tkey
       
    def getheight(self,x):

        if x.left!=None:
            hl=self.getheight(x.left)
        else:
            hl=0
            
        if x.right!=None:    
            hr=self.getheight(x.right)
        else:
            hr=0

        x.hl=hl
        x.hr=hr

        if hl<hr:
            return hr+1
        else:
            return hl+1      
              
    def printtree(self):
        if self.root==None:
            return
        
        self.i=0
        self.h=self.getheight(self.root)
        print(self.h)
        
        self.s=[]
        while self.i<=self.h:
            self.s.append([])
            self.i=self.i+1

        self.printtree_do(self.s,self.root,len(self.s),len(self.s)*2)

        self.i=self.h
        while self.i>=0:
            self.j=0
            self.sl=0
            self.pstr=""
            self.k=""
            while self.j<len(self.s[self.i]):
                #print(str(self.i) + ":"+ str(self.s[self.i][self.j].key)+" h:"+str(self.s[self.i][self.j].ph)+" l:"+str(self.s[self.i][self.j].pl))
                #print(str(self.i) + ":"+ str(self.s[self.i][self.j].key)+" l:"+str(self.s[self.i][self.j].hl)+" r:"+str(self.s[self.i][self.j].hr)) 
                if self.s[self.i][self.j].parent!=None:
                    self.k=str(self.s[self.i][self.j].key)+"("+str(self.s[self.i][self.j].parent.key)+")"
                else:
                    self.k=str(self.root.key)+"(0)"

                #self.k = "\033[1;31;40m " + self.k + " \033[0m"
                
                if self.sl==0:
                    self.sl=self.s[self.i][self.j].pl
                else:
                    self.sl =self.s[self.i][self.j].pl-self.s[self.i][self.j-1].pl

                self.pstr=self.pstr+ self.printtree_stradd("    ",self.sl)+ self.k
                self.k=""
                
                self.j=self.j+1
            print(self.pstr)
            self.i=self.i-1
     
    def printtree_do(self,s,x,ph,pl):

        if x.left!=None:
            self.printtree_do(s,x.left,ph-1,pl-2)

        x.ph=ph
        x.pl=pl
        s[ph-1].append(x)

        if x.right!=None:
            self.printtree_do(s,x.right,ph-1,pl+2)
            
    def printtree_stradd(self,sp,l):
        s = ""
        for i in range(l):
            s = s + sp
        return s

    @staticmethod
    def test():
        print("beigin test tree")
        myTree = MyTree()
        s=[6,7,2,5,9,3,1,4,8,0]
        for i in range(len(s)):
            v = MyTreeNode(s[i])
            myTree.insert(v)
        
        myTree.printtree()
        
        #myTree.delete(myTree.search(9))
        #myTree.printtree()
        
class MyTreeNode(object):
    def __init__(self,k):
        self.left=None
        self.right=None
        self.parent=None
        self.key=k
        self.ph=0
        self.pl=0
        self.hl=0
        self.hr=0

#MyTree.test()

#构建二叉树
class MyRBTree(object):

    def __init__(self):
        self.root=None;
        self.noneNode = MyRBTreeNode("","B")
        
    def insert(self,v):
        if self.root==None:
            v.left=self.noneNode
            v.right=self.noneNode
            v.parent=self.noneNode
            v.color="B"
            self.root=v
            return
        
        self.x=self.root
        while self.x!=self.noneNode:
            if v.key<self.x.key:
                if self.x.left==self.noneNode:
                    self.y=self.x
                    break
                else:
                    self.x=self.x.left
            else:
                if self.x.right==self.noneNode:
                    self.y=self.x
                    break
                else:
                    self.x=self.x.right
                    
        v.parent=self.y
        if v.key<self.y.key:
            self.y.left=v
        else:
            self.y.right=v

        v.left=self.noneNode
        v.right=self.noneNode
            
        self.recolorins(v)

    def recolorins(self,v):
        while v.parent.color=="R":
            if v.parent == v.parent.parent.left:
                if v.parent.parent.right.color=="R":
                    v.parent.parent.right.color="B"
                    v.parent.color="B"
                    v.parent.parent.color="R"
                    v=v.parent.parent
                elif  v.parent.parent.right.color=="B":
                    if v==v.parent.right:
                        v=v.parent
                        self.leftrot(v)
                    v.parent.color="B"
                    v.parent.parent.color="R"
                    self.rightrot(v.parent.parent)
            elif v.parent == v.parent.parent.right:
                if v.parent.parent.left.color=="R":
                    v.parent.parent.left.color="B"
                    v.parent.color="B"
                    v.parent.parent.color="R"
                    v=v.parent.parent
                elif  v.parent.parent.left.color=="B":
                    if v==v.parent.left:
                        v=v.parent
                        self.rightrot(v)
                    v.parent.color="B"
                    v.parent.parent.color="R"
                    self.leftrot(v.parent.parent)

        self.root.color="B"
            
    def recolordel(self,v):
        
        while v!=self.root and v.color=="B":
            y=v.parent                              #这里很重要，因为v肯能是nonoNode,所以v.parent可能在旋转过程中发生变化，所以这里要先保存为y
            if v==y.left:
                if y.right.color=="R":
                    y.right.color="B"
                    y.color="R"
                    self.leftrot(y)
                    
                if y.right.color=="B":
                    if y.right.left.color=="B" and y.right.right.color=="B":
                        y.right.color="R"
                        y.color="B"
                        v=y
                    else:
                        if y.right.left.color=="R" and y.right.right.color=="B":
                            y.right.color="R"
                            y.right.left.color="B"
                            self.rightrot(y.right)
                            
                        y.right.right.color="B"
                        y.right.color=y.color
                        y.color="B"
                        self.leftrot(y)

                        v=self.root
            else:
                if y.left.color=="R":
                    y.left.color="B"
                    y.color="R"
                    self.rightrot(y)
                    
                if y.left.color=="B":
                    if y.left.right.color=="B" and y.left.left.color=="B":
                        y.left.color="R"
                        y.color="B"
                        v=y
                    else:
                        if y.left.right.color=="R" and y.left.left.color=="B":
                            y.left.color="R"
                            y.left.right.color="B"
                            self.leftrot(y.left)
                            
                        y.left.left.color="B"
                        y.left.color=y.color
                        y.color="B"
                        self.rightrot(y)   
                        v=self.root
        v.color="B"
        
    def leftrot(self,v):
        y=v.right
        v.right=y.left
        y.left.parent=v
        
        y.left=v
        y.parent=v.parent

        if v.parent==self.noneNode:
            self.root=y
        else:
            if v==v.parent.left:
                v.parent.left=y
            else:
                v.parent.right=y

        v.parent=y
                
    def rightrot(self,v):

        y=v.left
        v.left=y.right
        y.right.parent=v
        
        y.right=v
        y.parent=v.parent
        
        if v.parent==self.noneNode:
            self.root=y
        else:
            if v==v.parent.left:
                v.parent.left=y
            else:
                v.parent.right=y
        v.parent=y

    def getnext(self,v):
        if v.right!=self.noneNode:
            return self.getmini(v.right)
        
        self.x=v
        self.y=v.parent
        while self.y!=self.noneNode:
            if self.x==self.y.left:
                break
            else:
                self.x=self.y
                self.y=self.x.parent
                
        return self.y

    def getmini(self,v):
        self.x=v
        while self.x!=self.noneNode:
            if self.x.left!=self.noneNode:
                self.x=self.x.left
            else:
                break
        return self.x
    
    def search(self,k):
        if self.root==None:
            return None

        self.x=self.root
        self.y=None
        while self.x!=self.noneNode:
            if k<self.x.key:
                self.x=self.x.left
            elif k>self.x.key:
                self.x=self.x.right
            else:
                self.y=self.x
                break

        return self.y
            
    def delete(self,v):

        if v.left==self.noneNode or v.right==self.noneNode:
            self.y=v
        else:
            self.y=self.getnext(v)
             
        if self.y.left!=self.noneNode:
            self.x=self.y.left
        else:
            self.x=self.y.right

        self.x.parent=self.y.parent

        if self.y.parent!=self.noneNode:
            if self.y.parent.left==self.y:
                self.y.parent.left=self.x
            else:
                self.y.parent.right=self.x
        else:
            self.root=self.x

        if self.y!=v:
            self.tkey=v.key
            v.key=self.y.key
            self.y.key=self.tkey

        if self.y.color=="B":
            self.recolordel(self.x)
       
    def getheight(self,x):

        if x.left!=self.noneNode:
            hl=self.getheight(x.left)
        else:
            hl=0
            
        if x.right!=self.noneNode:    
            hr=self.getheight(x.right)
        else:
            hr=0

        x.hl=hl
        x.hr=hr

        if hl<hr:
            return hr+1
        else:
            return hl+1      
              
    def printtree(self):
        #print(self.root.color)
        if self.root==None:
            return
        
        self.i=0
        self.h=self.getheight(self.root)
        #print(self.h)
        
        self.s=[]
        while self.i<=self.h:
            self.s.append([])
            self.i=self.i+1

        self.printtree_do(self.s,self.root,len(self.s),len(self.s)*2)

        self.i=self.h
        while self.i>=0:
            self.j=0
            self.sl=0
            self.pstr=""
            self.k=""
            while self.j<len(self.s[self.i]):
                #print(str(self.i) + ":"+ str(self.s[self.i][self.j].key)+" h:"+str(self.s[self.i][self.j].ph)+" l:"+str(self.s[self.i][self.j].pl)+" c:" + self.s[self.i][self.j].color)
                #print(str(self.i) + ":"+ str(self.s[self.i][self.j].key)+" l:"+str(self.s[self.i][self.j].hl)+" r:"+str(self.s[self.i][self.j].hr)) 
                if self.s[self.i][self.j].parent!=self.noneNode:
                    self.k=str(self.s[self.i][self.j].key)+"("+str(self.s[self.i][self.j].parent.key)+")"
                else:
                    self.k=str(self.root.key)+"(0)"

                #self.k = "\033[1;31;40m " + self.k + " \033[0m"
                self.k = self.k + self.s[self.i][self.j].color
                
                if self.sl==0:
                    self.sl=self.s[self.i][self.j].pl
                else:
                    self.sl =self.s[self.i][self.j].pl-self.s[self.i][self.j-1].pl

                self.pstr=self.pstr+ self.printtree_stradd("    ",self.sl)+ self.k
                self.k=""
                
                self.j=self.j+1
            print(self.pstr)
            self.i=self.i-1
     
    def printtree_do(self,s,x,ph,pl):

        if x.left!=self.noneNode:
            self.printtree_do(s,x.left,ph-1,pl-2)

        x.ph=ph
        x.pl=pl
        s[ph-1].append(x)

        if x.right!=self.noneNode:
            self.printtree_do(s,x.right,ph-1,pl+2)
            
    def printtree_stradd(self,sp,l):
        s = ""
        for i in range(l):
            s = s + sp
        return s

    @staticmethod
    def test():
        print("beigin test tree")
        myRBTree = MyRBTree()
    
        #s=[36,40,38,45,67,12,11,22,34,24,44,29]
        s=[36,40,38,45]
        for i in range(len(s)):
            v = MyRBTreeNode(s[i],"R")
            myRBTree.insert(v)

        myRBTree.printtree()
        myRBTree.delete(myRBTree.search(36))
        print("refresh test tree-------------------------------------------")
        myRBTree.printtree()
        
class MyRBTreeNode(object):
    def __init__(self,k,c):
        self.left=None
        self.right=None
        self.parent=None
        self.key=k
        self.color=c
        self.ph=0
        self.pl=0
        self.hl=0
        self.hr=0

#MyRBTree.test()

#动态规划-最长公共子序列
a=["B","D","B","A","E","F","C","G","H","D","D","K","B","A"]
b=["D","A","E","G","H","P","D","K","B"]
c=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
d=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
e=[]
def lcs_length(a,b,c,d):
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                c[i][j]=c[i-1][j-1]+1
                d[i][j]="LU"
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                d[i][j]=" U"
            else:
                c[i][j]=c[i][j-1]
                d[i][j]=" L"

    s=""
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            s=s+"    "+str(c[i][j])+d[i][j]
        print(s)
        s=""
            
    i=len(a)
    j=len(b)
    while i>0 and j>0:
            if d[i][j]=="LU":
                e.append(a[i-1])
                i=i-1
                j=j-1
            elif d[i][j]==" U":
                i=i-1
            else:
                j=j-1
    for i in range(len(e)-1,-1,-1):
        print(e[i])

#lcs_length(a,b,c,d)

#动态规划-最优二叉查找树
a=[0.15,0.1,0.05,0.1,0.2]
b=["computer","pc","database","network","games"]
c=[0.05,0.1,0.05,0.05,0.05,0.1]
e=[[0.00 for i in range(len(a)+2)] for j in range(len(a)+2)]
w=[[0.00 for i in range(len(a)+2)] for j in range(len(a)+2)]
r=[[0 for i in range(len(a)+2)] for j in range(len(a)+2)]
rt=[]
def bst_optimal(a,b,c,e,w,rt):
    for i in range(1,len(a)+2):
        e[i][i-1]=c[i-1]                
        w[i][i-1]=c[i-1]

    for i in range(len(a)):
        for j in range(1,len(a)-i+1):
            for k in range(j+i,len(a)+1):
                e[j][k]=1000000.00
                w[j][k]=w[j][k-1]+a[k-1]+c[k]               #这里很绕，e[1][1]=e[1][0]+a[0]+c[1]
                for m in range(j,k+1):
                    t=e[j][m-1]+e[m+1][k]+w[j][k]
                    if t<e[j][k]:
                        e[j][k]=t
                        r[j][k]=m

    s=""
    for i in range(1,len(a)+1):
        for j in range(1,len(a)+1):
            s=s+"  "+str(r[i][j])
        print(s)
        s=""
        
    bst_optimal_pnt(r,rt,1,len(a))
    print(rt)
    
def bst_optimal_pnt(r,rt,i,j):

    k=r[i][j]
    
    if i==j:
        rt.append(k)
        return

    rt.append(k)

    if k>=i+1:
        bst_optimal_pnt(r,rt,i,k-1)
    
    if k<=j-1:
        bst_optimal_pnt(r,rt,k+1,j)

#bst_optimal(a,b,c,e,w,rt)

#贪心算法-最活动列表
e=[[0 for i in range(2)] for j in range(11)]
e[0][0]=1
e[0][1]=4
e[1][0]=3
e[1][1]=5
e[2][0]=0
e[2][1]=5
e[3][0]=5
e[3][1]=7
e[4][0]=3
e[4][1]=8
e[5][0]=5
e[5][1]=9
e[6][0]=6
e[6][1]=10
e[7][0]=8
e[7][1]=11
e[8][0]=8
e[8][1]=12
e[9][0]=2
e[9][1]=13
e[10][0]=12
e[10][1]=14
s=[]
def max_act_sel(e):
    s.append(0);
    i=1
    m=0
    while i<len(e):
        if e[i][0]>=e[m][1]:
            m=i
            s.append(m)
        i=i+1
    print(s)
                    
#max_act_sel(e)

#贪心算法-赫夫曼编码树
class Huffman_tree(object):
    
    def __init__(self,l):
        self.root=None
        self.l=l
        
    def pnt(self,n,s):

        if n.k!="":
            print(n.k+":"+s)
            return

        if n.left!=None:
            self.pnt(n.left,s+"0")

        if n.right!=None:
            self.pnt(n.right,s+"1")
        
    def run(self):

        if len(self.l)==1:
            self.pnt(self.root,"")
            return
        
        m1=self.l[0]
        for i in range(1,len(self.l)):
            if self.l[i].v<=m1.v:
                m1=self.l[i]
        self.l.remove(m1)
        m2=self.l[0]
        for i in range(1,len(self.l)):
            if self.l[i].v<=m2.v:
                m2=self.l[i]
        self.l.remove(m2)

        hNode=Huffman_node(m1,m2,m1.v+m2.v,"")
        m1.parent=hNode
        m2.parent=hNode
        self.l.append(hNode)
        self.root=hNode
        
        self.run()
        
    
    @staticmethod
    def test():
        l=[]
        hNode=Huffman_node(None,None,45,"a")
        l.append(hNode)
        hNode=Huffman_node(None,None,13,"b")
        l.append(hNode)
        hNode=Huffman_node(None,None,12,"c")
        l.append(hNode)
        hNode=Huffman_node(None,None,16,"d")
        l.append(hNode)
        hNode=Huffman_node(None,None,9,"e")
        l.append(hNode)
        hNode=Huffman_node(None,None,5,"f")
        l.append(hNode)
        
        hTree = Huffman_tree(l)
        hTree.run()
        
    
class Huffman_node(object):
    def __init__(self,l,r,v,k):
        self.left=l
        self.right=r
        self.parent=None
        self.v=v
        self.k=k

#Huffman_tree.test()

#构建B树( 暂未实现磁盘存取）
class MyBTree(object):
    def __init__(self):
        self.root=None
        self.t=2
    def insert(self,k):
        if self.root==None:
            n=MyBTreeNode()
            n.k.append(k)
            self.root=n
            return

        y=self.root
        if len(y.k)==(2*self.t-1):
            n=MyBTreeNode()
            n.isleaf=False
            n.c.append(y)
            self.root=n
            self.nodesplit(n,y,0)
            if k>n.k[0]:
                self.nodeadd(n.c[1],k)
            else:
                self.nodeadd(n.c[0],k)
        else:
            self.nodeadd(y,k)
        
    def nodesplit(self,x,y,i):

        n=MyBTreeNode()
        n.isleaf=y.isleaf

        while len(y.k)>self.t:
            n.k.append(y.k[self.t])
            y.k.remove(y.k[self.t])

        while len(y.c)>self.t:
            n.c.append(y.c[self.t])
            y.c.remove(y.c[self.t])

        x.k.insert(i,y.k[self.t-1])
        y.k.remove(y.k[self.t-1])
        x.c.insert(i+1,n)        
        
    def nodeadd(self,y,k):

        i=0
        while i<len(y.k):
            if k<y.k[i]:
                break;
            else:
                i=i+1

        if y.isleaf:   
            y.k.insert(i,k)
        else:
            if len(y.c[i].k)==(2*self.t-1):
                self.nodesplit(y,y.c[i],i)
                if k>y.k[i]:
                    i=i+1
            self.nodeadd(y.c[i],k)

    def delete(self,n,i,k):
        if i==-1:
            v=n
        else:
            v=n.c[i]
            if len(v.k)==self.t-1:
                vl=None
                vr=None
                if i-1>=0:
                    vl=n.c[i-1]
                if i+1<len(n.c):
                    vr=n.c[i+1]

                if vl!=None and len(vl.k)>self.t-1:
                    v.k.insert(0,n.k[i-1])
                    n.k[i-1]=vl.k[len(vl.k)-1]
                    vl.k.remove(vl.k[len(vl.k)-1])
                    if not vl.isleaf:
                        v.c.insert(0,vl.c[len(vl.c)-1])
                        vl.c.remove(vr.c[len(vl.c)-1])
                    
                elif vr!=None and len(vr.k)>self.t-1:
                    v.k.append(n.k[i])
                    n.k[i]=vr.k[0]
                    vr.k.remove(vr.k[0])
                    if not vr.isleaf:
                        v.c.append(vr.c[0])
                        vr.c.remove(vr.c[0])
                else:
                    if vl!=None:
                        vl.k.append(n.k[i-1])
                        vl.k.extend(v.k)
                        n.k.remove(n.k[i-1])
                        if not v.isleaf:
                            vl.c.extend(v.c)
                        n.c.remove(n.c[i])
                        v=vl
                    elif vr!=None:
                        v.k.append(n.k[i])
                        v.k.extend(vr.k)
                        n.k.remove(n.k[i])
                        if not vr.isleaf:
                            v.c.extend(vr.c)
                        n.c.remove(n.c[i+1])
                    if len(n.k)==0:
                        self.root=v    

        j=0
        while j<len(v.k):
            if k==v.k[j]:
                if not v.isleaf:
                    self.nodedelete(v,j)
                else:
                    v.k.remove(v.k[j])
                return
            elif k<v.k[j]:
                break
            else:
                j=j+1
  
        self.delete(v,j,k)
        
    def nodedelete(self,n,i):
        vl=n.c[i]
        vr=n.c[i+1]
        if len(vl.k)>self.t-1:
            vp=self.findprev(n,i)
            n.k[i]=vp.k[len(vp.k)-1]
            self.delete(vl,-1,n.k[i])
        elif len(vr.k)>self.t-1:
            vn=self.findnext(n,i)
            n.k[i]=vn.k[0]
            self.delete(vr,-1,n.k[i])
        else:
            k=n.k[i]
            vl.k.append(n.k[i])
            vl.k.extend(vr.k)
            vl.c.extend(vr.c)
            n.k.remove(n.k[i])
            n.c.remove(n.c[i+1])
            if not vl.isleaf:  
                self.nodedelete(vl,self.t-1)
            else:
                self.delete(vl,-1,k)

    def findnext(self,n,i):
        v=n.c[i+1]
        while not v.isleaf:
            v=v.c[0]
        return v
    
    def findprev(self,n,i):
        v=n.c[i]
        while not v.isleaf:
            v=v.c[len(v.c)-1]
        return v
    
    def pnt(self,x):
        print(x.k)
        if not x.isleaf:
            for i in range(len(x.c)):
                print("Node:"+str(x.k))
                self.pnt(x.c[i])
                
    def search(self,v,k):
        
        i=0
        while i<len(v.k):
            if k==v.k[i]:
                return v.k[i]
            elif k<v.k[i]:
                break
            else:
                i=i+1

        if v.isleaf:
            return None
        else:
            return self.search(v.c[i],k)
                
    @staticmethod
    def test():
        myBTree=MyBTree()
        myBTree.insert("I")
        myBTree.insert("H")
        myBTree.insert("G")
        myBTree.insert("F")
        myBTree.insert("E")
        myBTree.insert("D")
        myBTree.insert("C")
        myBTree.insert("B")
        myBTree.insert("A")
        myBTree.delete(myBTree.root,-1,"H")
        myBTree.pnt(myBTree.root)
        print(myBTree.search(myBTree.root,"D"))

class MyBTreeNode(object):
    def __init__(self):
        self.k=[]
        self.c=[]
        self.isleaf=True

#MyBTree.test()

#构建斐波那挈堆

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
        
        if v.k<self.miniH.k:
            self.miniH=v
            
    def popmini(self):
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
                if y.k>x.k:
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

    def search(self,v,k):

        if v!=None and v.k==k:
            return v

        if v==None:
            x=self.miniH
            n=self.n
        else:
            x=v.child
            n=v.degree

        i=0
        while i<n:
            r=self.search(x,k)
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
                print(str(v.parent.k)+":"+str(v.k))
            else:
                print(v.k)

        i=0

        while i<n:
            self.pnt(x)
            x=x.right
            i=i+1
            
    def decrease(self,v,k):

        if k>=v.k:
            return False

        v.k=k
        if v.parent!=None and v.k<v.parent.k:
            self.cut(v,v.parent)

        x=self.miniH
        n=self.n
        i=0
        while i<n:
            if x.k<self.miniH.k:
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
        myFIBHeap1=MyFIBHeap();
        myFIBHeap1.insert(MyFIBNode(28))
        myFIBHeap1.insert(MyFIBNode(27))
        myFIBHeap1.insert(MyFIBNode(29))
        myFIBHeap1.insert(MyFIBNode(20))
        myFIBHeap1.insert(MyFIBNode(16))
        myFIBHeap1.insert(MyFIBNode(12))
        myFIBHeap1.insert(MyFIBNode(17))
        myFIBHeap1.insert(MyFIBNode(36))
        myFIBHeap1.insert(MyFIBNode(46))
        myFIBHeap1.insert(MyFIBNode(19))
        myFIBHeap1.popmini()
        myFIBHeap1.decrease(myFIBHeap1.search(None,36),15)
        myFIBHeap1.decrease(myFIBHeap1.search(None,29),14)
        myFIBHeap1.delete(myFIBHeap1.search(None,20))
        myFIBHeap1.pnt(None)
        print("----------")

        myFIBHeap2=MyFIBHeap();
        myFIBHeap2.insert(MyFIBNode(59))
        myFIBHeap2.insert(MyFIBNode(52))
        myFIBHeap2.insert(MyFIBNode(64))
        myFIBHeap2.insert(MyFIBNode(69))
        myFIBHeap2.insert(MyFIBNode(70))
        myFIBHeap2.popmini()
        myFIBHeap2.pnt(None)
        print("----------")

        MyFIBHeap.combine(myFIBHeap1,myFIBHeap2)

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

MyFIBHeap.test()

#构建vEB树,层层递归把人搞得很晕
class MyvEBTree(object):
    def __init__(self,u):
        self.u=u
        self.a=[0]*self.u
        self.root=None

    def sqrt(self,u):
        return int(math.sqrt(u))
    
    def low(self,u,k):
        return k%int(math.sqrt(u))

    def height(self,u,k):
        return int(k/int(math.sqrt(u)))

    def index(self,u,h,l):
        return (h*int(math.sqrt(u))+l)
        
    def create(self,u):
        myvEBNode=None
        if u>=2:
            myvEBNode=MyvEBNode(u)
            if u>=4:
                myvEBNode.summary=self.create(self.sqrt(u))
                for i in range(self.sqrt(u)):
                    myvEBNode.cluster.append(self.create(self.sqrt(u)))

        if self.u==u:
            self.root=myvEBNode
            
        return myvEBNode
    
    def insert(self,v,k):
        
        if v.min==None:
            v.min=k
            v.max=k
            return
        
        if k<v.min:
            m=k
            k=v.min
            v.min=m
        
        if v.u>2:
            if v.cluster[self.height(v.u,k)].min==None:
                self.insert(v.summary,self.height(v.u,k))
                self.insert(v.cluster[self.height(v.u,k)],self.low(v.u,k))
            else:
                self.insert(v.cluster[self.height(v.u,k)],self.low(v.u,k))

            if k>v.max:
                v.max=k
        
        if k>v.max:
            v.max=k

    def min(self,v):
        return v.min

    def max(self,v):
        return v.max

    def prev(self,v,k):
        if v.u==2:
            if k==1 and v.min==0:
                return 0
            return None
        elif v.max!=None and k>v.max:
            return v.max
        else:
            m=self.min(v.cluster[self.height(v.u,k)])
            if m!=None and self.low(v.u,k)>m:
                l=self.prev(v.cluster[self.height(v.u,k)],self.low(v.u,k))
                return self.index(v.u,self.height(v.u,k),l)
            n=self.prev(v.summary,self.height(v.u,k))
            if n==None:
                if v.min!=None and k>v.min:
                    return v.min
                return None
            else:
                return self.index(v.u,n,self.max(v.cluster[n]))
        
    def next(self,v,k):
        if v.u==2:
            if k==0 and v.max==1:
                return 1
            return None
        elif v.min!=None and k<v.min:
            return v.min
        else:
            m=self.max(v.cluster[self.height(v.u,k)])
            if m!=None and self.low(v.u,k)<m:
                l=self.next(v.cluster[self.height(v.u,k)],self.low(v.u,k))
                return self.index(v.u,self.height(v.u,k),l)
            n=self.next(v.summary,self.height(v.u,k))
            if n==None:
                return None
            else:
                return self.index(v.u,n,self.min(v.cluster[n]))

    #标准删除函数
    def delete(self,v,k):
        if v.min==v.max:
            v.min=None
            v.max=None
        elif v.u==2:
            if k==0:
                v.min=1
                v.max=1
            if k==1:
                v.min=0
                v.max=0
        else:
            if k==v.min:
                m=self.min(v.summary)                       
                k=self.index(v.u,m,self.min(v.cluster[m]))         
                v.min=k
                
            self.delete(v.cluster[self.height(v.u,k)],self.low(v.u,k))
            if v.cluster[self.height(v.u,k)].min==None:
                self.delete(v.summary,self.height(v.u,k))
                if k==v.max:
                    m=self.max(v.summary)
                    if m==None:
                        v.max=v.min
                    else:
                        v.max=self.index(v.u,m,self.max(v.cluster[m]))
                
            if k==v.max:
                v.max=self.index(v.u,self.height(v.u,k),self.max(v.cluster[self.height(v.u,k)]))

    #另一种删除函数写法，更简洁但是效率方面可能会低一点            
    def delete(self,v,k):
        if v.min==v.max:
            v.min=None
            v.max=None
        elif v.u==2:
            if k==0:
                v.min=1
                v.max=1
            if k==1:
                v.min=0
                v.max=0
        else:
            if k==v.min:
                k=self.next(v,v.min)
                v.min=k
            self.delete(v.cluster[self.height(v.u,k)],self.low(v.u,k))
            if v.cluster[self.height(v.u,k)].min==None:
                self.delete(v.summary,self.height(v.u,k))
            if k==v.max:
                k=self.prev(v,v.max)
                v.max=k 
  
    def pnt(self,v):
        if v==None:
            v=self.root

        print("u:"+str(v.u)+" min="+ str(v.min) + " max="+ str(v.max))
        if v.u>2:
            print("--------------")
            print("v.summary")
            self.pnt(v.summary)
            for i in range(len(v.cluster)):
                  print("v.cluster"+str(i))
                  self.pnt(v.cluster[i])
            print("--------------")
            
    @staticmethod
    def test():
        myvEBTree=MyvEBTree(16)
        myvEBTree.create(myvEBTree.u)
        myvEBTree.insert(myvEBTree.root,2)
        myvEBTree.insert(myvEBTree.root,3)
        myvEBTree.insert(myvEBTree.root,4)
        myvEBTree.insert(myvEBTree.root,5)
        myvEBTree.insert(myvEBTree.root,7)
        myvEBTree.insert(myvEBTree.root,14)
        myvEBTree.insert(myvEBTree.root,15)
        print(myvEBTree.next(myvEBTree.root,2))
        print(myvEBTree.prev(myvEBTree.root,6))
        myvEBTree.delete(myvEBTree.root,15)
        myvEBTree.delete(myvEBTree.root,14)
        myvEBTree.delete(myvEBTree.root,7)
        myvEBTree.delete(myvEBTree.root,5)
        myvEBTree.delete(myvEBTree.root,4)
        myvEBTree.insert(myvEBTree.root,4)
        myvEBTree.insert(myvEBTree.root,5)
        myvEBTree.insert(myvEBTree.root,7)
        myvEBTree.insert(myvEBTree.root,14)
        myvEBTree.insert(myvEBTree.root,15)
        print(myvEBTree.next(myvEBTree.root,14))
        myvEBTree.pnt(None)

class MyvEBNode(object):
    def __init__(self,u):
        self.u=u
        self.min=None
        self.max=None
        self.summary=None
        self.cluster=[]

#MyvEBTree.test()
        

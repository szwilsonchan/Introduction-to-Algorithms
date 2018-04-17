import datetime
import random
import sys
sys.setrecursionlimit(5000)
runtimes = 0

#生成逆序数组
def gena1(a):
    i=999
    while i>0:
        a.append(i)
        i=i-1
        
#生成顺序数组
def gena2(a):
    i=1
    while i<999:
        a.append(i)
        i=i+1

#生成随机数组
def gena3(a):
    i=1
    while i<999:
        a.append(random.randint(0,999))
        i=i+1

#生成等长随机数组
def genabase(a):
    i=1
    while i<999:
        a.append(random.randint(100,999))
        i=i+1

#选择排序1，每次比出最小值并更新，时间度N平方
def sortsel1(a):
    begin = datetime.datetime.now()
    number=0
    for i in range(len(a)):                 #第一轮循环
        for j in range(i+1,len(a)):         #第二轮循环，从第一轮循环下一位开始
            if a[i] > a[j]:                 #如果发现有更小的数字，进行交换              
                number = a[i]               
                a[i] = a[j]
                a[j] = number
    end = datetime.datetime.now()
    print("sortsel1:"+str(end-begin))
    return a

#选择排序2，每轮比出最小值再更新，时间度N平方
def sortsel2(a):
    begin = datetime.datetime.now()
    number=0
    starti=0
    indexj=0
    for i in range(len(a)):                 #第一轮循环
        starti=a[i]                         #最小值标志位
        for j in range(i+1,len(a)):         #第二轮循环，从第一轮循环下一位开始
            if starti > a[j]:               #如果发现最小值，更新最小值并记录最小值位置索引
                indexj=j
                starti = a[j]
        if indexj>0:                        #如果有最小值，则交换最小值和第一轮循环开始数的值        
            number = a[i]
            a[i] = a[indexj]
            a[indexj] = number
            indexj=0
    end = datetime.datetime.now()
    print("sortsel2:"+str(end-begin))
    return a

#冒泡排序，每轮排出一个最大值，时间度N平方
def sortpop1(a):
    begin = datetime.datetime.now()
    number=0
    index=0                                             #已排好的最大值位置索引，如： 原始列表：6,5,4,3，2，1，排序过程中：3，2，1，4，5，6，则index=3
    lena = len(a)
    for j in range(lena):                               #第一轮循环
        for i in range(lena-index-1):                   #第二轮循环,从最前面开始，到最大值位置索引前一位，因为最大值位置索引后面的已排好序
            if a[i+1] < a[i]:                           #如果后一位小于当前值的，和当前值交换，循环完则最大数出现在循环末尾
                number = a[i]
                a[i] = a[i+1]
                a[i+1] = number
        index = index + 1                               #更新最大值位置索引                           
        
    end = datetime.datetime.now()
    print("sortpop1:"+str(end-begin))
    return a

#插入排序1
def sortins1(a):
    begin = datetime.datetime.now()
    number=0
    index=0                                             #插入位置索引
    lena = len(a)
    for i in range(lena-1):                             #第一轮循环
        index = i                                       #记录当前值索引
        number = a[i+1]                                 #记录下一位数值
        if a[index]>number:                             #当前值和下一位值比较，如果当前值大于下一位值，则启动比较插入程序
            while index >= 0:                           #下一位值和前面的所有数值逐一比较
                if a[index]>number:                     #此循环中的当前数值大于下一位值
                    a[index+1] = a[index]               #更新此循环中的当前数值至下一位置，相当于把大的数值往右边冒泡
                    index = index - 1
                else:                                   #如果数字小于下一位值，则找到插入值
                    break
            a[index+1] = number
            
    end = datetime.datetime.now()
    print("sortins1:"+str(end-begin))
    #print(a)
    return a

#插入排序2，另一种写法
def sortins2(a):
    begin = datetime.datetime.now()
    lena = len(a)
    for index in range(1,lena):
        value = a[index]
        i = index - 1
        while i >= 0 and (value<a[i]):
                if value<a[i]:
                    a[i+1] = a[i]
                    a[i] = value
                    i = i - 1
                else:
                    break
        
    end = datetime.datetime.now()
    print("sortins2:"+str(end-begin))
    return a

#归并排序，时间度 N*LOG(N)
def sortmer1(a):
    
    if len(a)==1:                               #如果列表长度为1，直接返回
        return a

    
    al = sortmer1(a[0:int(len(a)/2)])           #取整从中间位置拆分
    ar = sortmer1(a[int(len(a)/2):len(a)])      

    b=[]                                        #定义合并列表
    lenal=len(al)                               #左边列表长度
    lenar=len(ar)                               #右边列表长度

    indexl = 0                                  #左边比较索引  
    indexr = 0                                  #右边比较索引

    if 1==2:
        while indexr<lenar and indexl<lenal:    #比较索引未达到左边或右边最大位置
            if al[indexl]<ar[indexr]:           #如果左边列表当前值小于右边列表当前值
                b.append(al[indexl])            #添加左边列表当前值至合并列表B
                indexl = indexl + 1
            else:                               #如果右边列表当前值小于等于左边列表当前值
                b.append(ar[indexr])            #添加右边列表当前值至合并列表B   
                indexr = indexr + 1

        if indexl != lenal:                     #如果左边列表没有比较完
            for i in range(indexl,lenal):       #则把左边列表剩余的值直接加到合并列表B
                b.append(al[i])
            
        if indexr != lenar:                     #如果右边列表没有比较完
            for i in range(indexr,lenar):
                b.append(ar[i])                 #则把右边列表剩余的值直接加到合并列表B

    else:                                       #另外一种实现方式
        al.append(1000000000)
        ar.append(1000000000)
        while indexr<lenar or indexl<lenal:
            if al[indexl]<ar[indexr]:
                b.append(al[indexl])
                indexl = indexl + 1
            else:
                b.append(ar[indexr])
                indexr = indexr + 1
        
    return b


#堆排序主程序，时间度 N*LOG(N)        
def sortsta1(a):
    sortstack_build(a)                          #构建堆结构，堆的顶点是最大值
    i=0
    number=0
    while i<=len(a)-2:                          #循环交换堆顶和堆末元素，交换后最大值在列表末尾，然后重够堆结构
        number=a[0]
        a[0]=a[len(a)-i-1]
        a[len(a)-i-1]=number
        if len(a)-i-1>=2:                       #交换后，重构堆结构，堆大小减1
            sortstack_cal(a,0,len(a)-i-1)
        i = i+1
    return a

#堆排序构建树
def sortstack_build(a):
    i = int((len(a)/2))-1
    while i>=0:                                 #从中间位置循环重构堆结构
        sortstack_cal(a,i,len(a))
        i=i-1

#堆排序调整树结构     
def sortstack_cal(a,i,s):
    l = 2*i+1                                   #取左子节点位置
    r = 2*i+2                                   #取右子节点位置
    m = 0                                       #最大值位置索引
    number = 0
    
    if l < s and a[i]<a[l]:                     #如果左子节点值大于当前节点值
        m = l                                   #更新最大值位置索引为左子节点位置
    else:
        m = i                                   #更新最大值位置索引为当前节点位置    
        
    if r < s and a[m]<a[r]:                     #如果右子节点值大于最大值
        m = r                                   #更新最大值位置索引为右子节点位置

    if m!=i:                                    #如果最大值位置索引为左子节点位置或右子节点位置，则交换最大值和当前值
        number=a[i]
        a[i]=a[m]
        a[m]=number
        sortstack_cal(a,m,s)                    #向下循环重构堆结构

#快速排序1，归并排序，时间度 N*LOG(N)         
def sortqck1(a,q,r):
    global runtimes
    runtimes = runtimes +1
    if q<r:
        m = sortquick_split(a,q,r)              #拆分列表并返回拆分点位置
        if q<m-1:                               #如果拆分点位置不是小于第三位，则继续从左边拆分
            sortqck1(a,q,m-1)
        if m+1<r:                               #如果拆分点位置不是大于倒数第三位，则继续从右边拆分
            sortqck1(a,m+1,r)
    
#快速排序2，随机归并排序，时间度 N*LOG(N)
def sortqck2(a,q,r):
    
    if q<r:
        t = random.randint(q,r)
        tmp=0
        tmp=a[r]
        a[r]=a[t]
        a[t]=tmp
        
        m = sortquick_split(a,q,r)
        sortqck2(a,q,m-1)
        sortqck2(a,m+1,r)


#快速排序拆分列表
def sortquick_split(a,q,r):
    number=a[r]                                 #取最后位置的数值做为比较基准值
    tmp=0                                       
    i=q                                         #记录开始比较位置
    j=q-1                                       #记录最后一个比基准值小的位置
    while i<r:
        if a[i]<number:                         #如果比基准值小，则和最前面大于基准值的数值进行交换                                       
            j=j+1
            tmp=a[j]
            a[j]=a[i]
            a[i]=tmp
        i=i+1
    a[r]=a[j+1]                                 #比较基准值和最前面大于基准值的数值进行交换
    a[j+1]=number
    return j+1

#快速排序拆分列表1,另一种实现方式（优化了顺序列表效率）
def sortquick_split1(a,q,r):
    number=a[r]                                 #取最后位置的数值做为比较基准值
    tmp=0                                       
    i=q                                         #记录开始比较位置
    j=q-1                                       #记录最后一个比基准值小的位置
    while i<r:

        if j==q-1 and a[i]>=number:
            j=i
            
        if a[i]<number and j!=q-1:              #如果比基准值小，则和最前面大于基准值的数值进行交换
            tmp=a[j]
            a[j]=a[i]
            a[i]=tmp
            j=j+1
 
        i=i+1

    if j==q-1:
        j=r

    a[r]=a[j]                                    #比较基准值和最前面大于基准值的数值进行交换
    a[j]=number
        
    return j

#计数排序，时间度N
def sortcnt1(a):
    
    m=0
    for i in range(len(a)):                 #循环比较取出列表中的最大值
        if a[i]>m:
            m=a[i]
            
    c = [0]*(m+1)                           #创建中间列表C，列表最大值m,最小值0，长度m+1
    b = [0]*(len(a))                        #创建排序后列表b
    
    for i in range(len(a)):                 #更新列表C中每个数值的个数，比如c[5]=20，则代表有20个数字是5
        c[a[i]]=c[a[i]]+1
        
    for i in range(len(c)-1):               #更新列表C中小于等于每个数值的个数，比如c[5]=30，则代表有30个数字小于等于5
        c[i+1]=c[i+1]+c[i]
    
    for i in range(len(a)):                 #遍历原始列表，取出每个数字在C列表中的数值，该数值就是该数字在新列表中的排序位置
        index = c[a[i]]-1                   #取出排序位置，等于个数减1，因为索引是从0开始
        b[index]=a[i]                       #更新取出的数字至B列表相应排序位置
        c[a[i]] = index                     #更新C列表里的排序位置，等于原位置减1

    return b

#基数排序，时间度N
def sortbase(s,j):

    a = []                                  
    for i in range(len(s)):                 #先按末位数字排序，比如说：358，则先取出8构造一个新列表排序，列表按末位数字排序后，再递归前一位数字排序    
        a.append(int(str(s[i])[j-1]))

    m=0
    for i in range(len(a)):
        if a[i]>m:
            m=a[i]
            
    c = [0]*(m+1)
    b = [0]*(len(a))
    
    for i in range(len(a)):
        c[a[i]]=c[a[i]]+1
        
    for i in range(len(c)-1):
        c[i+1]=c[i+1]+c[i]

    i=len(a)-1
    while i>=0:                             #这里采用计数排序  
        index = c[a[i]]-1
        b[index]=s[i]                       #从原始列表里取出数字更新至排序列表
        c[a[i]] = index
        i=i-1

    if j-1 <=0:
        return b                            #如果已是首位数字排序，则直接返回排序后的列表B
    else:
        return sortbase(b,j-1)              #如果不是首位数字排序，则进行前一位数字排序

#桶排序，时间度N
def sortpots(s):

    a=[]
    for i in range(10):                     #构造一个10维列表
        d=[]
        a.append(d)
    
    for i in range(len(s)):                 #根据首位数字不同，放置不同的数字到相应的子列表里
        a[int(str(s[i])[0])].append(s[i])

    for i in range(10):                     #逐个排序相应的子列表
        #sortqck1(a[i],0,len(a[i])-1)
        sortsta1(a[i])

    r=[]
    for i in range(10):                     #把各子列表拼接在一起
        r = r + a[i]

#返回第I大的数
def miniqck2(a,q,r,i):

    if q==r:
        return a[q]

    if q<r:
        t = random.randint(q,r)             #构造随机快速排序
        tmp=0
        tmp=a[r]
        a[r]=a[t]
        a[t]=tmp

        m = sortquick_split(a,q,r)          #进行快速排序
        if m==i-1:                          #如果返回的快速排序插入点等于I-1,则正好找到第I大的数
            return a[m]
        
        if i-1<m:                           #如果快速排序插入点大于I, 则从左边至M之间继续找插入点
            return miniqck2(a,q,m-1,i)
        else:                               #如果快速排序插入点小于I, 则从M和结尾之间继续找插入点
            return miniqck2(a,m+1,r,i)


a=[]    
gena3(a)
sortpop1(a)

a=[]         
gena3(a)
begin = datetime.datetime.now()
sortmer1(a)
end = datetime.datetime.now()
print("sortmer1:"+str(end-begin))

a=[]    
gena3(a)
sortsel1(a)

a=[]
gena3(a)
sortsel2(a)

a=[]    
gena3(a)
sortins1(a)

a=[]
gena3(a)
runtimes = 0
begin = datetime.datetime.now()
sortsta1(a)
end = datetime.datetime.now()
print("sortsta1:"+str(end-begin))

a=[]
gena2(a)
runtimes = 0
begin = datetime.datetime.now()
sortqck1(a,0,len(a)-1)
end = datetime.datetime.now()
print("sortqck1:"+str(end-begin))

a=[]
gena3(a)
runtimes = 0
begin = datetime.datetime.now()
sortcnt1(a)
end = datetime.datetime.now()
print("sortcnt1:"+str(end-begin))


a=[]
genabase(a)
begin = datetime.datetime.now()
sortbase(a,len(str(a[0])))
end = datetime.datetime.now()
print("sortbase:"+str(end-begin))

a=[]
genabase(a)
begin = datetime.datetime.now()
sortpots(a)
end = datetime.datetime.now()
print("sortpots:"+str(end-begin))

a=[]
gena3(a)
begin = datetime.datetime.now()
miniqck2(a,0,len(a)-1,1)
end = datetime.datetime.now()
print("miniqck2:"+str(end-begin))



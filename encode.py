import sys


def encode(text,code):
    s=''
    for i in text:
        s=s+code[i]
    return s

class Node :
  def  __init__(self,char,freq):
      self.char=char
      self.freq=freq
      self.left=None
      self.right=None

class priority_queue:
    def __init__(self):
        self.arr=[]
    def size(self):
        return len(self.arr)
    def add_new(self,node):
        self.arr.append(node)
    def remove(self):
        n=len(self.arr)
        min_val=0
        for i in range(n):
            if self.arr[i].freq<self.arr[min_val].freq:
                min_val=i
        t=self.arr[n-1]
        self.arr[n-1]=self.arr[min_val]
        self.arr[min_val]=t
        return self.arr.pop()

def tree_maker(table):
    pq=priority_queue()
    for i,j in table:
        pq.add_new(Node(i,j))
    while pq.size()>1:
        l=pq.remove()
        r=pq.remove()
        node=Node('Intnode',l.freq+r.freq)
        node.left=l
        #pq.add_new(node)
        node.right=r
        pq.add_new(node)

    return pq.remove()
codes={}
def code_maker(root,s):
    
    if root==None:
        return
    if root.left==None and root.right==None:
        codes[root.char]=s
    if root.left!=None:
        s=s+'0'
        code_maker(root.left,s)
        s=s[:len(s)-1]
    
    #print(root.char,root.freq)
    if root.right!=None:
        s=s+'1'
        code_maker(root.right,s)
        s=s[:len(s)-1]

def frecount(text):
    count={}
    for i in text:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    return count


input_file=sys.argv[1]
output_file='output.txt'
if len(sys.argv)>2:
    output_file=sys.argv[2]+'.txt'
text=""
try:
    with open(input_file,'r',encoding='utf-8') as file:
        text=file.read()
        freq_table=frecount(text)
except (IOError):
    print("Error in opening file")

head=tree_maker(freq_table.items())
code_maker(head,'')
try:
    with open(output_file,'w',encoding='utf-8') as file:
        file.write(str(len(freq_table))+' '+str(head.freq)+' ')
        for i,j in codes.items():
            if i==' ':
                file.write('/s'+j+' ')
            elif i=='\n':
                file.write('/n'+j+' ')
            else:
                file.write(i+j+' ')
        file.write('\n')
except (IOError):
    print("Error in opening file")


encoded=encode(text,codes)
l=[]
i=0
while i+8<len(encoded):
    l.append(int(encoded[i:i+8],2))
    i=i+8
if i<len(encoded):
    s=encoded[i:]
    while len(s)<8:
        s=s+'0'
    l.append(int(s,2))

try:
    with open(output_file,'a',encoding='utf-8') as file:
        for i in l:
            file.write(chr(i))
except (IOError):
    print("Error in opening file")

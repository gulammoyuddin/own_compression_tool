import sys
class Node :
  def  __init__(self,char):
      self.char=char
      self.left=None
      self.right=None
head=Node('Internal')
no_chars=0
def change_no_of_chars(i):
    global no_chars
    no_chars=i
def makeTree(s):
    char=''
    code=''
    if s[0]=='/' and (s[1]=='s' or s[1]=='n'):
        char=s[:2]
        code=s[2:]
    else:
        char=s[:1]
        code=s[1:]
    p=head
    for i in code:
        if i=='0':
            if p.left==None:
                p.left=Node('Internal')
            p=p.left
        else:
            if p.right==None:
                p.right=Node('Internal')
            p=p.right
    if char=='/s':
        char=' '
    if char=='/n':
        char='\n'
    p.char=char

def metadata(s):
    l=s.split(' ')
    un=int(l[0])
    change_no_of_chars(int(l[1]))
    i=2
    while i<len(l) and un>0:
        #print(l[i])
        makeTree(l[i])
        un=un-1
        i=i+1

def decode(s):
    ans=''
    binary=''.join(format(ord(i),'08b') for i in s)
    p=head
    for i in binary:
        if i=='0':
            p=p.left
        else:
            p=p.right
        if no_chars>0 and p.left==None:
            ans=ans+p.char
            change_no_of_chars(no_chars-1)
            p=head
    #print(ans)
    return ans

input_file=sys.argv[1]
output_file='output1.txt'
if len(sys.argv)>2:
    output_file=sys.argv[2]+'.txt'
text=""
try:
    with open(input_file,'r',encoding='utf-8') as file:
        text=file.readlines()
except (IOError):
    print("Error in opening file")

metadata(text[0])

"""def ini(root):
    if root==None:
        return 
    print(root.char)
    ini(root.left)
    ini(root.right)
ini(head)"""
ans=''


for i in range(1,len(text)):
    ans=ans+decode(text[i])

try:
    with open(output_file,'w',encoding='utf-8') as file:
        file.write(ans)
except (IOError):
    print("Error in opening file")
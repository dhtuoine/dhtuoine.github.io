class Node:
    def __init__(self, name, par = None ):
        self.name= name
        self.par = par
    def display(self):
        print(self.name)

from collections import defaultdict
data=defaultdict(list)
data['A']=['B','C', 'D']
data['B']=['E', 'F']
data['C']=['G','H']
data['D']=['I','J']
data['F']=['K','L','M']
data['H']=['N','O']

def equal(O,G):
  return O.name == G.name
def checkInArray(tmp,Open):
 for x in Open:
    if equal(x,tmp):
      return True
      return False
    
def path(O):
    print(O.name)
    if O.par!=None:
      path(O.par)
    else:
      return
  
def BFS(S=Node('A'), G=Node('M')):
  Open=[]
  Closed=[]
  Open.append(S)
  while True:
      if len(Open) == 0:
         print('tim kiem that bai')
         return
      O= Open.pop(0)
      Closed.append(O)
      if equal(O,G)==True:
         print('tim kiem thanh cong')
         path(O)
         return
      for x in data[O.name]:
         tmp=Node(x)
         tmp.par=O

      ok1=checkInArray(tmp,Open)
      ok2=checkInArray(tmp,Closed)
# nếu tmp không thuộc O và C thì đưa vào cuối Open
      if not ok1 and not ok2 :
        Open.append(tmp)
BFS(Node('A'), Node('M'))
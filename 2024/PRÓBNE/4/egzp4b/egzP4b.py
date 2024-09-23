from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None

def tree(root):
  T=[]
  def rek(p):
    if p!=None:
      T.append(p.key)
      rek(p.left)
      rek(p.right)
  rek(root)
  T.sort()

def f(T):
  tab=[]
  for v in T:
    tab.append((v.key))

def poprzednik(p):
  val = None
  q=p
  p = p.left
  while p != None:
    val = p.key
    p = p.right
  if val==None:
    while q.parent.key>q.key:
      q=q.parent
    val=q.parent.key

  return val


def nastepnik(p):
  q=p
  val = None
  p = p.right

  while p != None:

    val = p.key
    p = p.left
  if val==None:
    while q.parent.key<q.key:
      q=q.parent
    val=q.parent.key
  return val


def sol(root, T):

  res = 0
  for v in T:
    val1 = poprzednik(v)
    val2 = nastepnik(v)
    if val1 != None and val2 != None and v.key == (val1 + val2) / 2:
      res += v.key
  return res
    
runtests(sol, all_tests = True)
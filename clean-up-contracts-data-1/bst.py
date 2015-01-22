#!/usr/bin/python2


from __future__ import print_function

class TreeNode:
  def __init__(self,key,val,left=None,right=None, parent=None):
    self.key = key
    self.payload = val
    self.leftChild = left
    self.rightChild = right
    self.parent = parent

  def hasLeftChild(self):
    return self.leftChild

  def hasRightChild(self):
    return self.rightChild

  def isLeftChild(self):
    return self.parent and self.parent.leftChild == self

  def isRightChild(self):
    return self.parent and self.parent.rightChild == self

  def isRoot(self):
    return not self.parent

  def isLeaf(self):
    return not (self.rightChild or self.leftChild)

  def hasAnyChildren(self):
    return self.rightChild or self.leftChild

  def hasBothChildren(self):
    return self.rightChild and self.leftChild

  def replaceNodeData(self,key,value,lc,rc):
    self.key = key
    self.payload = value
    self.leftChild = lc
    self.rightChild = rc
    if self.hasLeftChild():
        self.leftChild.parent = self
    if self.hasRightChild():
        self.rightChild.parent = self


class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.size = 0

  def length(self):
    return self.size

  def __len__(self):
    return self.size

  def __iter__(self):
    return self.root.__iter__()

  def put(self,key,val):
    if self.root:
      self._put(key,val,self.root)
    else:
      self.root = TreeNode(key,val)
    self.size = self.size + 1

  def _put(self,key,val,currentNode):
    if key < currentNode.key:
      if currentNode.hasLeftChild():
        self._put(key,val,currentNode.leftChild)
      else:
        currentNode.leftChild = TreeNode(key,val,parent=currentNode)
    else:
      if currentNode.hasRightChild():
        self._put(key,val,currentNode.rightChild)
      else:
        currentNode.rightChild = TreeNode(key,val,parent=currentNode)

  def __setitem__(self,k,v):
    self.put(k,v)

  def get(self,key):
    if self.root:
      res = self._get(key,self.root)
      if res:
        return res.payload
      else:
        return None
    else:
        return None

  def _get(self,key,currentNode):
    if not currentNode:
      return None
    elif currentNode.key == key:
      return currentNode
    elif key < currentNode.key:
      return self._get(key,currentNode.leftChild)
    else:
      return self._get(key,currentNode.rightChild)

  def __getitem__(self,key):
    return self.get(key);

  def __contains__(self,key):
    if self._get(key,self.root):
      return True
    else:
      return False

outCSV = open("final.csv", "w+")
print('contractname,status,bidPurchaseDeadline,bidSubmissionDeadline,'+
 'bidOpeningDate,tenderid,publicationDate,publishedIn,contractDate,'+
 'completionDate,awardee,awardeeLocation,Amount', file=outCSV, end ='');
b = BinarySearchTree()

def toBST():
  with open("awards.csv") as i1:
    next(i1) #First line is title :P
    for line in i1:
      line = line.strip();
      total = line.split(',')
      b[total[0]] = total[1:]
  pass

def main():
  amount = 0;
  toBST();
  #b has the awards bst
  with open("contracts.csv") as i2:
    next(i2) #Creepy First Line
    for line in i2:
      print ('', file=outCSV, end='\n');
      total = line.split(',')
      if total[0] in b:
        #print("a", file=outCSV, end='');
        print(line[:-1] + ',' + ','.join(b[total[0]]), file=outCSV, end='')
        amount = amount + int(b[total[0]][4])
      else:
        print(line[:-1] + ',,,,,', file=outCSV, end='')
  print ("Total Amount of Current Contracts: " + str(amount))

if __name__ == '__main__':
  main()

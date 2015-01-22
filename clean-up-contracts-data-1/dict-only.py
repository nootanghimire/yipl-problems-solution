#!/usr/bin/python2

from __future__ import print_function

outCSV = open("final.csv", "w+")

print('contractname,status,bidPurchaseDeadline,bidSubmissionDeadline,'+
 'bidOpeningDate,tenderid,publicationDate,publishedIn,contractDate,'+
 'completionDate,awardee,awardeeLocation,Amount', file=outCSV, end ='');
b = dict()

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

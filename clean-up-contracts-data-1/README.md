# Solution

The solution would be to compare the contractname of contracts.csv with **each** contractname of awards.csv. Thus, this is all about implementing the Efficient Search algorithm. 

An *easy* way to search would be our old *search-everywhere-for-each* method, which is an O(mxn), or O(n<sup>2</sup>).

But If we, perform binary search then we will be able to decrease the Big-O to O(mxlg(n)). 

Thus, there are two files:
   1. bst.py #which implements binary search tree where searching is O(lg(n))
   2. dict-only #which implements only dict. Note that searching in a dict is O(n)


# Running
1. Make sure you have python2 installed in `/usr/bin/python2`
1.1. Type `$ ls /usr/bin/python2`
1.2. If you `/usr/bin/python2` then go to Step 2, else to Step 3

2. Run the script by `$ ./bst.py` or `$ ./dict-only.py`
2.1. If you run  into problems try `$ chmod +x *.py`

3. Type `$ python2 bst.py` or `$ python2 dict-only.py`

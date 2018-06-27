import datetime as D ;
print(D.date(2018, 4, 7) + D.timedelta(weeks=6))
from functools import reduce
x = reduce(lambda x,y : [y] + x, [0,1,2],[])
print(x)
'''
x = reduce(lambda x,y : x+y, [47,11,42,13])
print(x)
n = "A"
ZERO = 0
print(ord(n))
s = int(ord(n)+"3")
print(s)
lbist = [17,15,13]
alist = list(reversed(lbist))
print(alist)
'''

categories=["mammals","reptiles","insects"]
animals=["cow","dog","viper","python","bee","fly"]
where=[[0,1],[2,3],[3,4]]

print {y[1] : {x[1] for x in enumerate(animals) if x[0] in where [y[0]]} for y in enumerate(categories)}
print {x[1] for x in enumerate(animals) if x[0] in where}
#slist = enumerate(animals)
#print (list(slist))
#print (slist[0])
#{x[1] for x in enumerate(animals) if x[0] in where [y[0]]}
#Test whether the create datastructure for the enumerate is a set or a tuple
# This makes it immutable or   respectively
print("animals")
for x in enumerate(animals):
    print(x)
    #print(x[1])
      
print("categories")
for y in enumerate(categories):
    print (y)
    #print (y[1])]
    

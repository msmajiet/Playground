tree = {
  'abc': {
    'def': 1,
    'ghi': {
      'jkl': 1
      },
    'xyz': 1,
    'qwerty': {
      'test': {
        'fred': 1,
        'bob': 1
        }
      }
    }
  }
  
def traverse_dict(datastr, valuein):
#    found = "False"
#    while (found == 0):
    
    for k in datastr.keys():
        if (valuein == k):
            return "True"
        
    for v in datastr.values():
        #filter(lambda v:isinstance(v,dict),traverse_dict(v,valuein))
        #filter(lambda x:isinstance(x,dict),datastr.values)
        #map(traverse_dict(v,valuein),(filter(lambda x:isinstance(x,dict),v)))
        
        #if type(v) is dict:
       	#if isinstance(v,dict):
            #return traverse_dict(v,valuein)
        #else:
            #return "False"          		   
        
        g = lambda x: isinstance(x,dict)
        if (g(v)):
            return traverse_dict(v,valuein)
        else:
            return "False"     
            
print ("1******************************")
status = traverse_dict(tree,'abc')
print ("Status",status)
print ("1******************************")

print ("2******************************")
status = traverse_dict(tree,'test')
print ("Status",status)
print ("2******************************")

print ("3******************************")
status = traverse_dict(tree,'qwerty')
print ("Status",status)
print ("3******************************")

print ("4******************************")
status = traverse_dict(tree,'asd')
print ("Status",status)
print ("4******************************")

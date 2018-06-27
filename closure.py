def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message)
        
    return inner_func
    

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()


    
print ([n**2 for n in range(10) if n%2])


lst = [-1, 1, -2, 20, -30, 10]
lsta = [x[1] for x in sorted([(abs(x),x) for x in lst])]
print lsta
#print(sort(lst, key=abs))

print "a".endswith("")
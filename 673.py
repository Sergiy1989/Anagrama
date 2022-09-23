def anag():
    a = str(input())
    b = str(input())
    c = []
    d = []
    for i in a:
        c.append(i)
    for j in b:
        d.append(j)
  
    if sorted(c) == sorted(d):
        print(True)
    else:
        print(False)
anag()

    
    

def search(a,b):
    lst=[]
    panjang=len(a)
    set=0
    for i in range(panjang):
        if a[i]==b:
            set=set+1
            lst.append(i)
    if set!=0:
        print "ada"
        print "ada di"
        print lst
    else:
        print "gaada"

n=5 # Wybór wielkości szachownicy, n=5 Szachownica 5x5
def hetmani(n):
    general=""
    kol=""
    wier=""
    przek1=""
    przek2=""
    przek3=""
    przek4=""
    print "Maximize "
    for x in range(1, n + 1): 
        for y in range(1, n + 1):
            print '+ ' + 'x' + str(x) + ',' + str(y),
            general += 'x' + str(x) + ','  + str(y) + '\n'
            
    print '\n \n' + "Subject to "
    for x in range(1, n + 1): # Właściwie, to nie ma sensu upychać tego w pętli powyżej, bo i tak trzeba by potem wypsiać rozwiązanie
        for y in range(1, n + 1):
            kol += ' + ' + 'x' + str(x) + ','  + str(y)
            wier += ' + ' + 'x' + str(y) + ','  + str(x)
        print kol + ' <= 1'
        print wier + ' <= 1'
        kol=""
        wier=""
        j=n
        i=1
        k=x
        while ( k < n + 1 ):
            przek1 += ' + ' + 'x' + str(j) + ','  + str(k)
            przek2 += ' + ' + 'x' + str(i) + ','  + str(k)
            przek3 += ' + ' + 'x' + str(j) + ','  + str(n-k+1)
            przek4 += ' + ' + 'x' + str(i) + ','  + str(n-k+1)
            k += 1
            j -= 1
            i += 1
        
        if (x <> 1 and x <> n): # Jakaś tam ifologia by się nie dublować... 
            print przek1 + ' <= 1'
            print przek3 + ' <= 1'
        if (x <> n):   # I nie wypisywać ograniczeń typu x1,1<=1, które są zbędne bo wynikają z innych
            print przek2 + ' <= 1'
            print przek4 + ' <= 1'
        przek1=""
        przek2=""
        przek3=""
        przek4=""
    print '\n \n' + "Bounds " # Nie potrzeba nam, solver przyjmuje zawsze xij>=0, z innych warunków wynika xij<=1
    print '\n \n' + "General "
    print general
    return;

hetmani(n)

# Szymon Tworek
# Algorytm wykorzystuje zmodyfikowany "insertion sort", zewnętrzna pętla while odpowiada za element który w danej chwili
# jest sprawdzany, natomiast wewnętrzny while sprawdza k kolejnych elementów i wybiera najmniejszy z nich, czyli
# ten który powinien zostać zamieniony. Element, który powinien zostac zamieniony jest przechowywany pod zmienną "mini"
# a następnie przepięty.
# Złożoność czasowa dla  k = Θ(1) to Θ(n), dla k=Θ(log n) to Θ(nlog n), dla k=Θ(n) to k=Θ(n^2)



from zad1testy import Node, runtests


def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    g=Node()
    g.next=p
    p=g
    while p.next!=None and p.next.next!=None:
        licznik=1
        mini=p
        n=p.next

        while licznik<=k and n.next!=None:
            if n.next.val<mini.next.val:
                mini=n
            n=n.next
            licznik+=1

        if mini!=p:

            if mini==p.next:
                pom = p.next
                pom2 = mini.next.next
                p.next = p.next.next
                p.next.next = pom
                pom.next = pom2

            else:
                pom=mini.next.next
                mini.next.next=p.next.next
                p.next.next=pom
                pom2=mini.next
                mini.next=p.next
                p.next=pom2

        p=p.next

    return g.next
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )

import timeit

class Låtar:
    def __init__(self,datarad):
        rensad = datarad.strip()
        uppdelad = rensad.split("<SEP>")
        self.trackid=uppdelad[0]
        self.låtid=uppdelad[1]
        self.Artist=uppdelad[2]
        self.låttitel=uppdelad[3]

    def getartist(self):
        return self.Artist 

    def __lt__(self,other):
        if self.Artist < other.Artist:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.Artist > other.Artist:
            return True
        else:
            return False
    
    def __str__(self):
            return "Artist: " + self.Artist + " , Låt: " + self.låttitel+ " , Trackid: " + self.trackid+ " , Låtid:" + self.låtid

def readfile():
    Låtlista=[]
    with open("/Users/Fabian/Documents/DataOptimering/Labb6/unique_tracks.txt", "r", encoding = "utf-8") as fil:
        for rad in fil:  
            låt=Låtar(rad)
            Låtlista.append(låt)
    return Låtlista
#-------------------------------Sortering-----------------------------------------------------------

#Urvalsortera

def bubbelsortera(data):
    n = len(data)
    bytt = True
    while bytt:
        bytt = False
        for i in range(n-1):
            if data[i].Artist > data[i+1].Artist:
                data[i], data[i+1] = data[i+1], data[i]
                bytt = True

#----------Quicksort----------------------------------------------------------------------------------
def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)


#"Byter" plats på damerna så att det blir i ordning
def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v].Artist < pivot.Artist:
            v = v + 1
        h = h - 1
        while h != 0 and data[h].Artist > pivot.Artist:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v





#--------------------------------------------main-----------------------------------------------
def tid(lista):
    bubbelsort = timeit.timeit(stmt = lambda: bubbelsortera(lista), number = 10000)
    print("Insättningssortera tog", round(bubbelsort, 4) , "sekunder")
    Qsort = timeit.timeit(stmt = lambda: quicksort(lista), number = 10000)
    print("Qsort tog", round(Qsort, 4) , "sekunder")
    

def main():

    listan = readfile()
    lista = listan[0:50]
    n = len(lista)
    #n = 2
    print("Antal element =", n)

    sista = lista[n-1]
    testArtist = sista.Artist
    tid(lista)

main()




# Bubbelsortera = O(n(n-1)/2)
# Quicksort     = O(n log(n))





















"""
Tidtagning:

n=50
Bubbelsortera: 0.1067 sekunder
Qsort:         0.6901 sekunder

n=100
Bubbelsortera: 0.2202 sekunder
Qsort:         2.2202 sekunder

n=200
Bubbelsortera: 0.4082 sekunder
Qsort:         3.3675 sekunder

n=400
Bubbelsortera: 0.9532 sekunder
Qsort:         9.718  sekunder

"""
"""
Tidskomplexitet:

Bubbelsortera = O(n(n-1)/2)
Quicksort     = O(n log(n))

Enligt teorin så borde QS vara snabbare men under våra tester nu har BS varit solklart snabbast.
Vi tror att det har att göra med att någonstans i QS har det blivit något fel, som vi tyvär inte kan hitta,
som gör så att den itererar mer gånger än vad den ska.
"""
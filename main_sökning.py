
import timeit

class Låtar:
    def __init__(self,datarad):
        rensad = datarad.strip()
        uppdelad = rensad.split("<SEP>")
        self.trackid=uppdelad[0]
        self.låtid=uppdelad[1]
        self.artistnamn=uppdelad[2]
        self.låttitel=uppdelad[3]

    def __lt__(self,other):
        if self.artistnamn < other.artistnamn:
            return True
        else:
            return False
    
    def __str__(self):
            return "Artistnamn: " + self.artistnamn + " , Låt: " + self.låttitel+ " , Trackid: " + self.trackid+ " , Låtid:" + self.låtid
    def getartistnamn(self):
        return self.artistnamn

def readfilelista():
    
    Låtlista=[]
    with open("/Users/Fabian/Documents/DataOptimering/Labb6/unique_tracks.txt", "r", encoding = "utf-8") as fil:
        for rad in fil:  
            låt=Låtar(rad)
            Låtlista.append(låt)
            Tlåt=Låtar.getartistnamn
        return Låtlista

def readfiledict(Låtlista):
    Låtdict= {}
    Tlåt=Låtar.getartistnamn
    for rad in Låtlista:
        Låtdict[Tlåt]=Låtlista[len(Låtlista)-1]
    return Låtdict
    



#-------------------------------Sökning-----------------------------------------------------------
#tidtagningen
def linsok(data, key):
    for x in data:
        if x == key:
            return True
    return False

def sortera(lista):
    lista.sort()
    return lista


def binary_search(sortedList, key):
    
    left = 0
    right = len(sortedList) - 1
    found = False

    while left <= right and not found:
        midIndex = (left + right)//2
        if sortedList[midIndex].artistnamn == key:
            found = True
        else:
            if key < sortedList[midIndex].artistnamn:
                right = midIndex - 1
            else:
                left = midIndex + 1

def htabell(data, key):
    if key in data:
        return True
    else:
        return False



#--------------------------------------------main-----------------------------------------------
#Lägger in artisnman i dict och sen kopplar ihop det med sjävlva objektet
def main():
    listan = readfilelista()
    Dicton = readfiledict (listan)
    lista = listan[0:800]
    binlista=sortera(lista)
    n = len(lista)
    #n = 2
    print("Antal element =", n)

    sista = lista[n-1]
    testartist = sista.artistnamn

    bintid = timeit.timeit(stmt = lambda: binary_search(binlista, testartist), number = 10000)
    print("Binärsökningen tog", round(bintid, 4) , "sekunder")
    linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
    print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
    htbtid = timeit.timeit(stmt = lambda: htabell(Dicton, testartist), number = 10000)
    print("Sökning i Hashtabell tog", round(htbtid, 4) , "sekunder")


main()
"""
Tidtagning

200 element:
binär              0.0302 sekunder
linjär             0.2378 sekunder
Hashtabell (dict)  0.0022 sekunder

400 element
binär              0.0373 sekunder
linjär             0.466 sekunder
Hashtabell (dict)  0.0025  sekunder

800 element
binär-              0.0398 sekunder
linjär-             0.9229  sekunder
Hashtabell (dict)   0.0032 sekunder
"""
"""
Tidskomplexitet:
Binärsökning           = O(Log 2 n) i värsta fall
Linjär                 = O (n)      i värsta fall
Hashtabell genom dict  = O (1)

HT var soklart snabbast bland dessa 3 aglogritmer, bode när vi körde de lägre antal elementen och de större. 
Skillnaden mellan 200 element och 800 så ökade:
-binärsökning 31%
-linjär        280%
-HT            28%
"""
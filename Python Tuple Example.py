
def islemler(tuple1):
     
    print(len(tuple1[2:])) # tuple1 değişkeninin 2. indeksinden sonuna kadar olan elemanların sayısı yazdırılır
    print(tuple1[:3]) #tuple1 değişkeninin ilk üç elemanı yazdırılır
    tuple2 = tuple1[2:-2] #tuple1 değişkeninin baştan ikinci elemanından sondan ikinci elemanına kadar olan kısmı başka bir değişkene (mesela tuple2) atanıyor 
    print(max(tuple2)) # tuple2 değişkeninin maksimum elemanı    
    print(min(tuple2)) # tuple2 değişkeninin minimum elemanı
    
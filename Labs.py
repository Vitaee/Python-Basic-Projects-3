#Lab 02 Q1)

def right_justify( in_str): # Fonskiyonumuzu oluşturduk
    
    print(in_str.rjust(70)) # Girilen kelimenin önüne 70 boşluk ekledik(rjust methodu ile)
                            #fonksiyon parametresi.rjust("kaç tane boşluk istiyorsak yazalım")

right_justify("Hello") #Fonksiyona değer yani string atıyarak ekranımıza print olmasını sağladık.(70 boşluk bırakarak)
                       #in_str parametremize string yazdık print edilirken 70 boşluk bırakılacak sonra kelimemiz ekrana basılacak.


#Lab02 Q2)

def first(sutun):
    
    print("+", end=" ") # + işaretini print ediyoruz , end tanımlıyoruz
    for i in range(sutun-1):# for döngüsüne alıp bir alt satırdaki olayın tekrarlanmasını söylüyoruz
        print("- - - - +", end=" ")  # ilk kısmı yani + - - - - + kısmını yazdık    
    print("- - - - +" ) # Sonra - - - - + kısmını printledik yanına 
    
 #Özetle üst kısımda  + - - - - + - - - - + kısmını ayarladık 

def second(sutun):
    print("|", end=" ") # | işaretini print ediyoruz , end yani duracağı yeri söylemek için böyle bir tanım yapıyoruz
    for i in range(sutun-1): # for döngüsününe alıp alttaki olayı yazdırıyoruz 
        print("        |", end=" ") # ilk | işaretten ne kadar boşluk bırakmak istiyorsak o kadar boşluk bırakıp print ediyoruz.
    print("        |" ) # ve en son ki | işareti unutmayalım.
    
    
def grid(sutun,satır ):
    #şimdi ise kaç adet | , + veya - olacak ve kaça kaç(Örn;3x3) print edilecek onu yazıyoruz
    first(sutun) # ilk satır + - - - - + - - - - + kısmını yazdırkık first(sutun) kodunun başına # koyup test edebilirsin neler olacağını. 
    for i in range(satır): # yine for döngüsüne alarak kaç defa döngüye gireceğini belirleyeceğiz.
        for i in range(4): # 4 yazmamızın sebebi 4 tane | , 4 tane - , 4 tane + 2x2 matrix'inde 3 tane + oluyor.
            second(sutun) # | sütünları for döngüsünün içine aldık ki ekrana alt alta çıkabilsin.
        first(sutun) # son satır olan  + - - - - + - - - - + kısmını yazdırdık
            

grid(2,2) # 2 ye 2 bir matrix oluşturduk
grid(3,3) # 3 e 3 matrix


#Lab 03 Q1)
fmt = "{} is a {} - year course" # string'imizi tanımladım {} koyduğum yerlere gelmesi gerekenleri bir alt satırda yazdım.
print( fmt.format("ECC102", "first" ) ) #ekrana bu şekilde print edecek = 'ECC102 is a first-year course.'
#kelimeleri veya ''{}'' sayısını değiştirip olayı daha da iyi anlayabilirsin





#Q2)
fmt = "{} {} {} = {} " # string'imizi yazdık 
print( fmt.format( "30", "/", "5", 30 / 5 ) ) #Ekrana bu şekilde print edecek '30 / 5 = 6.0'.
#30 /  5 i belirtmemiz lazım yoksa hata alırız program çalışmaz. sadece 6 çıkmasını istersen 30 // 5 yazabilirsin.

#Q3)
print("  {}   | {}| {} ".format( "Class","Exam Type", "Grade" ) ) #Class, Exam Type, Grade'i ekrana yazdırdık
print("{}|{}|{} ".format( "-" * 10, "-" * 10, "-" * 13 ) ) # | işaretlerin arasında kaç tane "-" olacağını ekrana yazdırdık.
print("  {}  | {}  | {:.3f} ".format( "ECC102", "Midterm", 78.123 ) )#Uygun boşluklar bırakarak ekrana yazdırdık 
# .3f yazmamızın sebebi 78.123'den sonra diğer sayıları ekrana yansıtmak istemediğimiz için.
print("  {}  | {}    | {:.2f} ".format( "ECC104", "Final", 82.45 ) )# uygun boşluklar bırakıp {} içini doldurarak ekrana yazdırdık.
print("  {}  | {}   | {:.2f} ".format( "ECC108", "Makeup", 98.0 ) )
print("  {}  | {}    | {:.2f} ".format( "ECC200", "Resit", 100 ) )



#Lab 04 #Q1)
def divisible_by( a, n ): # iki parametre atadık(a,n)
    return True if a % n == 0 else False # eğer a sayısının n sayısına bölümünden kalanı 0 ise True yazdır değil ilse False.
    #return ederek,  a ve n parametrelerine sayı atadığımızda bize işlemi yapıp true veya false yazdırsın 

print( divisible_by( 10, 2 ) )   # Should print out: True
print( divisible_by( 10, 3 ) )   # Should print out: False
print( divisible_by( 22, 4 ) )   # Should print out: False
print( divisible_by( 250, 50 )) # Should print out: True
print( divisible_by( 101, 37 )) # Should print out: False


#Q2
def is_even( int_value ): #int_value yerine a veya b veya n yazabiliriz sorun yok.
    return int_value % 2 == 0 #eğer int_value çift sayı ise True değil ise False yazdırmasını sağladık

print( is_even( 4 ) )  # should return True
print( is_even( 28 ) ) # should return True
print( is_even( 39 ) ) # should return False
print( is_even( 1 ) )  # should return False




#Q3)
def is_odd( int_value ):
    return int_value % 2 == 1 #eğer int_value tek sayı ise True değil ise False yazdırmasını sağladık

print( is_odd( 4 ) )  # should return False
print( is_odd( 28 ) ) # should return False
print( is_odd( 39 ) ) # should return True
print( is_odd( 1 ) )  # should return True



#Lab 05 Q1)
def power(x,y): #Fonksiyon verilen 2 değerin 1.si tabanı 2.sini ise üssü alarak işlem yapıyor 
    if y == 0:  #Eğer y 0 olursa cevabı 1 olarak ekrana yazdırmasını söyledik 
        return 1
    if y >= 1: #Eğer y >= 1 ise işlemin yapılıp ekrana cevabı yazdırdık 
        return x * power(x, y - 1) # power rule; a x a'üssü (y-1)
    
power(4,2)    


#Lab 05 Q2)
def is_power(a,b): #Fonksiyon verilen iki sayının bölümünden kalan 0 veya 1 ise True, dğil ise ekrana False yazdıracak
    if(a % b == 0): # örn.(eğer 64 % 2 == 0 ise return True )
        return True
        if(a//b == 1): # örn.(eğer 2 / 2 == 1 ise  return True) değil ise False yazdır.
            return True
    else:
        return False
    
print(is_power(64,2))  # 62 // 2 = 32 ama 64 % 2 = 0 olduğu için true çıktı
print(is_power(9,2))  # 9 // 2 = 4 olduğu için false çıktı 
    




#Lab 06 Q1)
def middle( lst ): #fonksiyonu oluşturduk
    x = [] # boş liste, [2:3] atadık bize return olarak verilen listenin [2]. elemanı hariç diğer elemanları silecek.
    for a in lst:
        if a not in x:
            x.append(a)
    return x[2:3] # verilen listeye göre listenin örn.[1,2,3,4,5] , [2] = [3] elemanını haricinde diğerlerini sildirdik.
                  #ve kalan elemanlar ile yeni bir list oluşturup ekrana yazdırdık

def center(lst1): 
    z = []
    for b in lst1:
        if b not in z:
            z.append(b)
    return z[1:3]  # [1,2,3,4] listesindeki [1:3] yani 2,3 kısmı hariç geri kalanları silip 2,3 elemanları ile ekrana
                   #[2,3] yeni listemizi yazdık.
    
print(middle([1,2,3,4,5])) # lst ve lst1 listelerini oluşturduk ve bu iki listedeki bazı yerler hariç geri kalanının..
                           #silinip kalan elemanlarla yeni bir listeyi ekrana print ettirdik.
print(center([1,2,3,4]))
    

#Q2)
def chop(lst): #Yeni bir fonksiyon ve parametresini yazdık
    del lst[0] #listenin 1. elemanı 
    del lst[-1] # ve son elemanını sildik 
    
def middle(lst):  # ekrana yazdırma 
    new = lst[1:] #bu komutla geriye kalan elemanları return ediyoruz
    return new


my_list = [1, 2, 3, 4, 5] #işlemlerin yapılacağı listemizi oluşturduk.
chop_list = chop(my_list) #None yazdırmak için 

print(chop_list)  # Should be None çünkü (anladığım kadarıyla) chop_list'i [1,2,3,4,5] li olan listeye eşitliyoruz ama 
                  #ortada öyle bir liste yok çünkü elimizde [2,3,4] listesi kaldı bu yüzden ekrana None çıkıyor.
print(my_list)    # Should be [2,3,4]





#Q3)  #Verilen sayıları verilen işlemleri yapıp liste içerisinde print ettik
def addition(n): 
    return n + 3 # toplama fonksiyonunu oluşturduk.
def multiply(a):
    return a * 3 # çarpma
def division(b):
    return b // 3 # bölme
def exponential(c):
    return c ** 3 # üssü 

    
#Map methodu kullanarak her bir sayı belirlediğimiz sayı ile işlem yapıyor(return n + 3) mesela 1 + 3 = 4 
# ve listenin ilk elemanı 4 oluyor..

#We double all numbers using map() 

numbers =  (1, 2, 3, 4, 5) 
numbers1 = (1, 2, 3, 4, 5) 
numbers2 = (1, 2, 3, 4, 5) 
numbers3 = (1, 2, 3, 4, 5) 

result = map(addition, numbers) 
result1 = map(multiply, numbers1)
result2 = map(division, numbers2)
result3 = map(exponential, numbers3)

print(list(result)) 
print(list(result1)) 
print(list(result2)) 
print(list(result3)) 



#Lab 09
#Q1)
def total_purchase_price(stocks): #Fonksiyonumuzu tanımladık
    res = [] #Boş listemizi oluşturduk
    for block in stocks: 
        shares = block[2] #Verilen listede shares = 2 yaptık yani her listenin 2. elemanı 25, 50, 75 ve 100
        purchase_price = block[1] #Verilen listede price = 1 yaptık yani 43.50, 42.80, 42.10 ve 37.58
        res += [shares * purchase_price] #Bu sayılara işlem yaptırdık 25 * 43.50 , 50 * 42.80...
    return res #return diyerek işlem sonucunda oluşan elemanları listeye ekledik

portfolio= [ ( "25-Jan-2001", 43.50, 25, 'CAT', 92.45 ),  
( "25-Jan-2001", 42.80, 50, 'DD', 51.19 ),
( "25-Jan-2001", 42.10, 75, 'EK', 34.87 ),
( "25-Jan-2001", 37.58, 100, 'GM', 37.58 )
]

print(total_purchase_price(portfolio)) #ve ekrana yansıttık.









#Q2)#Bu program verilen listedki elemanların toplamını listedeki eleman saysına bölü sonucu ekrana yazdırıyor.
def getPairsCount(arr, n, sum): 
      
    count = 0 # Initialize result 
  
    # Consider all possible pairs 
    # and check their sums 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
      
    return count 

arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
print("Count of pairs is", 
      getPairsCount(arr, n, sum)) 






#Q3)
import math 
  
# Function for calculating variance 
def variance(s, n): 
  
    # Compute mean (average of 
    # elements) 
    sum = 0
    for i in range(0 ,n): 
        sum += s[i] 
    mean = sum /n 
  
    # Compute sum squared  
    # differences with mean. 
    sqDiff = 0
    for i in range(0 ,n): 
        sqDiff += ((s[i] - mean)  
                * (s[i] - mean)) 
    return sqDiff / n 
  
  

def standardDeviation(arr, n): 
  
    return math.sqrt(variance(arr, n)) 
  
# Driver Code 
x = [600, 470, 170, 430, 300] 
n = len(x) 
print("Variance: ", int(variance(x, n))) 
print("Standard Deviation: ", 
      round(standardDeviation(x, n), 3)) 





















































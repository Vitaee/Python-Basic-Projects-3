#HW 01 Q3) #Binary to Decimal (İkili sayı sisteminden Ondalıklı Sayıya çevirme)

a = input("Input a number in binary: ") # Kullanıcıdan 01'li sayı istiyoruz
decimal = 0 #ondalık değişkenini tanımladık
for digit in a: #a daki sayıyı
    decimal = decimal*2 + int(digit)#Alınan 01'li sayıyı ikili sayıya çevirmemize yarayan formül.
    #a = 1001 ise 1*2**0 + 0*2**1 + 0*2**2 + 1*2**3
    
print("Your decimal number is: " + str(decimal)) # sayımızı str formatına çevirdikki herhangi bir hata almayalım eğer,
#str(decimal), yazmaksak str + int toplaması yapmış oluruz ki pythonda böyle birşey yapılamaz.


#Q4) #Decimal to Binary
decimal = int(input("İnput a decimal number: ")) #kullanıcıdan bir sayı aldık 
binary="" #binary'i tanımladık
while decimal>0: # 9 > 0 
    #giriilen sayı 9 ve burdaki işlem sayı 9'a eşit olana kadar devam edecek
  binary = str(decimal%2) + binary 
  decimal = decimal//2
  #12//2 = 6   12 % 2 = 0
  #6//2 = 3    6 % 2 = 0
  #3//2 = 1    3 % 2 = 1
  #1 // 2 = 1  1 % 2 = 1

print("Your binary number is: " + binary)



#HW 02 Q2) #hazırda olan sayının, kullanıcıdan sayı isteyip hazırda olan sayının üssünü alıyoruz 
b = 2 #sayımızı belirledik
a = int(input("Enter the power of two")) # kullanıcıdan bir sayı istedik
print("Two to the power of ",a, "is", b**a) # kullanıcı 10 sayısını girdiğinde 2 üssü 10 = 1024



#Q3) #Bu sefer hazır bir sayı belirlemeyip her iki sayıyıda kullanıcıdan aldık.
a = int(input("Enter the base? "))
b = int(input("Enter the power of? "))
print("Two to the power of ",b, "is", a**b)




#Q4  #Kullanıcıdan alınan ondalık(01) sayıyı ikili sayı sistemine çevirdik.
a = int(input("Enter the left most digit: "))
b = int(input("Enter the next digit: " ))
c = int(input("Enter the next digit: "))
d = int(input("Enter the next digit: "))
#Kullanıcıdan alınan 4 tane veriyi formüle uygulayıp ekrana yazdırıyoruz.
print("The value is: " , (a*2**0 + b*2**1 + c*2**2 + d*2**3))




#Q5) #Hocamızın anlattığı bir algoritma vardı kaçtane şehir olursa şehirler arası kaçtane rota oluşturabiliriz
#Kullanıcıdan şehir sayısını alıp o sayının faktöriyelini alıyoruz ve ekrana yazdırıyoruz.
import math 
a = int(input("How many cities? "))
b = math.factorial(a)
print("For" , a , "cities, there are" , b , "possible routes")






#Q6)#Burda bölünen 2 sayının (13 / 3 = 4.33) "." sından sonra kaç adet rakam olacağını belirliyoruz.
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
# kullanıcıdan sayıları aldık
c = ("{:.2f}".format( a / b))
# çıkan sonucun sonunda "." tan sonra 2 sayı gelmesini sağladık ("{:.2f}") burdaki 2 "."dan sonra 2 adet sayı geleceğini belirttik.
print(a, "divided by" ,b, "is", c,) #sonucu print ettik.




#Q7) Burda ise bölünen 2 sayının . sından sonra 6 adet sayı gelmesini sağlıyoruz. "{:.6f}"
a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
c = ("{:.6f}".format( a / b))
print(a, "divided by" ,b, "is", c,)



#Q8) #Ondalık sayının  scientific notation (bilimsel gösterimi)
a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
c = ("{:.6e}".format( a / b)) #"." sonra kaçtane geleceğini belirledik e koyarak  scientific notation tanımını yaptık.
print(a, "divided by" ,b, "is", c,)



#Q9)Kullanıcıdan 4 tane herhangi bir karakter alıp o karakterin karşılık geldiği ondalık sayıyı ekrana veriyoruz.
    #ord() fonksiyonu ile

i = 0
while i < 4: #Programı 4 kez soru soracak şekilde ayarladık
    i += 1 #1.soru i = 1, 2.soru i = 2, 3.soru i= 3, 4.soru i = 4 ve program durur. 
    c = input("Enter a character: ")
    print("The Unicode encoding for character '" + c + "' is",ord(c)) #ord(c) yazıyoruz ki ord methodunu kullanabilelim.





#Q10) #Kullanıcıdan 2 sayı isteyip aşağıdaki işlemlerin sonucunu print ettiriyoruz.
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print(a + b) 
print(a - b)
print(a * b)
print("{:.2f}".format(a / b)) # "." dan sonra sadece 2 sayı gelmesini sağlıyoruz
print(a // b)
print(a % b)
print("{:,}".format(a**b)) #normalde 7**5 = 16807 fakat burda araya bir virgül koymak istiyoruz onuda "{:,}"
                           #bu işlemle sağlıyoruz.





#HW 03 Q6) #Verilen listede bulunan sayıların 3'e tam bölünebilenlerin toplamını veren program
num_list = [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 17, 18]
i = 0
sum = 0

while i < len(num_list): #i sayısı = 0 listenin içindeki elemanların sayısı 12, 0 > 12
    
    if(num_list[i] % 3 == 0): #listenin içindeki sayıların 3'e tam bölünenleri 
        
        sum = num_list[i] + sum # o sayıların toplamını 
        
    i = i + 1  #döngü sonsuza girmemesi için veya i += 1 de yazılabilir ve bunu yazmadığımız zaman,
               #ekrana herhangi bir sayı çıktısı alamayız.
        
print("The sum of all values divisible by 3 is",sum) #sonucu print ettik.

# Q7) #Programı bu sefer for loop ile yazdık.
num_list = [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 17, 18]
i = 0
sum = 0
for i in (num_list):  
    if(i % 3 == 0): # 3,6,9,15,18
        sum = sum + i # 3+6+9+15+18 = 51
        
print("The sum of all values divisible by 3 is" ,sum)






#Q9) Verilem listedeki string sayısını while döngüsü ile göstermek

items = ['apple', 55, 1.2, 'banana', lambda a: a, 'pear', None, 'cherry',  """Hello world!""", '''The Who''', ("a", 5), [("a", "5"), ("b", 3)]]

i = 0


while i < len(items): # i < 12:
    if(type(items) == str): #Listelerdeki elemanların string olanlarını al
        i += 1  # bu kod satırını yazmadığımız zaman aşağıdaki i += 1'i buraya almak zorundayız yoksa program çalışmaz.
                 #onuda yukarıya alıp yazarsak yine program çalışmaz çünkü KeyboardInterrupt hatası alıyoruz.
            
    i += 1 #while döngüsü için yazdığımız i+= 1  
    
print(f'There are {i // 2} string values' if i > 0 else "There no string values")
        #i = 12 i // 2 = 6 

    
print(f'There is a {i} string' if i == 0 else "There are no string values")
                                  # i = 0 olur ve sağdaki string ekrana çıkar.

    
print(f'There is a single string value' if i > 0 else "There are no string values")
                                    # 12 > 0 dan bu yüzden soldaki string ekrana çıkacak.






#Q10) While döngüsü ile yazdığımız programın for döngüsü ile yazılmış hali.
items = ['apple', 55, 1.2, 'banana', lambda a: a, 'pear', None, 'cherry',  """Hello world!""", '''The Who''', ("a", 5), [("a", "5"), ("b", 3)]]

i = 0

for item in items:
    if(type(item) == str):#listenin içindeki stringler
        i += 1
        #i = 1,2,3,4,5 ve 6 
        #i = 6 
        
print(f'There are {i} string' if i > 0 else "There no string values")
        #i sayımızı buraya yazdırmak için {} kullanıyoruz.(Format metodu)
    
if(type(item) == str):
    i = 1 # eğer i += 1 dersek i = 1,2,3,4,5 ve 6 olur gerek yok burda i == 0 yapıp listede hiç string olmadığını yazdırıyoruz.
print(f'There are {i} string' if i == 0 else "There are no string values")
                                
if(type(item) == str):
    i += 1 #i = 1 yazsak bile program bize soldaki stringi yazdırkcak çünkü if i > 0 yazdık i 0 dan büyük olduğu için 
           #soldaki string ekrana yansıdı.
    
print(f'There is a single string' if i > 0 else "There are no string values")





#HW 04 Q1) 
def sum_positive_even_numbers_1(number_list): #For döngüsü ile listedeki sayıların 2'ye tam bölünebilen sayıların,
                                              #toplamını yazdırıyoruz
    sum = 0
    for n in number_list:
        if n % 2 == 0: # 2,4,6,8
            sum = n + sum # 2 + 4 + 6 + 8 = 20
                           
           
    return sum # 20 değerini return ediyoruz ki ekrana 20 sayısını verebilelim
print(sum_positive_even_numbers_1( [1, 2, 3, 4, 5, 6, 7, 8] ))







#Q2)
def sum_positive_even_numbers_2(number_list):
    sum = 0
    n = 0
    number_list = [n for n in number_list if n % 2 == 0] # 2,4,6,8 i aldık
    for n in number_list: # [2,4,6,8] listesinin içindeki elemanları 
        sum += n          #topluyoruz. ve toplamı return ediyoruz.
    return sum
print(sum_positive_even_numbers_2( [1, 2, 3, 4, 5, 6, 7, 8] )) 






#Q3)Bir liste oluşturup o listeyi ekrana yazdırıyoruz birde içindeki
#elmanları en az 2şer2şer olmak üzere arttırıp 2.listeyi ekrana yazdırıyoruz
def asc_range(start,end,increment = 1): #3 parametresi olan bir fonksiyon
    i = start                            #oluşturduk
    while i < end: #i < 12 = 5 < 12
        yield i #yield i yazmadığımızda nonetype objesini döngü içinde 
                 #kullanamyacağımıza dair hata alıyoruz.
                 #yield i = 5,6,7,8,9,10,11            
        i += increment #kaçar kaçar arttıracağımızı yazdırmak için.
                       # increment 3 ise sonuç [5,8,11]
print(list(asc_range(5,12))) #ilk önce normal listeyi yazdık.
print(list(asc_range(5,12,3)))  #ve 3er 3er arttırdık.
             







#Q4)
ar = []
def asc_range(start,end):
    for i in [start]:
        if i == end:
           
            ar.append(end)
            
            return ar
        else:
            if i != 4: # eğer i != 5 olursa listemizdeki 5 değeri silinir.
                ar.append(i)
                
            return asc_range(i + 1, end) # i + 3 yazarsak [5,8,11] listemize ulaşmış oluruz.
        
print(list(asc_range(5,11)))
#Malesef 2. listemi yani [5,8,11] listesini print yapamadım bir türlü bende yapabildiğim kadarını yaptım


#Q5) #Fahrenheit to Celsius
def getConvertTo():
    a = input("Enter Selection: ") #Kullanıcı F girerse F. to C. , C girerse C to F 
    while a != "F" and a != "C": # F veya C haricinde başka bir şey girerse soruyu tekrarlatıyoruz
        a = input("Enter Selection ")
    return a
a = getConvertTo() #Aldığımız değeri return ediyoruz

def FahrenToCelsius(start,end): # 2 parametresi olan bir fonksiyon yazdık
    print("   F  ", " C") # F ve C başlığımızı attık.
    
    for temp in range (start,end): #for döngüsüne alıp kullanıcının girdiği 2 sayının arasında sayıları alt alta yazdıracağız.
        converted_temp = (temp - 32) * 5/9 #Formülümüz.
        print(" ",format(temp)," ",format(int(converted_temp))) #temp = F , converted_temp ise Celsius
                                                                # İf temp = 50 , converted_temp = 10 
temp_start = int(input("Enter temprature to convert: "))
temp_end = int(input("Enter ending temprature to convert: ")) #Kullanıcıdan 2 ayrı sayı istedik.

FahrenToCelsius(temp_start, temp_end) 
#Bu fonksiyonla 2 soruyu birden çözmü oluyoruz Q5 ve Q6 nın cevabı olarak sayılabilir.



#Q7) #Yazdığımız stringi alıp bazı harfleri büyük bazı harflerini küçük yazdırıyoruz
def capitalize(string):
    string, result = string.title(), "" #word[-1].upper() yerine lower yazarsak sadece kelimenin baş harflerini büyük yazmış oluruz.
    for word in string.split():#2.word[-1] yerine [-2] yazarsak out of range hatası alırız -1 olmalı!
        result += word[:-1] + word[-1].upper() + " " #ilk word :-1 yazmalıyizki tüm harfleri alsın :-2 yazarsak bazı harfleri
                                                     #kaldırır.         
    return result[:-1] # :-1 yazmamızın sebebi tüm kelimeyi alıp ekrana yazdırmak.      

print(capitalize("This is a test string"))



#Q8)  #Fonksiyon kullanarak listenin içerisinde kaçtane string oluduğunu yazdırıyoruz.(For loop)
def count_strings(items):
    i = 0
    for item in items: 
        if(type(item) == str):
            i += 1
    return i

t =  ['apple', 55, 1.2, 'banana', lambda a: a, 'pear', None, 'cherry', """Hello world!""", -2, '''The Who''', ("a", 5), [("a", "5"), ("b", 3)]]

print(count_strings(t))



#Q9) #Bu seferde while loop kullanarak listede kaç tane string olduğunu yazdırıyoruz
def count_strings(items):
    i = 0
    count = 0 
    while i < len(items):
        if(isinstance(items[i],str)):
            count += 1
        i += 1
            
    return count   
            
                  
t =  ['apple', 55, 1.2, 'banana', lambda a: a, 'pear', None, 'cherry', """Hello world!""", -2, '''The Who''', ("a", 5), [("a", "5"), ("b", 3)]]

print(count_strings(t))

#type() adlı bir fonksiyon vardı. Bu fonksiyonu bir nesnenin hangi veri tipinde olduğunu tespit etmek için kullanıyorduk:
#
#>>> type('can')

#<class 'str'>

#İşte buna benzer şekilde, tip denetimi için kullanabileceğimiz bir fonksiyon daha var. Bu fonksiyonun adı isinstance().

#Q10)
import statistics 

def std_deviation( values ):
    return values

values = [1, 2, 3, 4, 5] #listemizi tekrar tanımlamalıyız  %s = format methodu yani is den sonra hesaplanan sayı gelecek.

print(statistics.stdev(values))

# statistics fonksiyonu verilen listedeki elementlerin averajlarını hesaplayabilir.
#stdev() is standart deviatiton'un kısaltılmışı hocamız 10. soruda bunla ilgili bir formülde vermişti bizde hocamızın  
#bizden istediğini python diline döküyoruz


#Q11)
import numpy as np # numpy'i np olarak tanıttık
def correlation_coefficient(sample_a , sample_b): #2 parametreli bir fonk. oluşturduk
    
    return np.corrcoef(sample_a,sample_b)        #np.corrcoef(), np = numpy sample_a ve b yi return ediyorz
# np.corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>

sample_a = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
sample_b = [ 215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]   
#sample_a ve sample_b ye değer atıyoruz 
print(np.corrcoef( sample_a, sample_b)) #return'daki işlem yapılarak sonucu print ediyoruz.



#HW 05
#Q1)
#Nilakantha Series (Pi hesaplama)

the_pi = 0.0
the_num = 2.0

for i in range(500000):
    # the_pi = 0.13968253968253966 (the_num'dan önceki pi sayısı) 
    the_pi = the_pi + 4.0 /(the_num* (the_num+1.0)* (the_num+2.0)) - 4.0 /((the_num+2.0)* (the_num+3.0)* (the_num+4.0))
    the_num += 4.0 
    # the_pi = 0.1415926535897915 (the_num += 4.0'dan sonra pi sayısı)

print(the_pi + 3 ) 

#the_pi + 2 yazarsak 2.14.. diye gider (the_pi + 3) yazmamızın sebebi 3.14 ile başlatıyoruz.
#the_pi = 3.1415926535897913

#Q2)
def sum_first_n(n): #fonksiyonumuzu oluşturduk. fonksiyon_ismi(aldığı değer)
    
    return n * (n + 1) // 2   # 10 * (10+1) = 110 // 2 = 55 bize 10'a kadar olan sayıların toplamını verir.
    #return ederek işlemin gerçekleşmesini sağlıyoruz böylece ekrana sonucu yazdırabileceğiz.

#n = 10 #n parametresine sayımızı atıyoruz

print(sum_first_n(10)) #sonucu print ediyoruz.




#Q3)
import math #math kütüphanemizi import ettik ki içindeki factorial() methodunu kullanabilelim.

def mul_first_n(a): #fonksiyonumuzu oluştuyoruz..
    
    return math.factorial(a) #işlemimizi return ediyoruz math.factorial(4) = 4x3x2x1 = 24 

a = 4 # sayı atayarak o sayının faktoriyelinin hesaplanmasını sağlıyoruz.

print(mul_first_n(a)) # sonucu print ediyoruz.


#Q4)
def right_justify( in_str): #fonksiyonumuzu oluşturduk. 
    
    val = "▫"*5  #değişkenimizi tanımladık  val = ▫▫▫▫▫ 
    #format methodu ile bizden istenileni gerçekleştirebiliriz. 
    
    print("{}{}{}".format(val, in_str, val))  #{▫▫▫▫▫}{NEU}{▫▫▫▫▫} = val, in_str, val

right_justify("NEU") #fonskiyonumuzun parametresine değerimizi atadık. in_str = NEU

#ve sounç; ▫▫▫▫▫NEU▫▫▫▫▫


#Q5)
import statistics #Median methodunu kullanmak için ilk olarak içinde bulunduğu kütüphaneyi tanımlamamız gerek import
#etmemiz gerek ki kullanabilelim.

def median(values): #fonskiyonumuzu oluşturduk.
    return values #Values'i return ederek onu values = [1, 3, 5, 7] ve üzerinde gerekli işlemlern yapılmasını sağladık.

values = [1, 3, 5, 7]

print(statistics.median(values)) #eğer  len(values) = 4 ise çıkan sonuç ortadki 2  sayının toplamı / 2 
# [ 1, 3 , 5 , 7] = listenin eleman sayısı 4 yani çift sayı çift sayı olduğu için (5 + 3) / 2 = 4.0
# values = [1, 3 , 5] = eleman sayısı = 3 yani tek sayı bu yüzden listenin ortadaki elemanını ekrana yazdırılacak.



#Q6)
def letterize(number): #fonksiyonumuzu oluşturduk.
    return number #number = 16384 değerimizi return ettik.

#eğer return etmezsek expected an indented block hatası alırız : 'ten sonra bir alt satıra inilip 4 boşluk bırakılıp
#birşeyler yazmalıyız ki ortada bir fonskiyon olduğu anlaşılsın ortada bir değerin return edildiği belli olsun.
#bu soru için sadece return number dememiz yeterli

number = 16384 #numaramızı yazdık.

res = [str(x) for x in str(number)] 
#numaramızı alıp str yaptık yani str(x) = "1", "6" ,"3" , "8" , "4"
#str(x) = her bir rakama "" işareti atadık
#str(number) = 16384 sayısını string olarak tanımladık.
#ve res = ["1", "6", "3", "8", "4"] = liste olarak dışarıya çıkmasının sebebi [] parantezlerini kullanmamız bu [] içine
#yazdık ki hocamızın bizden istediği gibi bir çıktı olsun 

print(res) # = ["1", "6", "3", "8", "4"]
#burda çıkan res str cinsinden değil. for döngüsünden bir liste çıkıyor sadece.Onu print ettik.

print("The list is = " + str(res)) #burda res'i print ederken str(res) yazmazsak hata alırız.

#hata = Can only concatenate str (not "list") to str yani siz listenin yanında bir string ile print etmek isterseniz.
# o listeyi str'ye çevirmeniz lazım çünkü str + str ekrana çıkabilir ama str + list olmaz.






#Q7)
def letterize(number):
    return number 

number = 20910

res = [int(x) for x in str(number)] #int(x) = 2,0,9,1,0

#str(number) yazmamızın sebebi; for döngüsünde int bir değer döndürülemez hata alırız. ( int' object is not iterable ).
#string olarak çeviriyoruz ki for döngümüz çalışssın.

print(res)





#Q8)
import matplotlib.pyplot as plt #grafiğimizi oluşturmak için gerekli kütüphanemizi import edip onu plt olarak tanımladık.
import numpy as np #numpy kütüphanesini import ederek onu np olarak tanımladık.
%matplotlib inline #Jupyterlab'da çalıştıracaksanız bu kodu kullanın.

x = np.arange(0, 4*np.pi ,0.1)   # start,stop,step,  4 * np.pi = 12.566370614359172
#x = np.arange(4*np.pi) = array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.])

y = np.sin(x) # x'in sinüsünü aldık 
z = np.cos(x) # ve cosünüsü

plt.plot(x,y,x,z) # aldığımız sinüs ve cosünüsü (x,y) grafiğini çizdirdik mavi olan, sonra ise (x,z) grafiğini çizdirdik.

#plt.xlabel('x values from 0 to 4pi')   
#plt.ylabel('sin(x) and cos(x)')
#plt.title('Plot of sin and cos from 0 to 4pi')
#plt.legend(['sin(x)', 'cos(x)'])    

plt.show() #işlemlerden sonra grafiğin ekranda görünmesi için plt.show() kodumuzu kullandık.



#Q9
def grid(x, y):
    
    return "\n".join("[]" * y for _ in range(x))

print(grid(4, 3))














#Q10)
def fibo(num): #fonksiyonumuzu tanımladık.
    first = 0 #değişkenlerimizi tanımladık. 
    second = 1 #eğer second = 0 yaparsak bulunan tüm sayılar 0 olacak.
    result = [] #boş listemizi tanımladık.
    
    print("Fibonacci series is;") 
    
    for i in range(0,num): #0 dan başlamazsak 10'a kadar olan fibonacci sayısının son sayısını listemize yazdıramayız.
# 0 ve num yani num = 10  for i in range(0,10)   

        third = first + second # 0 + 1 = 1 , 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13..
        
        #bulduğumuz bu sayıları listemize ekliyoruz yani result = [1, 1, 2, 3, 5..]
        result.append(second)
        
        first = second #first değişkenimizi second'a eşitlemezsek bu listedeki bütün elamanlar = [1, 1, 1, 1, 1..]
        second = third #second değişkenimizi de third e eşitleyerek for döngümüzün içinde 10'a kadar olan sayıların
        #listelerini elde ediyoruz first = second eşitlediğimiz için second'ı da third'e eşitlememiz lazımki yine liste
        # = [1, 1, 1..] olmasın.
        
    return result # ve listemizi return ediyoruz ki ekrana yazdırabilelim return result yazmadığımız takdirde
    #ekranda sadece None yazar ve tabiki return değişkenizimi for döngüsünün dışına yazıyoruz..


print(fibo(10)) #ve num değişkenimize değer atıyoruz ki listemizi elde edebilelim.. 


# burdaki linkte fibonacci ile alakalı bir resim var daha iyi anlamak için bakabilirsiniz..
#https://en.wikipedia.org/wiki/Fibonacci_number#/media/File:PascalTriangleFibanacci.svg






































































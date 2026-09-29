print(10*"=",'PYTHON FUNCTION', 10*"=")
def greet(name):
    '''
    Fungsi ini menyapa nama orang
    sebagai parameter
    '''
    print("Hai",name,"Good Morning!!!")
print("Hasil ini adalah print dari komentar yang ada di dalam function",greet.__doc__)
greet('Asep')


print("")
print(10*"=",'FUNCTION ARGUMENTS', 10*"=")
def sapa(nama,msg):
    print("Hai",nama,',',msg)
sapa('Asep','Good Morning')


print("")
print(10*"=",'DEFAULT ARGUMENTS', 10*"=")
# parameter msg jadi opsional untuk diisi
# Tapi parameter setelahnya juga harus ada defaultnya
def sapa2(nama,msg="Good Morning"): 
    print("Hai",nama,",",msg)
sapa2('Hadniw')


print("")
print(10*"=",'ARBITRARY ARGUMENTS', 10*"=")
# Fungsi ini memanggil semua variabel di dalam tuples
def sapa3(*nama): 
    for name in nama:
        print("Hello",name)
sapa3('Hadniw','guawaim','Hitaf','Rabas')


print("")
print(10*"=",'PYTHON RECURSION', 10*"=")
def faktorial(x):
    if x == 1:
        return 1
    else :
        return (x*(faktorial(x-1)))
num = 3
print("Hasil Faktorial dari", num,"Adalah", faktorial(num))


print("")
print(10*"=",'ANONYMOUS FUNCTION', 10*"=")
f = lambda num:num*2
print("Kali dua dari",2,"Adalah:", f(2))


print("#=== Penambahan Fungsi Filter() ===#")
# Fungsi ini mengambil semua variabel yang ada di dalam list dan mengembalikan oleh fungsi yang berisi item yang telah dievaluasi ke TRUE (Ada kondisi yang menyebabkan variabel tersebut bernilai TRUE)
listangka = {1,3,5,4,6,7,8,11,10}
new_listangka = list(filter(lambda x: (x%2 == 0),listangka))
print("Penggunaan Filter():",new_listangka)


print("#=== Penambahan Fungsi Map() ===#")
# Fungsi ini mengambil semua variabel yang ada di dalam list dan mengembalikan oleh fungsi untuk setiap item
listangka = {1,3,5,4,6,7,8,11,10}
new_listangka2 = list(map(lambda x : (x*x),listangka))
print("Penggunaan Map(): ",new_listangka2)


print("")
print(10*"=",'GLOBAL, LOCAL, AND NON-LOCAL VARIABLE', 10*"=")
print("#=== Global Variable ===#")
c = 60
def tampil():
    global c
    print("C dalam:", c*2)
tampil()
print('C luar:', c*2)

print("")
print("#=== Local Variable ===#")
def tampil2():
    d = 20
    print("d dalam:",d)
tampil2()
# print("d luar:", d) 
# akan muncul peringatan d is not defined

print("")
print("#=== Non-Local Variable ===#")
# Ada 2 kondisi ada yang nonlocal memengaruhi ada yang tidak memengaruhi
# Tergantung variabel local didefinisikan terlebih dahulu atau belakangan
print("Yang memengaruhi")
def tampil3():
    e = 30

    def tampil3_2():
        nonlocal e
        e = 40
        print("e nonlocal:", e)
    tampil3_2()
    print("e local:", e)
tampil3()
print("Yang tidak memengaruhi")
def tampil4():
    f = 30
    def tampil4_2():
        nonlocal f
        f = 40
        print("f nonlocal:", f)
    print("f local:", f)
    tampil4_2()
tampil4()

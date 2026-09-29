#=== LIST ===#
print(10*("="),"LIST",10*("="))
List = []
print(List)
List = [1,2,3,4]
print(List)

#=== DICTIONARY ===#
print("\n",10*("="),"DICTIONARY",10*("="))
Dict = {'first':'BMW', 'second':'McLaren', 'Third':'Chevrolet'}
print(Dict)
Dict['Third'] = 'Harley Davidson'
print(Dict)

#=== TUPLES ===#
print("\n",10*("="),"TUPLES",10*("="))
Tuples = (1,2,3,'MySkill')
print(Tuples)
print(Tuples[2])
print(Tuples[:2])   # Sebelah kiri batas minimum dan kanan batas maksimum dari indek yg dicari
print(Tuples[3][2]) # Mencari indeks ke 3 lalu mencari part ke 2

#=== SETS ===#
print("\n",10*("="),"SETS",10*("="))
Sets = {1,2,3,4,5,5,5}
print(Sets)
Sets.add(6)
print(Sets)

#=== Modifikasi SETS ===#
Sets1 = {1,2,3,4}
Sets2 = {3,4,5,6}
print(Sets1.union(Sets2), "=====", Sets1 | Sets2)           # Gabungan 
print(Sets1.intersection(Sets2), "=====", Sets1 & Sets2)    # Irisan
print(Sets1.difference(Sets2), "=====", Sets1-Sets2)        # Isi Sets1 dikurangi dengan Sets2
print(Sets2.difference(Sets1), "=====", Sets2-Sets1)        # Isi Sets2 dikurangi dengan Sets1
print(Sets1.symmetric_difference(Sets2), "=====", Sets1 ^ Sets2) # Gabungan tanpa irisan
Sets1.clear() # Menghapus isi Sets1
print(Sets1)

#===== CONDITIONAL STATEMENT =====#
print("\n",10*("="),"IF ELSE",10*("="))
#=== IF Condition ===#
Num = 7
if Num >= 0 :
    print(Num,"=","Positive Number")

Num2 = 0
if Num2 > 0 :
    print(Num2,"=","Positive Number")
elif Num2 == 0 :
    print(Num2,"=","Zero Number")
else :
    print(Num2,"=","Negative Number")

#=== Loops ====#
print("\n",10*("="),"LOOPING",10*("="))
#== While Loop

Num3 = 1
odds = []
while Num3:
    if Num3 %2 == 0 :
        odds.append(Num3)
    if Num3 >= 100 :
        break
    Num3 += 1
print(odds)

#== For Loop
List = [1,2,3,4]
for i in List:
    print(i)

#=== Fuction ===#
print("\n",10*("="),"FUNCTION",10*("="))
#== With Return
def pow(a,b):
    return a+b
print(pow(1,2))

#== No Return
def pow(a,c):
    print(a*c)
pow(2,3)
#===== STRING =====#
quote = "Saya akan lawan!!!"
print(quote)

print("Saya manusia biasa"[1]) # Langsung mengambil yang ada di dalam

print(10*("="),'SINGLE STRING',10*("="))
quote1 = 'Saya akan lawan'
print(quote1)

print(10*("="),'DOUBLE STRING',10*("="))
quote2 = "I'm akan akan"
print(quote2)

print(10*("="),'TRIPLE STRING',10*("="))
quote3 = '''Saya akan "lawan" '''
print(quote3)


print("\n")
print(20*("="),'DELETE AND UPDATE STRING',20*("="))

print("#===# Update String #===#")
String1 = "Hello, I'm MySkill Student"
print('Intial string:', String1 )

print("#1")
ganti1 = list(String1)
ganti1[1] = 'I'
String2 = ''.join(ganti1)
print(String2)

print("#2")
String3 = String1[0:1] + 'a' + String1[2:]
print(String3)

print("\n#===# Reverse String #===#")
print("#1")
print(String1[::-1])

print("#2")
rev = "".join(reversed(String1))
print(rev)

print("\n#===# Slicing String #===#")
print('String1:', String1)
print('#1')
print("Slice from index 1 to 3:",String1[1:3])

print('#2')
print("Slice from index 3 to -1:",String1[3:-1])

print("\n#===# Update Entire String #===#")
String4 = String1
print('Entire String:', String1)
String4 = "Hidup Jokowi!!!"
print('Now String:',String4)

print("\n#===# Delete String Character #===#")
print('Entire String:', String1)
String5 = String1[0:2] + String1[8:]
print('Now String:',String5)

print("\n#===# Delete String #===#")
String6 = String1
print('Print Pertama:',String6,"\n")
#del String6
#print('Print Kedua:',String6) # Akan muncul error



myList = ["Jakarta", "Bandung", "Surabaya", "Purwokerto"]
print(myList)
print("Panjang dari myList:",len(myList))
print("Tipe data dari myList:", type(myList))


print("")
print(10*("="),"CONSTRUCTOR OF LIST",10*("=") )
myList = list(("Bandung", "Surabaya", "Jakarta", "Purwokerto"))
print(myList)

print(10*("="),"MODIFICATION OF LIST",10*("="))
print("Entire List:", myList)
print("Index ke-0:", myList[0])
print("Index ke-1 s/d 2:", myList[1:2])
print("Index ke-0 s/d -2:", myList[:-1])


print("")
print(10*("="),"CHANGE ELEMENT VALUE",10*("="))
print("Entire List:", myList)

myList[0] = "dungBan"
print("Newest List:", myList)

print("")
print("#===","Memasukkan item lebih atau kurang dari yang diganti","===#")
print("Entire List:", myList)
myList[1:2] = ["Tangerang", "Bekasi"] #Harus menggunakan min/max indexing
print(myList)

print("")
myList[1:] = ["Bali"]
print(myList)


print("")
print("#===","Add Item to List","===#")
print("Entire List:", myList)
myList.append("Madura") # Menambahkan ke paling belakang
myList.insert(1,"Jombang")
print(myList)

myList2 = ["Kyoto", "Tokyo", "Fukushima", "Seoul", "Gangnam"]
myList.extend(myList2)
print(myList)

print("")
print("#===","Delete Item to List","===#")
myList.remove("Kyoto")
print(myList)

myList.pop(0)
print(myList)
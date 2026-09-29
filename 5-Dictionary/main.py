print(10*"=","DEFINING DICTIONARY",10*"=")
print("=== #1 ===")
Dict1 = {1:'Jakarta', 2:'Bandung',3:'Tangerang' }
print(Dict1)

print("")
print("=== #2 ===")
Sumatera = dict([
    ('Satu','Aceh'),
    ('Dua','Medan'),
    ('Tiga','Way Kambas'),
    ('Empat','Padang')
])
print(Sumatera)

print("")
print("=== #3 ===")
Kalimantan = dict(
    satu= 'Samarinda',
    dua= 'Pontianak',
    tiga= 'Banjarmasin',
    empat= 'Palangkaraya'
)
print(Kalimantan)

print("")
print(10*"=","ACCESING DICTIONARY",10*"=")

# Salah ❌
# print(Dict1[Jakarta])

# Benar ✔️
print("Entire Dict: ",Dict1)
print("Kota kedua adalah:",Dict1[2])
print("print menggunakan Square Bracket []:",Sumatera['Satu'])
# Jika memanggil key yang tidak ada dalam dict maka akan muncul error
# print("Kota yang tidak ada dalam dict manapun:", Dict1['Toronto'])


print("")
print(10*"=","ADDING NEW ENTRY DICTIONARY",10*"=")
print("Entire Dict1:",Dict1)
Dict1[4] = 'Bekasi'
print("Dict1 Now:", Dict1,'\n')
print("=== Ubah Value ===")
Dict1[2] = 'Sukabumi'
print('Dict1 Now:', Dict1)


print("")
print(10*"=","BUILD DICTIONARY INCREMENTALLY",10*"=")
Dict4 = {}
type(Dict4)

Dict4['Nama'] = ['Iqbal', 'Hanafi', 'Ghost']
Dict4['Umur'] = [19,26]
Dict4['Posisi'] = ['Semester 2', 'Data Scientist']
Dict4['Makanan Favorit'] = ['Nasi Goreng', 'Mie Goreng', 'Nasi Kuning', 'Nasi Uduk']

print("")
print(Dict4)
print("Umur pada Dict4:", Dict4['Umur']) 
print("Makanan kesukaan Iqbal kedua adalah", Dict4['Makanan Favorit'][1])

# Bahkan key bisa berupa tipe data apa saja
Dict5 = {111:'Aselole', True:'Asep', 27.3:'Ucok'}
print("")
print("Ambil Value dari Dict campur tipe data: ",Dict5[True])

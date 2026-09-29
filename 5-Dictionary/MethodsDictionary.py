print(10*"="," .clear() ",10*"=")
Dict={ 'a':10, 'b':20, 'c':30}
print(Dict)
Dict.clear()
print(Dict)

print()
print(10*"="," .get() ",10*"=")
Dict2 = {'a':10, 'b':20, 'c':30}
print("Nilai A adalah ",Dict2.get('a'))

print()
print(10*"="," .keys() ",10*"=")
Dict3 = {'a':10, 'b':20, 'c':30}
print(Dict3.keys())

print()
print(10*"="," .update() ",10*"=")
Dict4 = {'a':10,'b':20,'c':30}
Dict5={'b':200,'d':100}
print("Dictionary 4:",Dict4)
Dict4.update(Dict5)
print("Dictionary 4 update:",Dict4)

print()
print(10*"="," .pop() ",10*"=")
print('Dict 4 sebelum pop:',Dict4)
Dict4.pop('b')
print('Dict 4 setelah pop',Dict4)

print()
print(10*"="," .popitem() ",10*"=")
print('Dict 4 sebelum popitem:', Dict4)
Dict4.popitem()
print('Dict 4 setelah popitem:', Dict4)
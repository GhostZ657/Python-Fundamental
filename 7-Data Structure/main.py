print(10*"=",'LINKED LIST',10*"=")
linked_list = ['First', 'Second', 'Third']
print("Linked List:", linked_list)
print()

# Menambahkan Item
linked_list.append('Fourth')
linked_list.append('Fifth')
linked_list.insert(3,'Sixth')
print("Linked List Now:", linked_list)
print()

linked_list.remove('Second')
print("Linked List setelah penghapusan:",linked_list)
print()


print(10*"=",'STACK',10*"=")
# Last in First Out
stack_list = ['First', 'Second', 'Third']
print('Stack List:', stack_list)
print()

stack_list.append('Fourth')
stack_list.append('Fifth')
print('Stack List Now:', stack_list)
print()

# Printing Top
print("Top dari stack:",stack_list[-1])
print()

# Popping Element
stack_list.pop()
print("Stack List setelah pop:", stack_list)
print()


print(10*"=",'QUEUE',10*"=")
# First IN first OUT
Queue_list = ['First', 'Second', 'Third']
print("Queue List:", Queue_list)
print()

Queue_list.append('Fourth')
Queue_list.append('Fifth')
print("Queue List Now:", Queue_list)
print()

print("Top dari Queue:", Queue_list[0])
print()

# Popping Element
Queue_list.pop(0)
print('Queue List setelah popping:', Queue_list)
print()


print(10*"=",'HASHMAP',10*"=")
hashmap = {0:'First', 1:'Second',2:'Third'}

def printdict(d):
    for key in d:   # Setiap key yang ada di d(hashmap), maka print key -> value dari key
        print(key,'->',d[key]) 
printdict(hashmap)


# Listas
mylist = []
if mylist:
    print("ok")
else:
    print("vide")

mylist = [1,2,3,4,5,"i put whatever"]
mylist.append("a la fin")
mylist.insert(1,"java")
# mylist.pop()
print(len(mylist))
print(mylist[-1])
print(mylist)
print(type(mylist))

#slicing
print(mylist[20:])
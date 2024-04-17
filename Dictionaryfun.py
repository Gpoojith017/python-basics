word=input()
print(word)
store=dict()
print(store)
store['p']=23
store['q']="abcd"
store['w']=21
store["hello"]=222
store[12]=11
print(store)
allkeys=store.keys()
print(allkeys)
for ele in allkeys:
    print(ele,store[ele])

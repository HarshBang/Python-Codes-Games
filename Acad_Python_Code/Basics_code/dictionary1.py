dict1={'name':'Vinayak','Roll_no':123,'Course':'STME'}
print(dict1)
print(dict([('name','abc'),('Roll_no',213),('course','CSDS')]))
dict2={x:2*x for x in range(1,10)}
print(dict2)


d={}
d['name']='Abhiram'
d['job']='student'
d['age']=23
print(d)
d['age']+=1
print(d)
d1={'ab':'QWERTY','at':'ASWD','bc':'uiojkl'}
for key in d1:
	print(key,'=>',d1[key])
    
for i in d:
    print(i,'==>',d[i])
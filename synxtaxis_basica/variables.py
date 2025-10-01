a=5


b=3.5

name="Saltos"

is_active= True

print(a,b,name,is_active)

print(type(a))
print(type(name))
print(type(is_active))


device='router'
id=101

print(f'Device{device} and ID:{id}')


#operaciones aritmeticas 

numbera=2
numberb=3


#result=numbera+numberb
#print(f"The sum is : {result}")


print("The result of adding two numbers is: ",numbera+numberb)
print("The result is: ",numbera-numberb)
print("The result is: ",numbera*numberb)
print("The result is: ",numbera**numberb)
print("The result is: ",numbera/numberb)
print("The result is: ",numbera//numberb)


#String
print("STRINGS")
name = "Yusseppe Saltos"
print(name.upper())
print(name.capitalize())
name2=name.upper()
#print(name2.lower)


language='PYTHON'
print(language[0])
print(language[-1])
print(len(language))

#List
print("#List")
device=['router', 'switch', 'cable', 45, True, False,]
print(len(device))


print(device[0])
print(device[-1])

device.append('Server')

print(device)

names=list()
names.append('Yusseppe')
names.append('Steve')
names.append('Aby')
names.append('Paititi')
print(names)
names[1]='Juanjo'
print(names)
print(names.pop())
print(names)


numbers=list(range(10))
print(numbers)
selectednumbers=numbers[2:4]
print(selectednumbers)

print(numbers[:-1])
print(numbers[:3])
numbers[2:3]=[100,100]
print(numbers)

#TUPLES
print('#TUPLES')

containertuple=(10, 20)
print(containertuple[0])

containerlist=list(containertuple)
print(type(containerlist))


#DICTIONARY
print('#DICTIONARY')

animals=('#TUPLES')

animals={'dog':'nice','cat':'pretty','cow':'big', 'monkey':'dirty'}

print(animals['cow'])

animals['cat']='fast'
print(animals['cat'])

print('cow' in animals)

del animals['monkey']
print(animals)

animals['monkey']='dirty'
animals['viper']='little'
animals['turtle']='hard'

for item in animals:
    feature=animals[item]
    #print("%item has %feature"%(item, feature))

print('okkk!!!!')
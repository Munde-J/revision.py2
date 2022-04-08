from stat import FILE_ATTRIBUTE_SPARSE_FILE


age=35
age1=35.0

print(type(age))
print(type(age1))

description="""Morning
I had Milo

Afternoon
I had fruits

Evening
I had juice"""
print("This is my description: " + description)

# String slicing
name="Charter"
print(name[0])

print(name[2],name[3],name[4])
print(name[2:5])

print(name[-1])
print(name[2:])

word ="hospital"
print(word.capitalize())
print(word.upper())
print(word.lower())

shaddyAge =95
name="Shaddy"

print(shaddyAge>18)
print(shaddyAge<=18)

print(shaddyAge==18 and name == "Shaddy")

print(shaddyAge==18 or name == "Shaddy")

myvar = ["orange","banana","banana",23,75j]
newVar =myvar.append("Accra")
print(myvar)

myvar.insert(0,123)
print(myvar)

# set
myvar = {"orange","banana","banana",23,75j}
print(myvar)
print(len(myvar))

myvar = ["orange","banana","banana",23,75j]
myvar[1]="coconut"
print(myvar)
myvar = {"orange","banana","banana",23,75j}
myvar.add("ground")
print(myvar)

# dictionary
myvar = {"orange","banana","banana",23,75j}
myvar.add("ground")
for e in myvar:
  print("This element is",e)
  print(myvar)

  
  loby = ["loby",23,"Italian"]
  bandy= ["bandy",29,"Ghanian"]
  bandy= ["bandy",23,"Ghanian"]
  Brundi= ["brundi",23,"Togolese"]

  people={"loby":loby, "bandy":bandy, "brundi":Brundi}
  print(people)

  print(people["loby"])
  print(people["loby"][2])

#   people.add("john",25)
#   print(people)
print(people.get("bandy"))

print(people.keys())



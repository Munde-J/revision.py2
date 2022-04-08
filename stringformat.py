from unicodedata import name


name="kobby{}"
age =str(40)

print(name+age)
print(name,age)

name="kobby"
age =40
nationality ="chinese"

print(name.format(age))
data = "hello my name is {} and age is {} and I am a {}"
print(data.format(name,age,nationality))
 
name= "Arthur"
age=45
nationality="Nigerian"

description="My name is {1} and I am {2} years old and I  am {0}"
print(description.format(nationality,name,age))


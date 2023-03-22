print("Hello World !", 1, 2, sep="~", end="009\n")
print("LOL")
#STRINGS ARE IMMUTABLE !!!
a = "!!!#!Abhi!#!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #removes trailing characters
print(a.replace("Abhi", "lmao"))
print(a.split("#"))
h = "introduction to Python"
print(h.capitalize())
print(h.center(30))  # number of extra spaces + len(string) = 30
print(len(h))
print("length of centered string:",len(h.center(25)))
print(a.count("!#"))
print(h.endswith("python")) # h.startswith("introduction") 
print(h[5:15])
print(h.endswith("to", 5, 15)) #checks whether the substring [5:15] ends with "to"
str = "This dude does stuff pretty neat. He is skilled!"
print(str.find("is")) #returns -1 if not found  
#print(str.index("lol")) # same as above but returns exception when not found
print(str.islower())
print(str.isspace())
print(h.istitle()) #returns true if all words have first letter capital
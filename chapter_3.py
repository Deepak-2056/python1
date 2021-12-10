name = "what is your name , where do you livve , i am form nepal"
#print (name[0])
#print (len(name))
#print(name.endswith("nepal"))
#print(name.endswitch("what"))
#print(name.count("what"))
#print(name.capitalize())
#print(name.find("do"))
#print(name.replace("nepal","nepali"))
#about = " hello i am \t from nepali.\n i speak neapli language "
#print(about)
#name = input("enter your name")
#print("good afternoon \t" + name)


letter = """ dear <|name|>, good morning . i am happy to tell you about 
your selected!
Date: <|date|>

"""
name = input("enter your name \n ")
date = input("enter your date \n ")
letter = letter.replace("<|name|>" , name)
letter = letter.replace("<|date|>" , date)
print(letter)





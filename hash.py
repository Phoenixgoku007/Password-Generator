""" â ï¸ In progress â ï¸ """

" " " ð  This Program is mainly designed to generate a password which is a divisible of 8 and 6.In future more updates will be provided for generating a password in any length.If you have any suggestions to make this password generator to generate any length of password other than divisible of 6 and 8 without  missing any characters then you can contribute to this software... ð """

""" ð¡ï¸ you can check the strength of the passwords generated from my program on HowSecureIsMyPassword website ð"""

import random #To randomly select alphabets and speial characters

try:
 small="abcdefghijklmnopqrstuvwxyz"
 caps=small.upper() #Alphabets in  capital form
 special="!@#$%^&*()_-+=,<.>/?:;[]{}`~" 
 s2=small[::-1] #Reversed version of small
 c2=caps[::-1]  #Reversed version of caps
 spe2=special[::-1] #Reversed version of special
 pas=""  #To store the randomly generated values in upcoming steps
 new_pas=[] #To append the password generated into a list to shuffle it up



 Len=int(input("\nEnter the length of the password combination you need but It must be atleast greater than 8â£ characters in Length...ð¤")) #Get the length of the password from user

 print("\n\nYour password Length is ð...\n\nð",Len)
 
 if(Len<8): 
     print("\n\n ð Sorry!,Atleast you have to create a password which is 8 digit long otherwise in this modern age it will not take even â³ few seconds âï¸ to hack your password!!! ð")
     
 else:
    
  if(Len==8 or Len%8==0):
     print("\n\nð° ð² Your Password is safe for next âï¸few Hoursâï¸ only...consider creating passoword with more than 10 characters ð :)")
     
     for i in range (0,Len//8): # reversed version of small letters are added here
         pas=pas+random.choice(s2)
     
     for j in range (0,Len//8): # Reversed version of caps letters are added here
         pas=pas+random.choice(c2)
         
     for k  in range (0,Len//4): # Reversed version of special characters are added here
         pas=pas+random.choice(spe2)
    
     for l in range (0,Len//8): # small letters are added in a random manner
         pas=pas+random.choice(small)
         
     for m in range (0,Len//8): # capital letters are added in a random manner
         pas=pas+random.choice(caps)
         
     for n in range (0,Len//4): # special characters are added in a random manner
         pas=pas+random.choice(special)
         
  

     
     
  else:
     
     for i in range (0,Len//6): # reversed version of small letters are added here
         pas=pas+random.choice(s2)
     
     for j in range (0,Len//6): # Reversed version of caps letters are added here
         pas=pas+random.choice(c2)
         
     for k  in range (0,Len//6): # Reversed version of special characters are added here
         pas=pas+random.choice(spe2)
    
     for l in range (0,Len//6): # small letters are added in a random manner
         pas=pas+random.choice(small)
         
     for m in range (0,Len//6): # capital letters are added in a random manner
         pas=pas+random.choice(caps)
         
     for n in range (0,Len//6): # special characters are added in a random manner
         pas=pas+random.choice(special)

 new_pas.append(pas) # uploading the generated password into a list
 random.shuffle(new_pas) # mixing up each and individual digits of the password generated
 print("\n\nð Here Is Your Precious Key ð\n\n","ð",new_pas,"ð")

        
except: # To avoid unexpected error or infinite loop and provide meaning full details of the problem occured

     print("\n\n ðµ Invalid Input!!!, ð Try Once Again :)")
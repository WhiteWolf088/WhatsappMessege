#Download External Package
#Type "pip pywhatkit" in terminal in your Ide


import pywhatkit
Number=input("Enter the Number  : ")
Messege=input("Enter the messege  : ")
Hour=int(input("Enter the Hour : "))
Minutes=int(input("Enter the Minutes : "))
pywhatkit.sendwhatmsg(Number,Messege,Hour,Minutes)

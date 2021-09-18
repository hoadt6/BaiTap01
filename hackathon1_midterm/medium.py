def anagram_number(number):
    result = False
    number_list = list(str(number))
    number_list.reverse()
    number_reverse_str = ''.join(number_list)
    if (str(number) == number_reverse_str):
         result = True
    return result
    pass

def roman_to_int(s):
     roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
     i = 0
     num = 0    
     while i < len(s):
          if i+1<len(s) and s[i:i+2] in roman:
           num += roman[s[i:i+2]]
           i+=2
          else:
            num+=roman[s[i]]
            i+=1
     return num
     pass

print(anagram_number(121121))
print(anagram_number(1254))

print(roman_to_int("XI"))
print(roman_to_int("IX"))
print(roman_to_int("IXIV"))
print(roman_to_int("XL"))
print(roman_to_int("CMDX"))

import urllib3
from bs4 import BeautifulSoup
import codecs

def extract_names(filename):
    
  # Opening the html file
  HTMLFile = open("baby1990.html", "r")
  
# Reading the file
  index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
  S = BeautifulSoup(index, 'lxml')
 
  file = codecs.open("baby1990.html", "r", "utf-8")
  print(file.read())


 
  return S

pass
 

print(extract_names("http://baby1990.html"))

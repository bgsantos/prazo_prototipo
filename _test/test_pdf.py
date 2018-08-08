from bs4 import BeautifulSoup
import os
# pdftohtml -noframes -s -i <file>

#test1
dirname = os.path.split(__file__)[0] 
filename = "{}/../static/20180807INTDJETJRJ_1.html".format(dirname)
file = open(filename,'rb')

soup = BeautifulSoup(file.read(), 'html.parser')

t = soup.find_all(attrs={"class":"ft13"})

print(t[1].get_text())
print(t[1].next_sibling.next_sibling.next_sibling.next_sibling.get_text()) # id
print("*" * 50)

dirname = os.path.split(__file__)[0] 
filename = "{}/../static/20180808CAPDJETJRJ_1.html".format(dirname)
file = open(filename,'rb')

soup = BeautifulSoup(file.read(), 'html.parser')

t = soup.find_all(attrs={"class":"ft13"})

print(t[1].get_text())
print(t[1].next_sibling.next_sibling.next_sibling.next_sibling.get_text()) # id
print("*" * 50)



from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

rea = urlopen('https://www.snapdeal.com/')
a = bs(rea.read(),"html.parser")
for i in a.findAll('a'):
    if 'href' in i.attrs:
      print(i.attrs['href'])
    # print(i)

# for i in a.find('div', {'id': 'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)')):
#     if 'href' in i.attrs:
#         print(i.attrs['href'])
# link=[]
# x=a.select('img[src^="https://n1.sdlcdn.com/imgs/f/n/u"]')
#
#
# for img in x:
#     link.append(img['src'])
# for l in link:
#     print(l)


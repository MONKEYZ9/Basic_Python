from typing import Sized
import requests as req
from bs4 import BeautifulSoup as bs

url = 'http://www.google.com'
res = req.get(url)

# print(type(res.text))
soup = bs(res.text, 'html.parser') # print(response.text)와 비슷해

# print(soup.title)
# print(res.text[:500])
print(soup.title.string)  # html의 타이틀만 불ㄹ러와
print(soup.span) # span의 가장 상단만 가져와
print(soup.findAll('span')) 

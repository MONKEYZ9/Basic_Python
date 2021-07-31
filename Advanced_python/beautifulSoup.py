from typing import Sized
import requests as req
from bs4 import BeautifulSoup as bs

url = 'http://www.naver.com'
res = req.get(url)

# print(type(res.text))
soup = bs(res.text, 'html.parser') # print(response.text)와 비슷해

# file = open("C:\\Users\\mingzzang\\Desktop\\google.html", 'w')
# file.write(res.text)
# file.close()

print(soup.title)
# # print(res.text[:500])
# print(soup.title.string)  # html의 타이틀만 불ㄹ러와
# print(soup.span) # span의 가장 상단만 가져와
# print(soup.findAll('span')) 

from datetime import datetime

print(datetime.today().strftime('%y%m%d%h'))


search_rank_file = open('C:\\Users\\mingzzang\\Desktop\\link_partner.txt', 'a')


# html에서 모든 a태그를 가져오는 것
results =soup.find_all('a', 'link_partner')
rank = 1
for result in results:
    search_rank_file.write(str(rank)+'위'+result.get_text()+'\n')
    print(rank,'위 : ',result.get_text(), '\n')
    rank += 1
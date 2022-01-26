from bs4 import BeautifulSoup as bs
import requests


res = requests.get('https://codeforces.com/contests')
soup = bs(res.content, 'html.parser')
res = soup.select_one('#pageContent > div.contestList > div.datatable > div:nth-child(6) > table')
print(res)

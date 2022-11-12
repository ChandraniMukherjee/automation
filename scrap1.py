import requests
from bs4 import BeautifulSoup as b
page=requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.content)
soup=b(page.content,'html.parser')
print(soup.prettify())
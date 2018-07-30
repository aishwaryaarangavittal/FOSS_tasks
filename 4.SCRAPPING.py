import webbrowser
import requests
import bs4#contians eautiful soup4

str=raw_input("enter search parameter:")
res=requests.get('https://google.com/search?q='+str)
soup=bs4.BeautifulSoup(res.text,'lxml')
links=soup.select('.r a')#selector
results=min(10, len(links))
for i in range(results):
	   webbrowser.open('https://google.com' + links[i].get('href'))


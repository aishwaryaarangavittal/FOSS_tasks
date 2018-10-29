#it is wrong
import webbrowser
import requests
import bs4#contians beautiful soup4

# search term input
str=raw_input("enter search parameter:")

# using requests to request html content of the page.
res=requests.get('https://google.com/search?q='+str)

soup=bs4.BeautifulSoup(res.text,'lxml')

# selector to select required id or class from the parsed html.
links=soup.select('.r a')#selector

results=min(10, len(links))
for i in range(results):
	   webbrowser.open('https://google.com' + links[i].get('href'))


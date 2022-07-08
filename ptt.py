import bs4
import requests

data = requests.get("https://xn--42cah7d0cxcvbbb9x.com/%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%A1%E0%B8%B1%E0%B8%99%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%99%E0%B8%B5%E0%B9%89/")

soup = bs4.BeautifulSoup(data.text)
car = soup.find('article',{'class':'post-72 page type-page status-publish hentry'})
#print(car.find_all('td'))
print("ราคา น้ำมัน ปตท วันนี้")
name = 1
product = 2
for i in range(10):
	print(car.find_all('td')[name].text+" : "+car.find_all('td')[product].text)
	name = name+11
	product = product+11






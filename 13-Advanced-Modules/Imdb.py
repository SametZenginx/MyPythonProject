import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
htmlIcerik = response.content

soup = BeautifulSoup(htmlIcerik,"html.parser") #Siteyi parcalar.

basliklar = soup.find_all("td",{"class":"titleColumn"}) #film isimleri

ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"}) #film oylari

#boylari 250
a = float(input("Rating'i giriniz: "))

for baslik,rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")
    
    if (float(rating)>a):
        print("Film ismi: {} Filmin Rating'i: {}".format(baslik,rating))
import requests 

from bs4 import BeautifulSoup
url = "https://tr.wikipedia.org/wiki/G%C3%BCld%C3%BCr_G%C3%BCld%C3%BCr"
response = requests.get(url)

htmlIcerigi = response.content
soup = BeautifulSoup(htmlIcerigi,"html.parser")

"""
for i in soup.find_all("a"):
    print(i)
    print("*******************")
Bu başı a harfi olan bütün etiketleri alıcak.
"""

"""
for i in soup.find_all("a"):
    print(i.get("href"))
    print("*******************")
Bu href olanlari alicak
"""
"""
for i in soup.find_all("a"):
    print(i.text) A.text olan yazilari alıcak.
    print("*******************")
"""

print(soup.find_all("div",{"class":"mw-page-container"})) #Divleri aldık.

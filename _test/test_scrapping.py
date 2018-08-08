import requests
from bs4 import BeautifulSoup

from dtos.test_dtos import DTO_Songs
from test_repository import TestRepository 

def fetchSongs(el):
    for song in el:
        fields = song.find_all('span')
        level = fields[0].find('img').attrs['title']
        artist = fields[1].get_text()
        title = fields[2].get_text()
        date = fields[-1].get_text()
        s = DTO_Songs(level, artist, title, date)
        print(s.__dict__)
        TestRepository.saveTests(s.__dict__)
    return

url = "https://www.8notes.com/piano/classical/sheet_music/default.asp?orderby=6u"
r = requests.get(url)

if r.status_code != 200:
    print("Site não disponível")
    exit()

# soup.find('tag') -> only 1
# soup.find(id='id', class='class')
# soup.find_all() ->all results
# soup.find(attrs={"data-type":"content"})
# .get_text() -> retorna o valor real , html contnet do elemento

html = r.text

soup = BeautifulSoup(html, 'html.parser')

nav = soup.find(class_="pagination")
if nav is not None:
    last = nav.find_all('li')[-2].get_text()

last = int(last)

for i in range(1,last+1):
    print(i)
    url = "https://www.8notes.com/piano/classical/sheet_music/default.asp?page={}&orderby=6u".format(i)
    r = requests.get(url)
    html= r.text
    soup = BeautifulSoup(html, 'html.parser')

    el = soup.find_all(class_="listboxrow")
    fetchSongs(el)
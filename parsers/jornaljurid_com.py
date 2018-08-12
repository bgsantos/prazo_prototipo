from bs4 import BeautifulSoup
import requests
from tools.logger import createLog
from dtos.jornaljurid_dto import DTOJornalJuridHeaders

class JornalJurid():
    baseUrl = "https://www.jornaljurid.com.br"

    def __init__(self, category, subcategory = None):
        try:
            url = "{}/{}/{}".format(
                JornalJurid.baseUrl,
                category,
                subcategory if subcategory else ""
            )

            r = requests.get(url)
            if r.status_code == 404 or r.status_code == 500:
                createLog('error', 'O endereço {} não foi encontrado'.format(url))
                return None

        except Exception as e:
            createLog('error', e)
            return None

        self.soup = BeautifulSoup(r.text, 'html.parser', from_encoding="ISO-8859-1")

    def fetchNewsHeaders(self):
        resultList = self.soup.find_all(class_="search-result-list")
        headers = []

        if resultList == None:
            print("Tag não encontrada")
            return None

        for result in resultList[0].find_all('li'):
            publicacao = result.find_all(class_="date-post-search")[0].get_text()
            link = result.find_all('a')[1]['href']
            title = result.find_all('a')[1].get_text()

            headers.append(DTOJornalJuridHeaders(publicacao, link, title))
        
        return headers
    
    @classmethod
    def getNewsBody(cls, link):
        """"
        Retornar o artigo completo a partir do link
        """
        url = cls.baseUrl + link
        try:
            r = requests.get(url)
            if r.status_code == 404 or r.status_code == 500:
                createLog('error', 'O endereço {} não foi encontrado'.format(url))
                return None
        
        except Exception as e:
            createLog('error', e)
            return None

        soup = BeautifulSoup(r.text, 'html.parser', from_encoding="ISO-8859-1")

        if soup.find(class_="text-article") != None:
            body = soup.find(class_="text-article").text
            return body

        elif soup.find(class_="header-view") != None:
            body = soup.find(class_="header-view").find('p').text
            return body

        
         
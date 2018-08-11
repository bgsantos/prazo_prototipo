from bs4 import BeautifulSoup
from tools.logger import createLog

class DORJ():
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, 'html.parser')

    def getSumary(self):
        sumTitle = self.soup.find_all(attrs={"class":"ft11"})[1]
        print(sumTitle.get_text())

        el = sumTitle.next_sibling
        print("imediatamente após")
        print(el)
        for i in range(7):
            el = el.next_sibling
            print("sibling number " + str(i))
            print(el)
    
    def getAtosProcurador(self):
        anchors = self.soup.find_all(attrs={"class": "ft110"})
        for item in anchors:
            if "PROCURADOR-GERAL" in item.get_text() and len(item.get_text()) == 24:
                anchor = item
                print("Ancore found: " + item.get_text())

        print(anchor.next_sibling.next_sibling['class'])

        shouldContinue = True
        currentEl = anchor.next_sibling.next_sibling
        currentType = 'data'

        while shouldContinue: 

            if(currentEl['class'] == ['ft110'] and len(currentEl.get_text()) == 13):
                currentType = "data"
                createLog('debug', currentType + '||' + currentEl.get_text())
                currentEl = currentEl.next_sibling.next_sibling
            elif(currentEl['class'] == ['ft13'] or currentEl['class'] == ['ft116'] or currentEl['class'] == ['ft117']):
                currentType = "text"
                createLog('debug', currentType + '||' + currentEl.get_text())
                currentEl = currentEl.next_sibling.next_sibling
            else:
                print("Eu não me encaixo nas definições:" + str(currentEl))
                shouldContinue = False

                
            


        

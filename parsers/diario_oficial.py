from bs4 import BeautifulSoup
from tools.logger import createLog
from dtos.dorj_dto import DTODorjAtosProcurador, DTODorjDecisoesConselho
from datetime import datetime

class DORJ():
    """
    Realiza a extração de informações contidas no Diário Oficial do Estado do Rio.
    """
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, 'html.parser')

    def getDataEdicao(self):
        """
        Retorna a data da edição do Diário Oficial.
        """
        anchor = self.soup.find(attrs={"class": "ft13"})
        date = anchor.next_sibling.next_sibling 
        return date.get_text()        
    
    def getAtosProcurador(self):
        """
        Retorna uma lista com os DTOs referentes aos Atos do Procurador-Geral.
        """
        anchors = self.soup.find_all(attrs={"class": "ft110"})
        
        for item in anchors:
            if "PROCURADOR-GERAL" in item.get_text() and len(item.get_text()) == 24:
                anchor = item
                print("Ancore found: " + item.get_text())

        if anchor == None:
            raise(Exception("Atos do Procurador-Geral não encontrados"))

        currentEl = anchor.next_sibling.next_sibling
        currentData = None
        shouldContinue = True
        AtosList = []
        lineBreakIndicators = [['ft116'], ['ft117'], ['ft118'],['ft119'] ,['ft120']]

        while shouldContinue: 

            if(currentEl['class'] == ['ft110'] and len(currentEl.get_text()) == 13):
                currentType = "data"
                createLog('debug', currentType + '||' + currentEl.get_text())

                currentData = datetime.strptime(currentEl.get_text()[-10:], "%d.%m.%Y")  
                currentEl = currentEl.next_sibling.next_sibling

            elif(currentEl['class'] in lineBreakIndicators):
                currentType = "text"
                createLog('debug', currentType + '||' + currentEl.get_text())

                AtosList[-1].content += currentEl.get_text()

                currentEl = currentEl.next_sibling.next_sibling

            elif(currentEl['class'] == ['ft13']):
                currentType = "newLine"
                createLog('debug', currentType + '||' + currentEl.get_text())

                dto_rj = DTODorjAtosProcurador(currentData, currentEl.get_text())
                AtosList.append(dto_rj)

                currentEl = currentEl.next_sibling.next_sibling

            else:
                print("Eu não me encaixo nas definições:" + str(currentEl))
                shouldContinue = False
            
        return AtosList
                
    def getDecisoes(self):
        """
        Retorna lista com decisões tomadas pelo Conselho.
        """
        anchor = self.soup.find_all(attrs={"class": "ft19"})[-1]
        if(len(anchor.get_text()) != 39):
            print("Não foi possível encontrar a ancora")
            return False
        
        lineBreakIndicators = [['ft119'],['ft120'], ['ft121'],['ft219'],['ft220'], ['ft221'], ['ft222'], ['ft319'] ,['ft320'], ['ft321'],['ft322']]
        currentEl = anchor.next_sibling.next_sibling
        currentPage = 1
        DecisoesList = []

        while currentEl:
            if "Processo" in currentEl.get_text() and "nº" in currentEl.get_text():
                numberPos = currentEl.get_text().find('nº') 
                number = currentEl.get_text()[numberPos+2:numberPos+16]
                
                DecisoesList.append(DTODorjDecisoesConselho(number, currentEl.get_text()[numberPos+17:]))
                createLog('debug', "Novo Processo || {}".format(currentEl.get_text()))

            elif currentEl['class'] in lineBreakIndicators:
                DecisoesList[-1].content += currentEl.get_text()
                createLog('debug', "Continuação || {}".format(currentEl.get_text())) 

            currentEl = currentEl.next_sibling.next_sibling
            if currentEl == None:
                print("Final da página")
                currentPage += 1
                page = self.soup.find(id="page{}-div".format(str(currentPage)))

                if page == None:
                    print("Final do documento")
                    return DecisoesList

                currentEl = page.find('p')
        
    def isHtmlValid(self, html = None):
        """
        Valida o html com base nas formatações implementadas.
        """
        if html == None:
            html = self.html
        
        raise NotImplementedError()
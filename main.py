from parsers.diario_oficial import DORJ
from parsers.jornaljurid_com import JornalJurid
from settings import BASE_DIR
from mongo_repository import AtosRepository, DecisoesRepository, JornalJuridRepository

""" === Diário Oficial Rio de Janeiro 10/08/2018 === """
file = open(BASE_DIR+'/static/dorj.html', 'rb')

dorj = DORJ(file.read())

# Data da edição
print(dorj.getDataEdicao())

# dorj.getDecisoes()

# Recuperar atos do procurador
# allActs = dorj.getAtosProcurador()

# for a in allActs: 
#     AtosRepository.saveAtoProcurador(a)

""" === Diário Oficial Rio de Janeiro 09/08/2018 ==== """
# file = open(BASE_DIR+'/static/dorj_9.html', 'rb')

# dorj = DORJ(file.read())

# # Data da edição
# print(dorj.getDataEdicao())

"""Recuperar Decisões do conselho superior"""

# for d in dorj.getDecisoes():
#     DecisoesRepository.saveDecisoes(d)

""" Recuperar atos do procurador """
# allActs = dorj.getAtosProcurador()

# for a in allActs: 
#     AtosRepository.saveAtoProcurador(a)

jd = JornalJurid('jurisprudencia')

for h in jd.fetchNewsHeaders():
    JornalJuridRepository.saveNewsHeaders(h)

for h in JornalJuridRepository.getNewsHeaders():
    text = JornalJurid.getNewsBody(h['link'])
    print(JornalJuridRepository.setNewsBody(h['link'], text))

JornalJuridRepository.getNewsCSV()


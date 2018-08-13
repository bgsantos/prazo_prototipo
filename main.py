from parsers.diario_oficial import DORJ
from parsers.jornaljurid_com import JornalJurid
from settings import BASE_DIR, CSV_DIR
from mongo_repository import AtosRepository, DecisoesRepository, JornalJuridRepository

""" === Diário Oficial Rio de Janeiro 10/08/2018 === """

# Acessando texto do diário oficial convertido para html
file = open(BASE_DIR+'/static/dorj20180810.html', 'rb')

dorj = DORJ(file.read())

# Data da edição
print(dorj.getDataEdicao())

# Recuperar atos do procurador-geral
# Em seguida salvar info

for a in dorj.getAtosProcurador(): 
    AtosRepository.saveAtoProcurador(a)

""" === Diário Oficial Rio de Janeiro 09/08/2018 ==== """

file = open(BASE_DIR+'/static/dorj20180809.html', 'rb')

dorj = DORJ(file.read())

# # Data da edição
print(dorj.getDataEdicao())

"""Recuperar Decisões do conselho superior"""
for d in dorj.getDecisoes():
    DecisoesRepository.saveDecisoes(d)

""" Recuperar atos do procurador """

for a in dorj.getAtosProcurador(): 
    AtosRepository.saveAtoProcurador(a)


""" ==== Jornal de Notícias Jurídicas ===== """

jd = JornalJurid('jurisprudencia')

# Resgata o título das notícias e armazena no banco
for h in jd.fetchNewsHeaders():
    JornalJuridRepository.saveNewsHeaders(h)

# Recuperando e salvando o artigo completo a partir do link
print("Recuperando artigos completos...")
for h in JornalJuridRepository.getNews():
    text = JornalJurid.getNewsBody(h['link'])
    JornalJuridRepository.setNewsBody(h['link'], text)

"""==== Geração de CSVs ==="""
# Gerar CSV para news
JornalJurid.generateNewsCSV(JornalJuridRepository.getNews())

# Gerar csv para atos e decisões
DecisoesRepository.createCSV(CSV_DIR + '/decisoes.csv')
AtosRepository.createCSV(CSV_DIR + '/atos.csv')
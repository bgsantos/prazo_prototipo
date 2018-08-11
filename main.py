from parsers.diario_oficial import DORJ
from settings import BASE_DIR

file = open(BASE_DIR+'/static/dorj.html', 'rb')

dorj = DORJ(file.read())

# dorj.getSumary()
dorj.getAtosProcurador()
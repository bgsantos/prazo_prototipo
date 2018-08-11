from datetime import datetime
from settings import BASE_DIR

def createLog(file, msg):
    if not isinstance(file, str) or not isinstance(msg, str):
        return "Parametros não são strings"

    with open(BASE_DIR + "/logs/" + file + ".txt", 'a') as f:
        f.write("{} => {}\n".format(datetime.now(), msg))
    
    return
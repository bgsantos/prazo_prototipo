from pymongo import MongoClient
from dtos.dorj_dto import DtoDORJAtosProcurador, DtoDORJDecisoes
from dtos.jornaljurid_dto import DTOJornalJuridHeaders
from tools.logger import createLog
import csv

class AtosRepository():
    client = MongoClient()
    db = client['prazo']
    collection = db.atos

    @classmethod
    def saveAtoProcurador(cls, data):
        if not isinstance(data, DtoDORJAtosProcurador):
            createLog('error', "saveAtoProcurador recebeu objeto do tipo {}".format(type(data)))
            return False
        try:
            result = cls.collection.insert_one(data.__dict__)
            return result
        except Exception as e:
            createLog('error', e)
            return False

class DecisoesRepository():
    client = MongoClient()
    db = client['prazo']
    collection = db.decisoes

    @classmethod
    def saveDecisoes(cls, data):
        if not isinstance(data,DtoDORJDecisoes):
            createLog('error', "saveDecisoes recebeu objeto do tipo {}".format(type(data)))
            return False
        
        try:
            result = cls.collection.insert_one(data.__dict__)
            return result
        except Exception as e:
            createLog('error', e)
            return False

class JornalJuridRepository():
    client = MongoClient()
    db = client['prazo']

    @classmethod
    def saveNewsHeaders(cls, data):
        if not isinstance(data, DTOJornalJuridHeaders):
            createLog('error', "saveNewsHeaders recebeu objeto do tipo {}".format(type(data)))
            return False

        try: 
            result = cls.db.news.insert_one(data.__dict__)
            return result

        except Exception as e:
            createLog('error', e)
            return False
        
    @classmethod
    def getNewsHeaders(cls):
        try:
            result = cls.db.news.find()
            return result

        except Exception as e:
            createLog('error', e)
            return None

    @classmethod
    def setNewsBody(cls,link, body):
        try:
            result = cls.db.news.update({"link":link}, {'$set':{'body': body}})
            return result

        except Exception as e: 
            createLog('error', e)
            return False
    
    @classmethod
    def getNewsCSV(cls):
        # Isto deveria ir para um a classe
        c = csv.writer(open('news.csv', 'w', encoding= "ISO-8859-1"))
        c.writerow(["id", "data", "title", "link", "body"])

        for n in cls.getNewsHeaders():
            try:
                body =n['body']
            except:
                body = ""

            c.writerow([
                n['_id'],
                n['date'],
                n['title'],
                n['link'],
                body
            ])
    

        

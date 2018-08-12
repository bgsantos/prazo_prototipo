from pymongo import MongoClient
from dtos.dorj_dto import DTODorjAtosProcurador, DTODorjDecisoesConselho
from dtos.jornaljurid_dto import DTOJornalJuridHeaders
from tools.logger import createLog
import os
import csv

class AtosRepository():
    client = MongoClient()
    db = client[os.getenv('DB_NAME')]
    collection = db.atos

    @classmethod
    def saveAtoProcurador(cls, data):
        if not isinstance(data, DTODorjAtosProcurador):
            createLog('error', "saveAtoProcurador recebeu objeto do tipo {}".format(type(data)))
            return False
        try:
            result = cls.collection.insert_one(data.__dict__)
            return result
        except Exception as e:
            createLog('error', e)
            return False
    
    @classmethod
    def getAtosProcurador(cls):
        try:
            return cls.collection.find()
        except Exception as e:
            createLog('error', e)
            return None

    @classmethod
    def createCSV(cls, file):
        atos = cls.getAtosProcurador()
        if atos.count() == 0:
            return False

        output = csv.writer(open(file,'w'))

        output.writerow(['_id', 'date', 'content'])
        
        for a in atos:
            output.writerow(list(a.values()))

class DecisoesRepository():
    client = MongoClient()
    db = client[os.getenv('DB_NAME')]
    collection = db.decisoes

    @classmethod
    def saveDecisoes(cls, data):
        if not isinstance(data,DTODorjDecisoesConselho):
            createLog('error', "saveDecisoes recebeu objeto do tipo {}".format(type(data)))
            return False
        
        try:
            result = cls.collection.insert_one(data.__dict__)
            return result
        except Exception as e:
            createLog('error', e)
            return False
    
    @classmethod
    def getDecisoes(cls):
        try:
            return cls.collection.find()

        except Exception as e:
            createLog('error', e)
            return None

    @classmethod
    def createCSV(cls, file):
        decisions = cls.getDecisoes()
        if decisions.count() == 0:
            return False

        output = csv.writer(open(file,'w'))

        output.writerow(['_id', 'process_number', 'content'])
        
        for d in decisions:
            output.writerow(list(d.values()))

class JornalJuridRepository():
    client = MongoClient()
    db = client[os.getenv('DB_NAME')]

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
    def getNews(cls):
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
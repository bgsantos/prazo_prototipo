from pymongo import MongoClient, errors

class TestRepository():
    client = MongoClient()
    db = client['prazo']
    collection = db.songs   

    @classmethod
    def getTests(cls, filters=None):
        return cls.collection.find()

    @classmethod
    def saveTests(cls,data):
        try:
            result = cls.collection.insert_one(data)
            return result
        except errors.DuplicateKeyError as e:
            print(e)
            return None

    @classmethod
    def init(cls):
        cls.collection.create_index("title", unique=True)




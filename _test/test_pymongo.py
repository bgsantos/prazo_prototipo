from test_repository import TestRepository

class Teste():
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def __repr__(self):
        return str(self.__dict__)

TestRepository.init()

item_1 = {
    'title': 'teste',
    'content':'another one'
}

t1 = Teste('caneca','café')
print(t1)

print(TestRepository.saveTests(t1))
print(TestRepository.getTests()[0])


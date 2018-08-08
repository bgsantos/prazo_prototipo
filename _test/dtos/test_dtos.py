class DTO_Songs():
    """
    Lógicas de negócio podem ser realizadas nessa camada
    """
    def __init__(self, level, artist, title, date):
        self.level = level.strip()
        self.artist = artist.strip()
        self.title = title.strip()
        self.date = date
        print('inicializado com sucesso {}'.format(type(self)))


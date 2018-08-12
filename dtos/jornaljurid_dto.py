class DTOJornalJuridHeaders():
    def __init__(self, date, link, title, body=None):
        self.date = date
        self.link = link
        self.title = title
        self.body = body

    def __repr__(self):
        return "Notícia de {} : Título {} \n Link: {}".format(
            self.date,
            self.title,
            self.link
        )
    
class DtoDORJAtosProcurador():
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def __repr__(self):
        return "Ato do dia {}: {}".format(
            self.date,
            self.content
        )

class DtoDORJDecisoes():
    def __init__(self,process_number, content):
        self.process_number = process_number
        self.content = content

    def __repr__(self):
        return "Processo de nº {}. Conteúdo:{}".format(
            self.process_number,
            self.content
        )
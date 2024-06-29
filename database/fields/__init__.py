from sqlalchemy import Column, Integer, String


class Field:
    type = None

    def integer(self, name):
        Column(name, Integer, primary_key=True)

    def Char(self, name, nullable=False):
        return Column(name, String(16), nullable=nullable)

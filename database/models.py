from sqlalchemy import Integer, Column

from database.metadata import Meta


class Model(metaclass=Meta):
    id = Column(Integer, primary_key=True)

    def search(self):
        return "search method from Model."

    def create(self):
        return "create method from Model."

    def update(self):
        return "update method from Model."

    def delete(self):
        return "delete method from Model."
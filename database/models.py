from sqlalchemy import Integer, Column

from database.metadata import Meta


class Model(metaclass=Meta):
    id = Column(Integer, primary_key=True)

    def search(self):
        # print(self.env.__table__)
        self.__table__.columns.id.table = self.__table__
        return self.db.query(self.__table__).filter(self.__table__.columns.id == 1).all()

    def create(self):
        return "create method from Model."

    def update(self):
        return "update method from Model."

    def delete(self):
        return "delete method from Model."
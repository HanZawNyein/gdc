from sqlalchemy import Column, String

from database.db import Base, engine
from database.env import ENV
from database.models import Model

if __name__ == '__main__':
    class BaseModel(Model):
        _name = "res_users"

        name = Column(String)
        username = Column(String, nullable=True)

        def create(self):
            res = super().create()
            print("create method from BaseModel")
            return res


    class BaseModel2(Model):
        _name = "res_users2"
        _inherit = "res_users"

        username = Column(String, nullable=False)
        name = Column(String)
        new_field = Column(String)
        email = Column(String)
        phone = Column(String)

        def create(self):
            res = super().create()
            print("create method from BaseModel")
            return res


    ENV.start()
    results = ENV.get_all_tables()
    # print(results)
    Base.metadata.create_all(engine)

    user = ENV['res_users']()
    # print(ENV['res_users'])

    # print(ENV._models)
    # print(user.create())
    # print(user.__table__)

    # print()
    # print(dir(user.id))
    # print()
    user.__table__.columns.id.table = user.__table__
    # print(user.env)
    print(user.search())
    # user.id.table = user
    # print(user.db.query(user.__table__).filter(user.__table__.columns.id == 1).first())

    # print(dir())#.query(ENV['res_users']).filter(user.id == 1).first())

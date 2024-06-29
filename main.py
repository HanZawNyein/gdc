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

        def create(self):
            res = super().create()
            print("create method from BaseModel")
            return res


    ENV.start()
    results = ENV.get_all_tables()
    Base.metadata.create_all(engine, tables=results)

    user = ENV['res_users']()
    print(ENV.models)
    print(user.create())

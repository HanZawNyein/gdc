from typing import Optional

from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.db import engine, Base,metadata_obj
from env import ENV
from metadata import Meta


class Model(metaclass=Meta):
    __abstract__ = True

    id = Column(Integer, primary_key=True)


    # id: Mapped[int] = mapped_column(primary_key=True)

    def search(self):
        return "search method from Model."


if __name__ == '__main__':
    class BaseModel(Model):
        _name = "res_users"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        username = Column(String,nullable=True)
        new_field = Column(String)

        def a(self):
            print("**")

    ENV.start()
    results = ENV.get_all_tables()
    print(results)
    # print(ENV._models)
    # Base.metadata.create_all(engine, tables=results)  # ,tables=ENV)
    user = ENV._models['res_users']()
    print(dir(ENV._models['res_users']))
    user.a()
    print(results)

    metadata_obj.create_all(engine,tables=results)  # ,tables=ENV)
    # print(dir(ENV['res_users']))





    # class BaseModel2(Model):
    #     _inherit = "res_users"
    #
    #     fullname: Mapped[Optional[str]]
    #
    #     def a(self):
    #         super().a()
    #         print("***")


    # ENV.start()
    # tables = ENV._get_all_tables()
    # print(tables)
    #
    # user = ENV._models['res_users']
    # print(user)
    # Base.metadata.create_all(engine, tables=[user])  # ,tables=ENV)
    # model = ENV['res_users']
    # model.a()

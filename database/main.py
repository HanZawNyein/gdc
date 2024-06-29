from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from env import ENV
from metadata import Meta


class Model(metaclass=Meta):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def search(self):
        return "search method from Model."


if __name__ == '__main__':
    class BaseModel(Model):
        _name = "res_users"

        name: Mapped[str] = mapped_column(String(30))

        def a(self):
            print("**")


    class BaseModel2(Model):
        _inherit = "res_users"

        fullname: Mapped[Optional[str]]

        def a(self):
            super().a()
            print("***")


    ENV.start()
    print(dir(ENV))
    model = ENV['res_users']
    model.a()

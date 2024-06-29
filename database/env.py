# ENV = {}

from sqlalchemy import Table, Column

from database.db import Base


class Env(object):
    _models: dict[str, object] = {}
    models: dict[str, object] = {}


    def __setitem__(self, model_name, instance):
        self._models[model_name] = instance

    def __getitem__(self, model_name):
        return self._models.get(model_name)

    def start(self):
        # Instantiate all model classes stored in the dictionary
        for name, cls in self._models.items():
            cls.__bases__ = tuple(cls.__bases__) + (Base,)
            cls.name = cls._name if hasattr(cls, '_name') else cls._inherit
            # cls.__tablename__ = cls._name if hasattr(cls, '_name') else cls._inherit
            cls.name = cls._name if hasattr(cls, '_name') else cls._inherit
            self._models[name] = cls
        self.models = self._models.copy()
        # for name, cls in self._models.items():
        #     self._models[name] = cls()

    def get_all_tables(self):
        results = []
        for name, cls in self._models.items():
            new_table = self.create_table(name)
            self._models[name].__table__ = new_table
            results.append(new_table)
        return results

    def create_table(self, model_name):
        model_cls = self._models[model_name]
        model_cls.__tablename__ = model_name.lower().replace('.', '_')
        # metadata = MetaData()
        # print(model_cls.__dict__.items())
        # columns  = []
        # print(dir(model_cls))
        columns = []
        for attr in dir(model_cls):
            if not attr.startswith('__'):
                obj = getattr(model_cls,attr)
                if isinstance(obj,Column):
                    obj.name = attr
                    # print(obj,type(obj))
                    columns.append(obj)
        # columns.extend([attr for attr_name, attr in model_cls.__dict__.items() if isinstance(attr, Column)])
        for column in columns:
            if not column.name:
                column.name = column.key
        table = Table(model_cls.__tablename__, Base.metadata, *columns)
        return table

    # def create_table(self, name):
    #     return Table(
    #         name,
    #         metadata_obj,
    #         Column("user_id", Integer, primary_key=True),
    #         Column("user_name", String(16), nullable=False),
    #         Column("email_address", String(60), key="email"),
    #         Column("nickname", String(50), nullable=False),
    #     )

    # def get_all_methods(self, cls):
    #     # methods_dict = {}
    #     # for name, cls in self.models.items():
    #         methods = [method_name for method_name, _ in inspect.getmembers(cls, predicate=inspect.isfunction)]
    #         # methods_dict[name] = methods
    #     # print(methods_dict)
    #         return methods


ENV = Env()

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
            # cls.name = cls._name if hasattr(cls, '_name') else cls._inherit
            self._models[name] = cls
        self.models = self._models.copy()

    def get_all_tables(self):
        results = []
        for name, cls in self._models.items():
            ...
            new_table = self.create_table(name)
            self._models[name].__table__ = new_table
            results.append(new_table)
        return results

    def create_table(self, model_name):
        model_cls = self._models[model_name]
        model_cls.__tablename__ = model_name.lower().replace('.', '_')
        columns = set()
        for attr in dir(model_cls):
            if not attr.startswith('__'):
                obj = getattr(model_cls,attr)
                if isinstance(obj,Column):
                    # obj.__tablename__ =model_cls.__tablename__
                    if not obj.name:
                        obj.name = attr
                    columns.add(obj)
                    # try:

                    # except Exception as e:
                    #     print(e)
        # print(columns)
        # print(self.models)
        # for attr in dir(model_cls):
        #     print(attr)
        # print(columns)
        for col in columns:
            if col.table is not None:
                col.table = None
            # print(type( col.table))
            # print(col.table)
        # print()
        # print(model_cls.__tablename__)
        table = Table(model_cls.__tablename__, Base.metadata, *columns)
        return table

ENV = Env()

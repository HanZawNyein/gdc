# ENV = {}
from db import Base


class Env(object):
    models: dict[str, object] = {}

    def __setitem__(self, model_name, instance):
        self.models[model_name] = instance

    def __getitem__(self, model_name):
        return self.models.get(model_name)

    def start(self):
        # Instantiate all model classes stored in the dictionary
        for name, cls in self.models.items():
            # print(name, cls)
            cls.__bases__ = (Base,) + tuple(cls.__bases__)
            self.models[name] = cls()
            # print(cls.__bases__)


ENV = Env()

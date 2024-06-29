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
        # for name, cls in self.models.items():
        #     # Create a new class that inherits from the original class
        #     new_class = type(cls.__name__, (cls,Base), cls.__dict__.copy())
        #     # Replace the original class with the new class in the dictionary
        #     self.models[name] = new_class()

        self.models = {name: cls() for name, cls in self.models.items()}


#
ENV = Env()

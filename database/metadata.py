from database.env import ENV as env


class Meta(type):
    def __new__(cls, name, bases, dct):
        # bastract = dct.get('__abstract__', None)

        # if bastract:
        #     return super().__new__(cls, name, bases, dct)

        # Check if _name and _inherit are in the class dictionary
        model_name = dct.get('_name', None)
        inherit_class_name = dct.get('_inherit', None)

        # If _inherit is specified and exists in models, create a new class with the desired inheritance
        # print(dct)
        if inherit_class_name:
            inherit_class = env[inherit_class_name]
            if inherit_class:
                print(cls.__dict__.items())
                org = dct.copy()
                # print(org)
                # print(type(bases))
                # print(bases)
                # print(inherit_class)
                bases = (inherit_class,)
                # dct.update(org)
                # print(dct)

        # Create the new class
        instance = super().__new__(cls, name, bases, dct)

        # Register the new class in the models dictionary
        if model_name:
            env[model_name] = instance

        if inherit_class_name and not model_name:
            env[inherit_class_name] = instance

        return instance

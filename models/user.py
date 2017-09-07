from models.mongox import Mongox

Model = Mongox


class User(Model):

    @classmethod
    def valid_names(cls):
        names = super(Model, cls).valid_names()
        names = names + [
            ('username', str, ''),
            ('uid', str, ''),
        ]
        return names

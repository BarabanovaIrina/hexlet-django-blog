from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
)


class Article(Model):
    name = CharField(max_length=200)  # название статьи
    body = TextField()  # тело статьи
    timestamp = DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return self.__repr__()

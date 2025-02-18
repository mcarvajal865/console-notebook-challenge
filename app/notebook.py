# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code: str = code

        self.title: str = title

        self.text: str = text

        self.importance: str = importance

        self.current_datetime = datetime.now()

        self.tags: list[str]

    def add_tags(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return (f"date: {self.current_datetime},\n title:{self.title}, text:{self.text}")

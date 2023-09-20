import peewee as pw
from config import DATABASE


class Model(pw.Model):
    class Meta:
        database = DATABASE


class Decision(Model):
    class Meta:
        table_name = 'decisions'

    number = pw.CharField()
    date = pw.DateField()
    case_number = pw.CharField()
    place = pw.CharField()
    judge = pw.CharField()
    text = pw.TextField()

    def __str__(self):
        return f'Решение {self.number} дела № {self.case_number} судьи {self.judge} от {self.date}, г. {self.place}'


Decision.create_table()

from django.db import models

class Todo(models.Model):
    # 컬럼 =
    name = models.CharField('NAME', max_length=5, blank=True) # blank는 빈값을 허용한다.
    todo = models.CharField('TODO', max_length=50) # blank Default는 False 이다.

    def _str_(self):
        return self.todo

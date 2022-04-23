from django.db import models


class Todo(models.Model):
    # 컬럼 =
    name = models.CharField('NAME', max_length=5, blank=True)  # blank는 빈값을 허용한다.
    todo = models.CharField('TODO', max_length=50)  # blank Default는 False 이다.

    def _str_(self):
        return self.todo

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.name: # self.name의 값이 없다면
            self.name = '홍길동'
            super().save()
            # 상위 클래스의 save 메소드를 호출하는 것을 잊지않을 것.
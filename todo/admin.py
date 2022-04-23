from django.contrib import admin

from todo.models import Todo


@admin.register(Todo) # 컨트롤 + 스페이스바 두번눌러서 제안
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')

from django.http import JsonResponse
from django.views.generic import ListView

from todo.models import Todo


class ApiTodoLV(ListView):
    model = Todo
    # template_name =


    # def get(self, request, *args, **kwargs):
    #     tmpList = [
    #         {'id': 1, 'name': 'd테스트1', 'todo': '테스트 내용 1'},
    #         {'id': 2, 'name': 'd테스트4', 'todo': '테스트 내용 4'},
    #         {'id': 3, 'name': 'd테스트2', 'todo': '테스트 내용 2'},
    #         {'id': 4, 'name': 'd테스트3', 'todo': '테스트 내용 3'},
    #     ]
    #     return JsonResponse(data=tmpList, safe=False)
    #

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)

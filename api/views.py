from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import BaseDeleteView
from django.views.generic.list import BaseListView

from todo.models import Todo


class ApiTodoLV(BaseListView):
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
#
@method_decorator(csrf_exempt, name='dispatch')
class ApiTodoDelV(BaseDeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object();
        self.object.delete()
        return JsonResponse(data={}, status=204)
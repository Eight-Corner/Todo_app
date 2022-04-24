from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from todo.models import Todo


class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'
# template_name 속성은 RedirectView를 제외한 모든 뷰에서 사용되기 때문에 template_name을 먼저 지정해준다.
# 그 외 필요한 속성들을 override 한다.
class TodoCV(CreateView):
    model = Todo
    fields = '__all__' # 모든 fields를 쓰는 표현
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')
    # 폼 처리가 끝나면 리다이렉트 시켜줄 url은 todo의 list로 이동시킨다.

class TodoLV(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'

class TodoDelV(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')
    # success_url을 지정할 때는 reverse_lazy 함수나 reversed 함수를 결정해서 사용하는데,
    # 여기서 reverse_lazy를 사용해야 한다. 그 이유는, success_url이 실행되는 시점에는
    # urls 파일 모듈이 아직 로딩이 안되어있기 때문이다. success_url = reverse_lazy 함수를 사용한다고 알아두면 좋다.

    # ----------------
    # 파이썬에서는 다중 상속을 받아야할 때 List를 먼저쓸지, Create를 먼저 쓸지 상속받는 순서도 중요하다. 이에 대한 설명은 Docs 참고
class TodoMOMCV(MultipleObjectMixin, CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form_list.html'
    success_url = 'todo:mixin'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)
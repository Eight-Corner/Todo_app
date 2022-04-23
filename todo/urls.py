from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),

    path('create/', views.TodoCV.as_view(), name='create'),
    path('list/', views.TodoLV.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete'),
    # delete는 pk(기본키)를 Integer로 넣어야 하기 때문에 <int:pk> 식으로 작성하는데, 이러한 표현을 path-coverter라고 한다.
    # 숫자가 들어오면 Integer로 변환해서 view에 넘겨주는 역할을 한다.
]

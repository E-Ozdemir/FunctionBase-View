
from django.urls import path
from .views import home,todoList,todoListCreate,toDo_list,todoListUpdate,todoListDelete


urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('toDo_list/', toDo_list),
    path('todoListUpdate/<int:pk>', todoListUpdate),
    path('todoListDelete/<int:pk>', todoListDelete),
]

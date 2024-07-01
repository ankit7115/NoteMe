from django.urls import path
from . import views

urlpatterns = [
    path('',views.getTodos),
    path('todo/',views.getTodos),
    path('todo/create/',views.createTodo),
    path('todo/<str:pk>/',views.getTodo),
    path('todo/<str:pk>/update/',views.updateTodo),
    path('todo/<str:pk>/delete/',views.deleteTodo),
]

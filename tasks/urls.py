from django.urls import path
from . import views

app_name='tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter/<str:filter_type>/', views.filter_task,name='index1'),
    path('AddTask/',views.add_task, name='addtask'),
    path('delete/<int:task_id>',views.delete_task,name='delete'),
    path('complete/<int:task_id>',views.complete_task,name='complete'),
    path('update_task/<int:task_id>',views.update_task,name='update'),
]
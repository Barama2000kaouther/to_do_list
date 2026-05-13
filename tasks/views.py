from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.


def get_task_content(task):
  form=TaskForm()
  count_tasks=task.count()
  return {
       'form':form,
      'all_tasks':task,
      'count_tasks':count_tasks
  } 

def index(request):
  tasks=Task.objects.all().values()
  context=get_task_content(tasks)
  return render(request,"tasks/index.html",context)
  
def filter_task(request,filter_type):

  if filter_type=='all': 
     return redirect('tasks:index')
    
  elif filter_type=='active':
      tasks=Task.objects.values().filter(is_completed=False)
     
  elif filter_type=='completed':
      tasks=Task.objects.values().filter(is_completed=True)
      
  context=get_task_content(tasks)
  return render(request,"tasks/index.html",context)
      
  
  
 

def add_task(request):
  if request.method=="POST":
    form=TaskForm(request.POST)
    if form.is_valid():
       form.save()
       return redirect('tasks:index')
    else:
      return redirect('tasks:index')
    
  return redirect('tasks:index')
  
    
def delete_task(request,task_id):
  if request.method=='POST':
      deletedTask=get_object_or_404(Task,id=task_id)
      deletedTask.delete()
      return redirect('tasks:index')
    
  return redirect('tasks:index')

def complete_task(request,task_id):
  if request.method=='POST':
       task = get_object_or_404(Task,id=task_id)
       task.is_completed = not task.is_completed
       task.save()
       return redirect('tasks:index')
   
  return redirect('tasks:index')
        
def update_task(request,task_id):
     if request.method=='POST':
       task = get_object_or_404(Task,id=task_id)
       task.task=request.POST['update_task']
       task.save()
       return redirect('tasks:index')
     else:
       return redirect('tasks:index')
 
 
 
    